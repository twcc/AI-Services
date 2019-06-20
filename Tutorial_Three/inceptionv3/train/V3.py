from tensorflow.python.keras.layers import Dense, GlobalAveragePooling2D, Input
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.datasets import cifar10
from tensorflow.python.keras.preprocessing.image import ImageDataGenerator
from tensorflow.python.keras.applications.inception_v3 import *
from tensorflow.python.keras.optimizers import SGD
from tensorflow.python.keras.callbacks import ModelCheckpoint
from sklearn.preprocessing import OneHotEncoder
from fun.NCHC_CallBack_Function import NCHC_CallBack
from fun.util import helpResize 

import numpy as np
import skimage.io as io
import tensorflow.python.keras.callbacks
import time, os, sys, argparse
import tensorflow as tf
import tensorflow.python.keras
import tensorflow.python.keras.models
import tensorflow.keras.backend as K
import json
import requests
import click

@click.group()
def cli():
    pass

@click.command()
@click.option('--training_num','tn',default = 2000,help ="The total number of images will be used for training.")
@click.option('--validation_num','vn',default = 1000,help ="The total number of images will be used for validation.")
@click.option('--image_size','ims',default = 139,help ="Change the dimension of the input image.")
@click.option('--batch','bas',default = 62,help ="Set how many images per batch during training.")
@click.option('--epoch','epc',default = 10,help ="Set how many times loop through the model before end of the training.")
def start_training(tn,vn,ims,bas,epc):
    
    training_num = tn 
    validation_num = vn 
    image_size = ims
    batch_size = bas
    epochs = epc

    WEIGHTS_FOLDER = './weights/'
    #WEIGHTS_FOLDER = save_path
    if not os.path.exists(WEIGHTS_FOLDER):
        os.mkdir(WEIGHTS_FOLDER)

    # Check if image dimension is correct.
    if type(image_size) is list:
        val1 = image_size[0]
        val2 = image_size[1]
        if val1 < 139 or val2 < 139:
            print("The size is not ok....")
            sys.exit(2)
        elif type(image_size) is int:
            if image_size <139:
                print("The size is not ok...")
                sys.exit(2)

    # Show the training condition
    print("Image size is {}".format(image_size))
    print("The batch_size is {}".format(batch_size))
    print("The epochs is {}".format(epochs))

    # Load images and data from cifar 10
    (x_train,y_train),(x_validation,y_validation) = cifar10.load_data()

    # Load part of train and test data.
    x_train = x_train[:training_num]
    x_validation = x_validation[:validation_num]
    Y_train = y_train[:training_num]
    Y_validation = y_validation[:validation_num]
    
    print("Total Train & Validation Num as shown below")
    print("Num of training images : {}".format(x_train.shape[0]))
    print("Num of validation images : {}".format(x_validation.shape[0]))

    X_train,X_validation = helpResize(x_train,x_validation,image_size)

    # Check if both of the list has the correct length.
    Y_new_train = np.array([np.zeros(10) for x in range(len(Y_train))],dtype='float32')
    for i,x in enumerate(Y_train):
        Y_new_train[i][x] = 1
    Y_new_val = np.array([np.zeros(10) for x in range(len(Y_validation))],dtype='float32')
    for i,x in enumerate(Y_validation):
        Y_new_val[i][x] = 1

    # This could also be the output of a different Keras model or layer
    if type(image_size) is list:
        input_shape = tuple(image_size) + (3,)
    else:
        input_shape = (image_size,image_size,3)
    base_model = InceptionV3(weights='imagenet', include_top=False,input_shape=input_shape)
    
    # Get the output of the Inception V3 pretrain model.
    x = base_model.output

    # Works same as Flatten(), but Flatten has larger dense layers, it might cause worse overfitting.
    # However, if the user has a larger dataset then the user can use Flatten() instead of GlobalAveragePooling2D or GlobalMaxPooling2D
    x = GlobalAveragePooling2D()(x)
    
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(10, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Use SGD as an optimizer
    model.compile(optimizer=SGD(lr=0.0001, momentum=0.9), 
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

    datagen = ImageDataGenerator(
        rotation_range=0,  # Randomly rotate images in the range (degrees, 0 to 180)
        # Randomly shift images horizontally (fraction of total width)
        width_shift_range=0.1,
        # Randomly shift images vertically (fraction of total height)
        height_shift_range=0.1,
        zoom_range=0.,  # set range for random zoom
        # Set the mode for filling points outside the input boundaries
        horizontal_flip=True,  # randomly flip images
    )
    datagen.fit(X_train)
    histories = NCHC_CallBack()
    c_time = "{}_{}_{}_{}_{}".format(time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday,time.localtime().tm_hour,time.localtime().tm_min)
    mc = ModelCheckpoint(WEIGHTS_FOLDER+c_time+"_weights.{epoch:02d}-acc-{acc:.2f}-loss-{loss:.2f}.hdf5",
                         monitor='val_loss',
                         verbose=0, 
                         save_best_only=False,
                         save_weights_only=False,
                         mode='auto', period=1)

    # Fit the model on the batches generated by datagen.flow().
    model.fit_generator(datagen.flow(X_train, 
                                 Y_new_train,
                                 batch_size=batch_size),
                    callbacks = [ histories,mc ], #added here
                    epochs=epochs,
                    validation_data=(X_validation, Y_new_val)
                    )
    
    K.clear_session()
    del model

cli.add_command(start_training)
if __name__ == "__main__":
    cli()

