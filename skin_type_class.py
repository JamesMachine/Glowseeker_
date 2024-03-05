import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cv2

import tensorflow as tf
from keras.applications.resnet50 import ResNet50
from keras.applications.resnet50 import preprocess_input
from keras.models import Sequential
from keras.layers import Dense

from keras.preprocessing.image import ImageDataGenerator



# images are bgr, plt expect rgb
img00001 = cv2.imread(r"C:\Users\james\OneDrive\DS\Glowseeker_\archive\Oily-Dry-Skin-Types\train\dry\dry_00f1189752d6631b2b22_jpg.rf.76aa1679ba838c9b368632b7ccb63dc0.jpg")
plt.imshow(img00001)    

# convert image to rgb
bgr_image = cv2.imread(r"C:\Users\james\OneDrive\DS\Glowseeker_\archive\Oily-Dry-Skin-Types\train\dry\dry_00f1189752d6631b2b22_jpg.rf.76aa1679ba838c9b368632b7ccb63dc0.jpg")
rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_image)

class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy')>0.999):
            print("\nReached 99.9% accuracy so cancelling training!")
            self.model.stop_training = True

train_datagen = ImageDataGenerator(validation_split=0.3,
                                   preprocessing_function=preprocess_input) # don't use rescale = 1./255

train_generator = train_datagen.flow_from_directory('Oily-Dry-Skin-Types',
                                                     target_size=(224,224),
                                                     batch_size=64,
                                                     shuffle=True,
                                                     class_mode='categorical',
                                                     subset='training')

validation_datagen = ImageDataGenerator(validation_split=0.3,
                                        preprocessing_function=preprocess_input)

validation_generator =  validation_datagen.flow_from_directory('Oily-Dry-Skin-Types',
                                                                target_size=(224,224),
                                                                batch_size=64,
                                                                class_mode='categorical',
                                                                subset='validation')    

model_res50 = Sequential()

model_res50.add(ResNet50(
    include_top=False,
    pooling='avg',
    weights='imagenet'
    ))

model_res50.add(Dense(3, activation='softmax'))

model_res50.layers[0].trainable = False 

model_res50.summary()

steps_per_epoch_training = len(train_generator)
steps_per_epoch_validation = len(validation_generator)

callbacks = myCallback()

model_res50.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

epoch = 2
fit_history = model_res50.fit_generator(
    train_generator,
    steps_per_epoch=steps_per_epoch_training,
    validation_steps=steps_per_epoch_validation,
    epochs=epoch,
    validation_data=validation_generator,
    verbose=1,
    callbacks=[callbacks]
)


model_res50.predict()

testGen = valAug.flow_from_directory(
	config.TEST_PATH,
	class_mode="categorical",
	target_size=(224, 224),
	color_mode="rgb",
	shuffle=False,
	batch_size=config.BS)
































