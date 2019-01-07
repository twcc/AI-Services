#!/bin/bash
export PATH=$PATH:/usr/local/cuda/bin

git clone https://github.com/wilicc/gpu-burn.git

cd ./gpu-burn

make >> progress.log

./gpu_burn 300
