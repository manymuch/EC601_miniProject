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
from keras.applications.mobilenet import MobileNet
from keras.losses import squared_hinge

def load_cars_train():
    data_dir = "./../../data/cifar10"

    file = os.path.join(data_dir,"data_batch_1")
    with open(file,'rb') as fo:
        dict = pickle.load(fo,encoding='bytes')
    return  np.array(dict[b'data']), np.array(dict[b'labels'])









# nn
epochs = 20
lr_start = 1e-5

X_train, Y_train = load_cars_train()
X_train = np.reshape(X_train,(-1,32,32,3))
Y_train = to_categorical(Y_train, num_classes=10)

print(X_train.shape)
print(Y_train.shape)


input = Input(shape=(32,32,3),name="inputs0")
model = MobileNet(input_shape=(32,32,3),weights=None,include_top=None)(input)
model = Flatten()(model)
model = Dense(1024, name='dense1',activation='relu')(model)
model = BatchNormalization(name='bn1')(model)
model = Dense(1024, name='dense2',activation='relu')(model)
model = BatchNormalization(name='bn1')(model)
model = Dense(10,name='last')(model)
mobile_model = Model(inputs=[input],outputs=[model])


opt = Adam(lr=lr_start)
mobile_model.compile(loss=squared_hinge, optimizer=opt, metrics=['acc'])
mobile_model.summary()

history = mobile_model.fit(X_train, Y_train,
                    batch_size=32,
                    #steps_per_epoch = 100,
                    epochs=epochs,
                    verbose=1)
#score = model.evaluate(X_test, Y_test, verbose=0)
