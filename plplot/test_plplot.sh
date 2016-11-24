
# Move to source directory & update source.
cd plplot
pwd
git fetch origin
git merge origin/master

#
# Move to build directory, build and test. Note that all the files
# that are generated will disappear as soon as this stops running
# so we'll capture everything by redirecting the output to a file.
#
cd ../plplot-build
pwd
echo "<!-- cmake -->"
cmake ../plplot -DBUILD_TEST=ON -DENABLE_tk=OFF
echo "<!-- cache -->"
more CMakeCache.txt
echo "<!-- make  -->"
make VERBOSE=1
echo "<!-- ctest -->"
ctest --verbose
echo "<!-- done  -->"
