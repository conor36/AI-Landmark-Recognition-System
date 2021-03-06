# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DsEPl2VyFqZPqv1ByBE0FXBb8YOx0Kxc
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import pandas as pd
import IPython.display as display
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os, time
from google.colab import files
from IPython.display import Image

#linking of google colab to google drive

from google.colab import drive
drive.mount('/content/drive')

#PATH_OF_DATA= '/content/drive/"My Drive"/Images/2061'
#!ls {PATH_OF_DATA}

Image('/content/drive/My Drive/Images/2061/image1.jpg')


#CNN model using Keras

def model():

  model = keras.models.Sequential([
                                 keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same', input_shape=(160, 160, 3) ),
                                 keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same', name='block0_conv2'), 
                                 keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block0_pool1'), #end of block 0
                                 keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', name='block1_conv1'),
                                 keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', name='block1_conv2'), 
                                 keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block1_pool1'), 
                                 keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block2_conv1'), 
                                 keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='block2_conv2'), 
                                 keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block2_pool1'), # end of block2
                                 keras.layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='block3_conv1'), 
                                 keras.layers.MaxPooling2D((2, 2), strides=(2, 2), name='block3_pool'), # end of block3, we use only 3 blocks
                                 keras.layers.Flatten(), 
                                 keras.layers.Dense(512, activation='relu'), 
                                 keras.layers.Dropout(0.4, name='Dropout_1'), 
                                 keras.layers.Dense(1, activation='sigmoid')
                                 ])

  model.summary()


#training the model for CNN
def trainingdata():

  path_train = '/content/drive/"My Drive"/Images'

  train_2061 = os.path.join('/content/drive/My Drive/Images/train/2061')
  train_6051 = os.path.join('/content/drive/My Drive/Images/train/6051')
  train_5554 = os.path.join('/content/drive/My Drive/Images/train/5554')
  train_6599 = os.path.join('/content/drive/My Drive/Images/train/6599')
  train_6651 = os.path.join('/content/drive/My Drive/Images/train/6651')
  train_6696 = os.path.join('/content/drive/My Drive/Images/train/6696')
  train_9633 = os.path.join('/content/drive/My Drive/Images/train/9633')
  train_9779 = os.path.join('/content/drive/My Drive/Images/train/9779')

#testing the model for CNN
def testingdata():

  test_2061 = os.path.join('/content/drive/My Drive/Images/test/test2061')
  test_6051 = os.path.join('/content/drive/My Drive/Images/test/test6051')
  test_5554 = os.path.join('/content/drive/My Drive/Images/test/test5554')
  test_6599 = os.path.join('/content/drive/My Drive/Images/test/test6599')
  test_6651 = os.path.join('/content/drive/My Drive/Images/test/test6651')
  test_6696 = os.path.join('/content/drive/My Drive/Images/test/test6696')
  test_9633 = os.path.join('/content/drive/My Drive/Images/test/test9633')
  test_9779 = os.path.join('/content/drive/My Drive/Images/test/test9779')

print("number of 206 training images: ", len(os.listdir(train_2061)))
print("number of 6051 training images: ", len(os.listdir(train_6051)))
print("number of 5554 training images: ", len(os.listdir(train_5554)))
print("number of 6599 training images: ", len(os.listdir(train_6599)))
print("number of 6651 training images: ", len(os.listdir(train_6651)))
print("number of 6696 training images: ", len(os.listdir(train_6696)))
print("number of 9633 training images: ", len(os.listdir(train_9633)))
print("number of 9779 training images: ", len(os.listdir(train_9779)))


print("number of 9779 testing images: ", len(os.listdir(test_2061)))
print("number of 6051 testing images: ", len(os.listdir(test_6051)))

#creating readable data for the Nerual Net
def fitdata():

  from tensorflow.keras.preprocessing.image import ImageDataGenerator

  train_datagen = ImageDataGenerator(rescale = 1/255.,
                                   horizontal_flip = True,
                                   zoom_range=0.0,
                                   height_shift_range=0.2,
                                   width_shift_range=0.1)

  test_datagen = ImageDataGenerator(rescale=1/255.,)

  train_datagenerator = train_datagen.flow_from_directory('/content/drive/My Drive/Images/train',
                                                        batch_size = 20,
                                                        class_mode='binary',
                                                        target_size=(160,160))


  test_datagenerator = train_datagen.flow_from_directory('/content/drive/My Drive/Images/test',
                                                        batch_size = 20,
                                                        class_mode='binary',
                                                        target_size=(160,160))



#compiling model
def compilemodel():

  model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.0001), 
             loss='binary_crossentropy', 
             metrics=['acc'])



  history = model.fit_generator(train_datagenerator, 
                              steps_per_epoch=100, 
                              epochs=15, 
                              validation_data=test_datagenerator, 
                              validation_steps=50, 
                              verbose=1)