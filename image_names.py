#!/usr/bin/env python
#
# Image names and directories as a list.
#

# Distro test images.
distro_test = [["plplot/arch-linux", "arch_linux"],
               ["plplot/centos-latest", "centos_latest"],
               ["plplot/debian-latest", "debian_latest"],
               ["plplot/debian-stable", "debian_stable"],
               ["plplot/fedora-latest", "fedora_latest"],
               ["plplot/opensuse-tumbleweed", "opensuse_tumbleweed"],
               ["plplot/ubuntu-latest", "ubuntu_latest"]]

# Python test images.
python_test = [["plplot/debian-latest-python27", "debian_latest_python27"],
               ["plplot/debian-latest-python34", "debian_latest_python34"]]

# All the test images.
names = distro_test + python_test
