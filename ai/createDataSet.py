import random
from itools import imagesDataset, storeManager
import numpy as np
import matplotlib.pyplot as plt



class DatasetManager:

    image_resize_length = 50
    image_resize_width = 50
    storeTools = storeManager.StoreManager()

    def create(self, args):

        paths  = args['PATHS'] 
        classes = args['CLASS'] 
        datasetName = args['DATASETNAME']
        mode = args["MODE"]

        x = []
        y = []

        if mode == "APPEND":
            x,y = self.__loadData(datasetName)

        x,y = self.__generate(paths, classes, x, y)
        self.__saveData(datasetName, x,y)

    def __loadData(self,datasetName):
        
        try:
            x = self.storeTools.datasetStorage_data(datasetName=datasetName)['x']
            y = self.storeTools.datasetStorage_data(datasetName=datasetName)['y']
        except:
            x = None
            y = None

        if x == None:
            x = []

        if y == None:
            y = []

        return x, y


    def delete(self, classes):
        pass

    def getData(self, datasetName, value):

        if value > 1:
            raise OSError("VALUE MUST BE LESS THAN 1")
        
        x = np.array(self.storeTools.datasetStorage_data(datasetName=datasetName)["x"])
        y = np.array(self.storeTools.datasetStorage_data(datasetName=datasetName)['y'])

        if len(x) != len(y):
             raise OSError("THE DATABASE IS CORRUPTED. SIZE X != SIZE Y")


        vtrain = int(value*len(x))

        return (x[:vtrain], y[:vtrain]), (x[vtrain:], y[vtrain:])



    def __generate(self, paths, classes, x=[], y=[]):

        imTools = imagesDataset.ImagesDataset()

        trainingData = []

        for index in range(0, len(classes)):

            itemNum = index
            classPath = paths[index]
            classe = classes[index]

            print("\nOPENING FOLDER:" + str(classPath))

            response = imTools.genDataset(itemNum, classPath)
            trainingData += response
            print(len(response), "NEW ITENS FROM", classe)

        print("\n")
        print(len(trainingData), "ITENS ARE READED")

        random.shuffle(trainingData)

        for image_array, label in trainingData:
            x.append(image_array)
            y.append(label)

        #x = np.array(x).reshape(-1, self.image_resize_length, self.image_resize_width, 1)

        return x, y


    def __saveData(self, datasetName,  x, y):

        print("SAVING DATA...")

        self.storeTools.datasetStorage_data(datasetName, {"x": x, "y": y})
        
        print("SAVED")


