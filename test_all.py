#!/usr/bin/env python
#
# Test all of the docker images.
#

import argparse
import multiprocessing
import os
import subprocess
import sys

import image_names

parser = argparse.ArgumentParser(description = 'Batch testing of PLplot in various linux distros using Docker')

parser.add_argument('--max_processes', dest='maxp', type=int, required=False, default=2,
                    help = "The maximum number of processes to run in parallel.")

parser.add_argument('--plplot_repo', dest='plplot_repo', type=str, required=False, default="",
                    help = "Absolute path to a local repository.")

args = parser.parse_args()


def mp_worker(docker_image):
    print("Starting", docker_image)
    if (len(args.plplot_repo) > 0):
        cmd = ["docker", "run", "-v", args.plplot_repo + ":/plplot_repo", docker_image]        
    else:
        cmd = ["docker", "run", docker_image]
    out = subprocess.check_output(cmd, stderr = subprocess.STDOUT)
    with open(docker_image.split("/")[1] + ".txt", "wb") as outfp:
        outfp.write(out)
    print("Finished", docker_image)

docker_images = []
for elt in image_names.names:
    docker_images.append(elt[0])
    
pool = multiprocessing.Pool(args.maxp)
pool.map(mp_worker, docker_images)
