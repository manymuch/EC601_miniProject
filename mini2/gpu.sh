#!/bin/bash -l

#$ -P ece601

# Request 4 CPUs
#$ -pe omp 4

# Request 1 GPU (the number of GPUs needed should be divided by the number of CPUs requested above)
#$ -l gpus=0.25

# Specify the minimum GPU compute capability 
#$ -l gpu_c=3.5


module load python/2.7.13
module load cuda/8.0
module load cudnn/5.1
nvidia-smi
