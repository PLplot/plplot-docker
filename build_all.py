#!/usr/bin/env python
#
# (re)-builds all of the docker images.
#
# Notes:
#   (1) arch-linux will always do a complete re-build even if nothing has
#       changed, not sure why.
#
import subprocess

import image_names

for elt in image_names.names:
    cmd = ["docker", "build", "-t", elt[0], "./plplot/" + elt[1] + "/."]
    subprocess.call(cmd)
