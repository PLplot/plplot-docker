#!/usr/bin/env python
#
# (re)-builds all of the docker images.
#

import subprocess

import image_names

for elt in image_names.names:
    cmd = ["docker", "build", "-t", elt[0], "./plplot/" + elt[1] + "/."]
    subprocess.call(cmd)



