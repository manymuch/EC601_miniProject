# EC601_miniProject 2 deep learning


# Task
building a deep learning project, including training, testing

# Usage

if you are running on SCC, you can easily load the module below by:
```
module load python/3.6.2
module load cuda/9.1
module load cudnn/7.1
module load tensorflow/r1.8
```
and then, train the networks, using CIFAR-10 datasets:
```
python cars3.py --train --test --epochs=10
```
it will train the networks for 10 epochs, save the parameters as a npz file and then test on testing dataset.

Also, you can continue training on a pretrained parameters using:
```
python cars.py --retrain --lr_start=1e-4
```
Remember to adjust learning rate start point by using --lr_start when retraining