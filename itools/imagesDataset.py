import os.path
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from rembg import remove
import numpy as np
from utils import storeManager


class ImagesDataset:
    

    image_w = 30
    image_h = 30

    storeManager = storeManager.StoreManager()

    def genDataset(self, classNum, path):

        imagesList = os.listdir(path)

        training_data = []
        counter = 1
        for item in imagesList:
            imagePath = path + "/" + item

            msg = "READING IMGES | " + str(item) + " | " + str(counter) + "/" + str(len(imagesList))
            self.storeManager.msgBroadcast(msg)

            try:

                if self.__checkIsImage(imagePath):
                    recized_array = self.convertData(imagePath)
                    training_data.append([recized_array, classNum])
            except:
                    
                print("AN ERROR OCURRED WHILE PROCCESSING IMAGE: "+str(item) + " FROM CLASS: " + str(classNum))

            counter +=1

        return training_data



    def convertData(self, imagePath):

        if self.__checkIsImage(imagePath):

            #image_array = cv2.imread(imagePath)
            image_array = self.__removeBackground(imagePath)
            recized_array = cv2.resize(image_array, (self.image_h,self.image_w))
            return recized_array
        else:
            return None
        

    def __removeBackground(self, path):

        input_image = Image.open(path)
        output_image = remove(input_image)
        output_array = np.array(output_image)
        return output_array
        

    def __checkIsImage(self, file_path):

        try:
            img = Image.open(file_path)
            img.close()
            return True
        except:
            return False
