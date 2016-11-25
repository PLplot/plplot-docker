# Distro
FROM ubuntu:latest
MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Update sources
RUN apt update
RUN apt --yes install apt-utils

# Get dependencies, these are in alphabetical order
RUN apt --yes install camlidl
RUN apt --yes install cmake
RUN apt --yes install default-jdk
RUN apt --yes install default-jre
RUN apt --yes install fonts-freefont-ttf
RUN apt --yes install gcc
RUN apt --yes install gdc
RUN apt --yes install gfortran
RUN apt --yes install git
RUN apt --yes install gnat
RUN apt --yes install g++
RUN apt --yes install itcl3
RUN apt --yes install itcl3-dev
RUN apt --yes install libcairo-dev
RUN apt --yes install libgtk2.0-dev
RUN apt --yes install libhpdf-dev
RUN apt --yes install liblasi-dev
RUN apt --yes install liblua5.2-dev
RUN apt --yes install liboctave-dev
RUN apt --yes install libpango1.0-dev
RUN apt --yes install libqhull-dev
RUN apt --yes install libshp-dev
RUN apt --yes install libxml-dom-perl
RUN apt --yes install libxml-parser-perl
RUN apt --yes install libwxgtk3.0-dev
RUN apt --yes install lua5.2
RUN apt --yes install ocaml
RUN apt --yes install octave
RUN apt --yes install pdl
RUN apt --yes install python-dev
RUN apt --yes install python-numpy
RUN apt --yes install python-qt4
RUN apt --yes install python-qt4-dev
RUN apt --yes install qt4-dev-tools
RUN apt --yes install sip-dev
RUN apt --yes install swig

# Set working directory
WORKDIR /plplot

# Get PLplot
RUN git clone git://git.code.sf.net/p/plplot/plplot plplot
RUN mkdir plplot-build

# Copy in the test shell script
COPY ./test_plplot.sh ./

# This is what what gets run when this is started.
CMD sh test_plplot.sh
