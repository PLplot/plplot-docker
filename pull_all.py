#!/usr/bin/env python
#
# Pull all of the PLplot docker images.
#

import subprocess

import image_names

for elt in image_names.names:
    cmd = ["docker", "pull", elt[0]]
    subprocess.call(cmd)
