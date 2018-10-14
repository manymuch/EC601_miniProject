import numpy as np
import os
import pickle
import argparse
np.random.seed(1337)  # for reproducibility

import keras.backend as K
from keras.models import Sequential, Model
from keras.layers import Conv2D, Dense, Dropout, Activation, BatchNormalization, MaxPooling2D,Input

from keras.layers import Flatten
from keras.optimizers import SGD, Adam,rmsprop
from keras.callbacks import LearningRateScheduler
from keras.utils import np_utils,to_categorical
from keras.losses import squared_hinge

parser = argparse.ArgumentParser(description = 'neural network training parameters')
parser.add_argument('--epochs',action="store",type=int, default=1)
parser.add_argument('--lr_start',action="store",type=float, default=1e-3)
parser.add_argument('--batch_size',action="store",type=int, default=64)
args = parser.parse_args()

epochs = args.epochs
lr_start = args.lr_start
batch_size = args.batch_size
print("total training epochs = "+str(epochs))
print("learning rate start = "+str(lr_start))
print("batch_size = "+str(batch_size))




def load_cars_train():
    data_dir = "./../../data/cifar10"

    file = os.path.join(data_dir,"data_batch_1")
    with open(file,'rb') as fo:
        dict = pickle.load(fo,encoding='bytes')
    return  np.array(dict[b'data']), np.array(dict[b'labels'])


X_train, Y_train = load_cars_train()
X_train = np.reshape(X_train,(-1,32,32,3))/255.0
Y_train = to_categorical(Y_train, num_classes=10)



model = Sequential()

#Conv1
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
#Conv2
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
#Conv3
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
#Conv4
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

#Conv5
model.add(Conv2D(128, (3, 3), padding='same'))
model.add(Activation('relu'))
#Conv6
model.add(Conv2D(128, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(1024))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10))
model.add(Activation('softmax'))


opt = rmsprop(lr=0.0001, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])
model.summary()

history = model.fit(X_train, Y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1)
#score = model.evaluate(X_test, Y_test, verbose=0)
