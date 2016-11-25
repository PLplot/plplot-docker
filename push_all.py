#!/usr/bin/env python
#
# Push all of the docker images. You need to log in first..
#

import subprocess

import image_names

for elt in image_names.names:
    cmd = ["docker", "push", elt[0]]
    subprocess.call(cmd)

