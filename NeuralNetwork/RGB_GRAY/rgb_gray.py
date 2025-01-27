import os
import cv2
import numpy as np 
import tqdm
from random import randint

import keras as k
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten

from keras.preprocessing import image
from keras.callbacks import EarlyStopping

#gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imwrite('color2_gray.png', gray_image)

xtrain = cv2.imread('color.jpeg')
ytrain = cv2.imread('color_gray.png',0)
x2 = cv2.imread('color2.png')
y2 = cv2.imread('color2_gray.png',0)
s = xtrain.shape
xtrain = np.array([xtrain, x2])
ytrain = np.array([ytrain[:, :, np.newaxis], y2[:, :, np.newaxis]])



model = Sequential()
model.add(Conv2D(1, kernel_size=(1, 1),
                 activation='relu', input_shape=s))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

val_loss_monitor = k.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=0, verbose=0, mode='auto')
model.fit(xtrain, ytrain,callbacks=[val_loss_monitor], validation_split=0.5)

xtest = cv2.imread('fb.png')
xtest = np.array([xtest])
o = model.predict(xtest)
cv2.imwrite('fb_gray_model.png',o[0])

