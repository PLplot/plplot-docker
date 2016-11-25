# Distro
FROM opensuse:tumbleweed
MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Update sources
RUN zypper --non-interactive update

# Get dependencies, these are in alphabetical order
#
# Missing:
#   D compiler.
#   PDL (Perl Data Language).
#
RUN zypper --non-interactive install cmake
RUN zypper --non-interactive install free-ttf-fonts
RUN zypper --non-interactive install gcc
RUN zypper --non-interactive install gcc-ada
RUN zypper --non-interactive install gcc-c++
RUN zypper --non-interactive install gcc-fortran
RUN zypper --non-interactive install gcc-java
RUN zypper --non-interactive install git
RUN zypper --non-interactive install libcairo2
RUN zypper --non-interactive install libgtk-2_0-0
RUN zypper --non-interactive install libharu-devel
RUN zypper --non-interactive install libLASi-devel
RUN zypper --non-interactive install liblua5_2
RUN zypper --non-interactive install libpango-1_0-0
RUN zypper --non-interactive install libqt4-devel
RUN zypper --non-interactive install lua52
RUN zypper --non-interactive install ocaml
RUN zypper --non-interactive install octave
RUN zypper --non-interactive install octave-devel
RUN zypper --non-interactive install pango-devel
RUN zypper --non-interactive install perl-XML-DOM
RUN zypper --non-interactive install perl-XML-Parser
RUN zypper --non-interactive install python-devel
RUN zypper --non-interactive install python-numpy
RUN zypper --non-interactive install python-qt4
RUN zypper --non-interactive install python-qt4-devel
RUN zypper --non-interactive install python-sip
RUN zypper --non-interactive install python-sip-devel
RUN zypper --non-interactive install qhull-devel
RUN zypper --non-interactive install shapelib
RUN zypper --non-interactive install swig
RUN zypper --non-interactive install tcl
RUN zypper --non-interactive install tcl-devel
RUN zypper --non-interactive install wxWidgets-3_0-devel

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
