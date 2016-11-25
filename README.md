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

### Comprehensive Testing ###

```sh
python pull_all.py  # This will pull the latest images.
python test_all.py
```

Note: By default test_all.py will test two images at once, if you want to run more (or less) tests in parallel use the --max_processes argument.

```sh
python test_all.py --max_processes 10
```
