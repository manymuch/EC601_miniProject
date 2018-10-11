import numpy as np
import os
import pickle
np.random.seed(1337)  # for reproducibility

import keras.backend as K
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, BatchNormalization, MaxPooling2D,Input

from keras.layers import Flatten
from keras.optimizers import SGD, Adam, RMSprop
from keras.callbacks import LearningRateScheduler
from keras.utils import np_utils,to_categorical
from keras.applications.vgg16 import VGG16
from keras.losses import squared_hinge

def load_cars_train():
    data_dir = "./../../data/cifar10"

    file = os.path.join(data_dir,"data_batch_1")
    with open(file,'rb') as fo:
        dict = pickle.load(fo,encoding='bytes')
    return  np.array(dict[b'data']), np.array(dict[b'labels'])



# nn
epochs = 20
lr_start = 1e-3

X_train, Y_train = load_cars_train()
X_train = np.reshape(X_train,(-1,32,32,3))/255.0
Y_train = to_categorical(Y_train, num_classes=10)

print(X_train.shape)
print(Y_train.shape)


model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same',
                 input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes))
model.add(Activation('softmax'))


opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
model.compile(loss='categorical_crossentropy',
              optimizer=opt,
              metrics=['accuracy'])
mobile_model.summary()

history = model.fit(X_train, Y_train,
                    batch_size=32,
                    #steps_per_epoch = 100,
                    epochs=epochs,
                    verbose=1)
#score = model.evaluate(X_test, Y_test, verbose=0)
