#
# Note that all the files that are generated will disappear as soon
# as this stops running so we'll capture everything by redirecting
# the output to a file.
#
if test "$(ls -A /plplot_repo)"; then
    # Use local volume if available.
    echo "<!-- using local repo -->"
    cd plplot-build
    echo "<!-- cmake -->"
    cmake /plplot_repo -DBUILD_TEST=ON -DENABLE_tk=OFF
else
    # Move to source directory & update source.
    echo "<!-- using SF repo -->"
    cd plplot
    pwd
    git fetch origin
    git merge origin/master
    cd ../plplot-build
    pwd
    echo "<!-- cmake -->"
    cmake ../plplot -DBUILD_TEST=ON -DENABLE_tk=OFF
fi

# Build and test.	
echo "<!-- cache -->"
more CMakeCache.txt
echo "<!-- make  -->"
make VERBOSE=1
echo "<!-- ctest -->"
ctest --verbose
echo "<!-- done  -->"
