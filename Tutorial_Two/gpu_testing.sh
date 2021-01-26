#!/bin/bash
export PATH=$PATH:/usr/local/cuda/bin

git clone https://github.com/wilicc/gpu-burn.git

cd ./gpu-burn

make >> progress.log 2>&1 # pipe error to log

./gpu_burn 300
