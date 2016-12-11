#!/usr/bin/env python
#
# (re)-builds the distro docker images.
#
import subprocess

import image_names

for elt in image_names.distro_test:
    cmd = ["docker", "build", "-t", elt[0], "./plplot/" + elt[1] + "/."]
    subprocess.call(cmd)
