# Output
![Sample](https://raw.githubusercontent.com/TW-NCHC/AI-Services/master/Tutorial_Benchmark/image.png)

# Env. check

1. Nvidia Driver version: `nvidia-smi`, `nvidia-smi topo --matrix`, `nvidia-smi nvlink --status`
2. CUDA Version: `/usr/local/cuda-10.0/bin/nvcc --version`
3. Cudnn Version: `cat /usr/lib/x86_64-linux-gnu/include/cudnn.h | grep CUDNN_MAJOR -A 2`


# Materials 

excel: https://docs.google.com/spreadsheets/d/10D_sx9bpKWZLHDb-Po7j_R4wqSqK68AjhnH1t2UZKjo/edit?usp=sharing

## Task1: LeaderGPU - [Resnet-50](https://www.leadergpu.com/articles/429-tensorflow-resnet-50-benchmark)

This benchmark is using 'parameter server' approach to do Resnet-50 training. Sample code can be retrived from [Reedwm's Github Project](https://github.com/reedwm/benchmarks) as following:

```
git clone https://github.com/reedwm/benchmarks
cd benchmarks
git checkout num_steps_issue_1.10
cd scripts/tf_cnn_benchmarks/
```

### gpu:1 batch:32
```
python tf_cnn_benchmarks.py --num_gpus=1 --batch_size=32 --model=resnet50 --variable_update=parameter_server
```

### gpu:2 batch:128
```
python tf_cnn_benchmarks.py --num_gpus=2 --batch_size=128 --model=resnet50 --variable_update=parameter_server
```

## Task2: Tensorflow official [Resnet-50](https://www.tensorflow.org/guide/performance/benchmarks)

This benchmark is using [Horovod](https://github.com/horovod/horovod) and MPI approach to do Resnet-50 training. Sample code can be retrived from [Horovod Github Project](https://github.com/uber/horovod) as following:

```
git clone https://github.com/uber/horovod
cd horovod/examples/
```

try following code for testing.

```
python tensorflow_synthetic_benchmark.py
```

* NOTE: hvd.Compression.fp16 not work in this source code, just skip line:59 ! like this...
![img](https://snag.gy/qevcXm.jpg)
* this modification does NOT required in NGC tensorflow 18.12 container environment, due to Horovod has been upgraded to 0.15.1.

### run w/ mpi 
for 1 GPU
```
/usr/local/mpi/bin/mpirun -np 1 -H localhost:1 python tensorflow_synthetic_benchmark.py
```
for 8 GPU
```
/usr/local/mpi/bin/mpirun -np 8 -H localhost:8 python tensorflow_synthetic_benchmark.py
```
