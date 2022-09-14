#!/bin/bash

# `$*` expands the `args` supplied in an `array` individually
# or splits `args` in a string separated by whitespace.
bash -c "echo $*"

echo "Hello $1"
time=$(date)
echo "::set-output name=time::$time"
