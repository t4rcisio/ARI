

from itools import imageDownloader
from utils import storeManager, tools
import os

class AI_routes:

    imDownloader = imageDownloader.ImagesDownloader()
    storeManager = storeManager.StoreManager()
    tools = tools.Tools()

    def downloadImages(self, queue):

        zmax = len(queue)

        counter = 1
        for item in queue:

            message = "DOWNLOADING " + str(queue[item]["C_NAME"]) + " | " + str(counter) + "/" + str(zmax)
            self.storeManager.msgBroadcast(message)
            
            data = queue[item]["ARGS"]
            output = data["FOLDER_INPUT"]
            search = str(data['WEB_INPUT']).split(",")
            maxDownload = int(data['WEB_MAXD'])

            res = self.imDownloader.run(output, search, maxDownload)
            counter +=1


    def clearFolder(self, path):

        queue = os.listdir(path)
        zmax = len(queue)

        counter = 1
        for item in queue:

            message = "CLEANING FOLDER " + str(os.path.basename(path)) + " | " + str(counter) + "/" + str(zmax)
            self.storeManager.msgBroadcast(message)

            file = path + "/" + item
            self.tools.deleteItem(file)
            counter +=1
    
    def createDataset(self, args):

        pass