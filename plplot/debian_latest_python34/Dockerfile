# Distro
FROM debian:latest
MAINTAINER Hazen Babcock <hbabcock@mac.com>

# Update sources
RUN apt update

# Get dependencies
RUN apt --yes install cmake
RUN apt --yes install gcc
RUN apt --yes install git
RUN apt --yes install libqhull-dev
RUN apt --yes install libshp-dev
RUN apt --yes install swig

RUN apt --yes install python3.4
RUN apt --yes install python3-dev
RUN apt --yes install python3-pip

# Set working directory
WORKDIR /plplot

# Get PLplot
RUN git clone git://git.code.sf.net/p/plplot/plplot plplot
RUN mkdir plplot-build

# Create configure python
RUN pip3 install virtualenv
RUN virtualenv -p /usr/bin/python3 venv
RUN . venv/bin/activate
RUN pip3 install numpy

# Copy in the test shell script
COPY ./test_plplot.sh ./

# Record when this image was made
RUN date > image_date.txt

# Volume for testing a local repo
VOLUME ["/plplot_repo"]

# This is what what gets run when this is started.
CMD sh test_plplot.sh
