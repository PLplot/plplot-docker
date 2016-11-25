### PLplot Docker ###

This project provides:

(1) Dockerfiles for generating docker images for the purpose of testing [PLplot](http://plplot.sourceforge.net/) on multiple linux distributions.

(2) Code to run the tests and analyze the results.


The PLplot docker image repository is [here](https://hub.docker.com/u/plplot/)

### Basic Testing ###

```sh
docker run plplot/XXX 2>&1 | tee XXX.txt
```

Where XXX is a docker image, for example:

```sh
docker run plplot/debian-latest 2>&1 | tee debian-latest.txt
```
