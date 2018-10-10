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


module load python/2.7.13
module load cuda/8.0
module load cudnn/6.0
module load tensorflow/r1.4
nvidia-smi
python cars.py

#qrsh -P ece601 -l gpus=1 -l gpu_c=3.5
