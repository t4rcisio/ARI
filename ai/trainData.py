import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

from ai import createDataSet
from itools import storeManager, imageDownloader, imagesDataset
import tensorflow as tf
from tensorflow.keras import Sequential, regularizers
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Dropout
import numpy as np
from tensorflow.keras.models import save_model, load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
import matplotlib.pyplot as plt


class TrainData:

    model = False
    imageTools = imagesDataset.ImagesDataset()

    def train(self, epochs=25, trainSplit=0.7):

        datasetTools = createDataSet.DatasetManager()


        datagen = ImageDataGenerator(rotation_range=20, width_shift_range=0.1, height_shift_range=0.1, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
        (x_train, y_train), (x_test, y_test) = datasetTools.getData(trainSplit)


        x_train = x_train/255
        x_test = x_test/255

        y_train = y_train.reshape(-1,)
        y_test = y_test.reshape(-1,)



        self.model = Sequential([
            Conv2D(filters=30, kernel_size=(3, 3), activation='relu', input_shape=(30, 30, 3)),
            MaxPooling2D((2, 2)),
            Dropout(0.3),
            
            Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Dropout(0.2),
            
            Flatten(),
            Dense(256, activation='relu'),
            Dropout(0.5),
            Dense(256, activation='relu'),
            Dropout(0.3),
            Dense(7, activation='softmax')
        ])

        # Compile Model
        optimizer = Adam(learning_rate=0.001)
        self.model.compile(optimizer=optimizer, loss='sparse_categorical_crossentropy', metrics=['accuracy'])

        # Train Model with Data Augmentation
        history = self.model.fit(datagen.flow(x_train, y_train, batch_size=32), steps_per_epoch=int(len(x_train) / 30), epochs=epochs, validation_data=(x_test, y_test))

        # Evaluate Model
        loss, accuracy = self.model.evaluate(x_test, y_test)
        print("Loss:", loss)
        print("Accuracy:", accuracy)

        '''plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Train', 'Test'], loc='upper left')
        plt.show()
        '''




        '''self.model = Sequential([
            Conv2D(filters=30, kernel_size=(3, 3), activation='relu', input_shape=(30, 30, 3)),
            MaxPooling2D((2, 2)),
            Dropout(0.3),
            
            Conv2D(filters=64, kernel_size=(3, 3), activation='relu'),
            MaxPooling2D((2, 2)),
            Dropout(0.3),
            
            Flatten(),
            Dense(256, activation='relu'),
            Dropout(0.5),
            Dense(512, activation='relu'),
            Dropout(0.3),
            Dense(7, activation='softmax')
        ])
        self.model.compile(optimizer='adam',
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        self.model.fit(x_train, y_train, epochs=epochs)

        loss, accuracy = self.model.evaluate(x_test, y_test)
        print("Loss:", loss)
        print("Accuracy:", accuracy)'''

    

    def save(self, path):


        if self.model == False:
            raise OSError("NO DATA TO SAVE! YOU MUST TRAIN OR LOAD A MODEL")
        
        if not str(path).endswith(".keras"):

            raise OSError("YOU MUST SAVE MODEL ON .keras FORMAT")

        if os.path.exists(path):
            os.remove(path)

        save_model(self.model, path)

        if os.path.exists(path):
            print("SUCESSFULL TO SAVE MODEL")



    def load(self, path):

        if not os.path.exists(path):
            raise OSError("THIS FILE DOES'T EXIST")

        self.model = load_model(path)


    def answere(self, path):
        
        try:

            if self.model == False:
                raise OSError("NO DATA TO SAVE! YOU MUST TRAIN OR LOAD A MODEL")

            vData = []
            vData.append(self.imageTools.convertData(path))
            vData = np.array(vData)
            nImage = vData/255
            result =  self.model.predict(nImage)
            return np.argmax(result)
        except:
            return False
    
    

