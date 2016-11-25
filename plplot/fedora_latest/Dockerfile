# Distro
FROM fedora:latest
MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Update sources
RUN dnf -y upgrade

# Get dependencies, these are in alphabetical order
#
# Missing:
#   ttf fonts
#
#   D compiler.
#   PDL (Perl Data Language).
#
RUN dnf -y install cairo-devel
RUN dnf -y install cmake
RUN dnf -y install fedora-gnat-project-common gprbuild
RUN dnf -y install gcc
RUN dnf -y install gcc-c++
RUN dnf -y install gcc-gfortran
RUN dnf -y install git
RUN dnf -y install gtk2-devel
RUN dnf -y install java-1.8.0-openjdk-devel
RUN dnf -y install lasi-devel
RUN dnf -y install libharu-devel
RUN dnf -y install lua
RUN dnf -y install lua-libs
RUN dnf -y install ocaml
RUN dnf -y install octave-devel
RUN dnf -y install pango-devel
RUN dnf -y install perl-XML-DOM
RUN dnf -y install perl-XML-Parser
RUN dnf -y install python
RUN dnf -y install python2-numpy
RUN dnf -y install PyQt4-devel
RUN dnf -y install qhull-devel
RUN dnf -y install qt-devel
RUN dnf -y install shapelib-devel
RUN dnf -y install sip-devel
RUN dnf -y install swig
RUN dnf -y install tcl-devel
RUN dnf -y install wxGTK3

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
