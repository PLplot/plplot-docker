
test_plplot.sh is what is run in each of the docker instances. The version in each of the distribution folders should match this version. Due to the way docker is designed you cannot add a file from a higher directory then where the Dockerfile is located, so this file has to be copied into each of the sub-directories.
