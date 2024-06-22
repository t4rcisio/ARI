import os.path
import pickle


class StoreManager:



    def datasetStorage_data(self, datasetName, data=False):

        return self.__pickeIO("./dataset/"+datasetName+".pkl", data)

    def __pickeIO(self, path, data=False):


        if not os.path.exists("./dataset"):
            os.mkdir("./dataset")


        if str(data) == "False":

            try:
                return pickle.load(open(path, 'rb'))
            except:
                return None
        else:
            try:
                pickle_storage = open(path, "wb")
                pickle.dump(data, pickle_storage)
                pickle_storage.close()
                return data
            except:
                return None