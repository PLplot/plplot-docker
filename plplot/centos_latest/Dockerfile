# Distro
FROM centos:latest
MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Update sources
RUN yum -y upgrade

# Get dependencies, these are in alphabetical order
#
# Missing:
#   D compiler
#   haru
#   LASi
#   octave
#   PDL (Perl Data Language)
#   qhull
#   shapelib
#   ttf fonts
#   wxWidgets
#
RUN yum -y install cairo-devel
RUN yum -y install cmake
RUN yum -y install gcc
RUN yum -y install gcc-c++
RUN yum -y install gcc-gfortran
RUN yum -y install gcc-gnat
RUN yum -y install git
RUN yum -y install gtk2-devel
RUN yum -y install java-1.8.0-openjdk-devel
RUN yum -y install lua
RUN yum -y install lua-devel
RUN yum -y install numpy
RUN yum -y install ocaml
RUN yum -y install pango-devel
RUN yum -y install perl-XML-DOM
RUN yum -y install perl-XML-Parser
RUN yum -y install python
RUN yum -y install PyQt4-devel
RUN yum -y install qt-devel
RUN yum -y install sip-devel
RUN yum -y install swig
RUN yum -y install tcl-devel

# Set working directory
WORKDIR /plplot

# Get PLplot
RUN git clone git://git.code.sf.net/p/plplot/plplot plplot
RUN mkdir plplot-build

# Copy in the test shell script
COPY ./test_plplot.sh ./

# Record when this image was made
RUN date > image_date.txt

# Volume for testing a local repo
VOLUME ["/plplot_repo"]

# This is what what gets run when this is started.
CMD sh test_plplot.sh
