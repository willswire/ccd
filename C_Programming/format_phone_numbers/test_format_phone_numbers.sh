#!/bin/bash

set -e

cmake -DCMAKE_BUILD_TYPE=Release -B $PWD/build/release -S $PWD
make -C $PWD/build/release/
./build/release/TestCode
