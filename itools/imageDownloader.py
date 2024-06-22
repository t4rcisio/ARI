import os.path
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import  By
from io import BytesIO
from PIL import Image
import base64
import hashlib
from utils import storeManager

class ImagesDownloader:

    storeManager = storeManager.StoreManager()
    minwidth = 16
    minHeight = 16

    def run(self, dirPath, googleSearch, maxDownload, res=False):


        self.__startEngine()

        for item in googleSearch:

            self.search(item)
            self.__downloadImages(item, dirPath, int(maxDownload/len(googleSearch)))

        self.driver.close()


    def __downloadImages(self, item, outputDir, maxDownload):


        counter = 0
        contentMap = {}
        cdownloader = 0
        cdownloader2 = 0

        while counter <= maxDownload:

            self.storeManager.msgBroadcast("DOWNLOADING: " + str(item) + " | " + str(counter) + " of " + str(maxDownload))

            imagesURL = self.driver.find_elements(By.TAG_NAME, 'img')

            for index in range(0, len(imagesURL[2:])):

                content = imagesURL[index].get_attribute("src")
                if str(content).startswith("data:image"):

                    header = str(content).split(",")
                    base64_content = str(content).split(",")[-1]
                    image_data = base64.b64decode(base64_content)

                    image = Image.open(BytesIO(image_data))
                    width, height = image.size

                    if width > self.minwidth and height > self.minHeight and not str(base64_content) in contentMap:


                        fileName = self.__filename(content) + "_.jpg"
                        path = outputDir + "\\" + fileName

                        if not os.path.exists(path):

                            with open(path, "wb") as f:
                                f.write(image_data)

                            counter +=1
                            contentMap[str(base64_content)] = base64_content

                            print("DOWNLOADING:" + str(fileName) + "\n" + str(counter) + " of " + str(maxDownload))
                            cdownloader +=1
                            cdownloader2 = 0


                    if counter > maxDownload:
                        return
                    
                elif str(content).startswith("http") and not 'google.com' in content:

                    height = int(imagesURL[index].get_attribute("height"))
                    width = int(imagesURL[index].get_attribute("width"))

                    if width > self.minwidth and height > self.minHeight and not str(content) in contentMap:

                        
                        fileName = self.__filename(content) + "_.jpg"
                        path = outputDir + "\\" + fileName

                        if not os.path.exists(path):

                            response = requests.get(content)
                            if response.status_code == 200:

                                with open(path, 'wb') as f:
                                    f.write(response.content)

                                counter += 1
                                contentMap[str(content)] = content

                                print("DOWNLOADING:" + str(fileName) + "\n" + str(counter) + " de " + str(maxDownload))
                                cdownloader +=1
                                cdownloader2 = 0

                    if counter > maxDownload:
                        return

            if cdownloader == 0:
                cdownloader2 +=1

            if cdownloader2 > 2:
                return

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            cdownloader = 0

    def __startEngine(self):

        self.driver = webdriver.Chrome()

    def search(self, imageClass):

        self.driver.get(self.__urlMaker(imageClass))

    def __urlMaker(self, query):
        base_url = "https://www.google.com/search"
        params = {
            "tbm": "isch",  # tbm parameter specifies image search
            "q": query  # q parameter specifies the search query
        }
        query_string = "&".join([f"{key}={value}" for key, value in params.items()])
        search_url = f"{base_url}?{query_string}"
        return search_url
    
    def __filename(self, content, maxl = 20):

        sha256 = hashlib.sha256()

        sha256.update(content.encode())

        hash_code = sha256.hexdigest()

        truncated_hash = hash_code[:20]

        return str(truncated_hash)