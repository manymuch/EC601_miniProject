#!/bin/bash -l

#$ -P ece601

# Request 4 CPUs
#$ -pe omp 1

# Request 1 GPU (the number of GPUs needed should be divided by the number of CPUs requested above)
#$ -l gpus=1

# Specify the minimum GPU compute capability
#$ -l gpu_c=4


#request 15 minutes maxium running time
#$ -l h_rt=0:15:00


module load python/3.6.2
module load cuda/9.1
module load cudnn/7.1
module load tensorflow/r1.8
nvidia-smi
python cars3.py

#qrsh -P ece601 -l gpus=1 -l gpu_c=3.5
