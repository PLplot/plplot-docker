# Distro
#
# I built this using this resource:
# https://github.com/czka/archlinux-docker
#
# I failed to get the images base/archlinux, base/arch and base/devel
# that are at hub.docker.com to work.
#
FROM archlinux_x86_64-base

MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Get dependencies, these are in alphabetical order
#
# Missing:
#   LASi 
#   PDL (Perl Data Language).
#
RUN pacman --noconfirm -Syu base-devel
RUN pacman --noconfirm -Syu cairo
RUN pacman --noconfirm -Syu cmake
RUN pacman --noconfirm -Syu dmd
RUN pacman --noconfirm -Syu gcc
RUN pacman --noconfirm -Syu gcc-ada
RUN pacman --noconfirm -Syu gcc-fortran
RUN pacman --noconfirm -Syu git
RUN pacman --noconfirm -Syu gtk2
RUN pacman --noconfirm -Syu jre7-openjdk
RUN pacman --noconfirm -Syu jdk7-openjdk
RUN pacman --noconfirm -Syu libharu
RUN pacman --noconfirm -Syu lua
RUN pacman --noconfirm -Syu ocaml
RUN pacman --noconfirm -Syu octave
RUN pacman --noconfirm -Syu pango
RUN pacman --noconfirm -Syu perl-xml-parser
RUN pacman --noconfirm -Syu python2
RUN pacman --noconfirm -Syu python2-numpy
RUN pacman --noconfirm -Syu python2-pyqt4
RUN pacman --noconfirm -Syu python2-sip
RUN pacman --noconfirm -Syu qhull
RUN pacman --noconfirm -Syu qt4
RUN pacman --noconfirm -Syu shapelib
RUN pacman --noconfirm -Syu sip
RUN pacman --noconfirm -Syu swig
RUN pacman --noconfirm -Syu tcl
RUN pacman --noconfirm -Syu ttf-freefont
RUN pacman --noconfirm -Syu wxgtk

# Set working directory
WORKDIR /plplot

# Get PLplot
RUN git clone git://git.code.sf.net/p/plplot/plplot plplot
RUN mkdir plplot-build

# Copy in the test shell script
COPY ./test_plplot.sh ./

# Record when this image was made
RUN date > image_date.txt

# This is what what gets run when this is started.
CMD sh test_plplot.sh
