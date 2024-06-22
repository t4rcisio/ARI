import pickle
import rsa
import os
import jwt
from utils import tools
import traceback

class StoreManager:


    def __init__(self, TOKEN=None):
        
        self.jwToken = "71eb5709088a7f8e583c4835a7face4b"
        self.rootPath = "C:/ARI.IA"
        self.tools = tools.Tools()

        self.PATH = {
            "HOME": self.rootPath,
            "TEMP": self.rootPath + "/temp",
            "MODELS": self.rootPath + "/models", 
        }

        [self.tools.createFolder(self.PATH[folder]) for folder in self.PATH]

        self.__loadKeys()
        


    def broadcast(self, path, data=False):

        return self.__dataManager(path, data)
    

    def tempConfig(self, data=False):

        return self.__dataManager(self.PATH["TEMP"]+"/temp.config", data)
    

    def args(self, data=False):

        return self.__dataManager(self.PATH["TEMP"]+"/args.config", data)
    
    def msgBroadcast(self, data=False):

        return self.__dataManager(self.PATH["TEMP"]+"/msgBroadcast.reg", data)
    
    def alertTrigger(self, data=False):

        return self.__dataManager(self.PATH["TEMP"]+"/alertTrigger.config", data)

    def modelParams(self, data=False):

        return self.__dataManager(self.PATH["TEMP"]+"/moedelParams.config", data)



    def __loadKeys(self, pub_Key=False, priv_key=False):

        self.privateKey = False
        self.publicKey  = False

        if pub_Key == False or priv_key==False:
            
            if os.path.exists(self.PATH["HOME"]+"/.env"):
                try:
                    dataFile = self.__jwDecode(open(self.PATH["HOME"]+"/.env", "r", encoding="UTF-8").read())["payload"]
                    self.publicKey = rsa.PublicKey.load_pkcs1(dataFile)
                    self.privateKey = rsa.PrivateKey.load_pkcs1(dataFile)
                except:
                    self.privateKey = False
                    self.publicKey  = False
        else:
                
            self.privateKey = priv_key
            self.publicKey  = pub_Key
        
        if not self.privateKey or not self.publicKey:

                self.publicKey, self.privateKey = rsa.newkeys(2048)
                data = self.__jwEncode(self.publicKey.save_pkcs1().decode('utf-8') + "\n" + self.privateKey.save_pkcs1().decode('utf-8'))
                open(self.PATH["HOME"]+"/.env", "w", encoding="UTF-8").write(data)


    def __encript(self, data):

        obj = pickle.dumps(data)
        return rsa.encrypt(obj, self.publicKey)

    def __decrypt(self, data):

        return rsa.decrypt(data.encode('latin1'), self.privateKey)
    

    def __jwEncode(self, data):

        return jwt.encode({"payload": data}, self.jwToken, algorithm="HS512")
    
    def __jwDecode(self, data):
        return jwt.decode(data, self.jwToken, algorithms=["HS512"])
    

    def __dataManager(self, path, data=False):

        try:
            
            if data == False:

                encoded = open(path, "r", encoding="UTF-8").read()
                jwData = self.__jwDecode(encoded)
                return jwData["payload"] #obj =  self.__decrypt(jwData["payload"])
                #return pickle.loads(obj)
            
            else:

                rdata = data #rdata = self.__encript(data).decode('latin1')
                paylaod = self.__jwEncode(rdata)
                open(path, "w", encoding="UTF-8").write(paylaod)
        except:
            print("An error ocurred on\n"+ traceback.format_exc())
            return None