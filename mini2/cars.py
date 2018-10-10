from __future__ import print_function
import argparse
import numpy as np
import os
import cPickle
np.random.seed(1337)  # for reproducibility

import keras.backend as K
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, BatchNormalization, MaxPooling2D
from keras.layers import Flatten
from keras.optimizers import SGD, Adam, RMSprop
from keras.callbacks import LearningRateScheduler
from keras.utils import np_utils
from keras.applications.mobilenet import MobileNet
from keras.losses import squared_hinge

def load_cars_train():
    data_dir = "./../../data/cifar10"

    file = os.path.join(data_dir,"data_batch_1")
    with open(file,'rb') as fo:
        dict = cPickle.load(fo)
    return  np.array(dict['data']), np.array(dict['labels'])

def load_cars_test():
    data_dir = "./../data/cars"
    ImageNpz = os.path.join(data_dir,"MNIST_test_images.npz")
    LabelNpz = os.path.join(data_dir,"MNIST_test_labels.npz")

    image = np.load(ImageNpz)["arr_0"]
    label = np.load(LabelNpz)["arr_0"]

    return image, label

parser = argparse.ArgumentParser(description='indicate the numbers of epoch and batchsize')
parser.add_argument('--epochs', type=int, default = 1)
parser.add_argument('--batchsize', type=int, default = 50)
args = parser.parse_args()



# nn
batch_size = args.batchsize
epochs = args.epochs
lr_start = 1e-3

X_train, Y_train = load_cars_train()
X_train.reshape(-1,32,32,3)



model = MobileNet(input_shape = [32,32,3],weights=None,classes = 10)

opt = Adam(lr=lr_start)
model.compile(loss=squared_hinge, optimizer=opt, metrics=['acc'])
model.summary()

history = model.fit(X_train, Y_train,
                    batch_size=batch_size, epochs=epochs,
                    verbose=1)
#score = model.evaluate(X_test, Y_test, verbose=0)
