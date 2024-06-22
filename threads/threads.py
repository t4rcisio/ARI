import time
from PyQt6.QtCore import QObject, QThread, pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from threading import Thread


from utils import storeManager
from scripts import imageDownloader
from ai import createDataSet


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    broadcast = storeManager.StoreManager()

    def run(self):

        
        args = self.broadcast.args()

        if args["OP"] == "IMAGE DOWNLOADER":

            self.application = imageDownloader.AI_routes()

            self.app = Thread(target=self.application.downloadImages, args=(args["ARGS"],))
            self.app.start()

        if args["OP"] == "CLEAR FOLDER":

            self.application = imageDownloader.AI_routes()

            self.app = Thread(target=self.application.clearFolder, args=(args["ARGS"],))
            self.app.start()


        if args["OP"] == "GENERATE DATASET":

            self.application = createDataSet.DatasetManager()

            self.app = Thread(target=self.application.create, args=(args["ARGS"],))
            self.app.start()

        else:
            self.progress.emit(1)
            self.finished.emit()
            return

        while (self.app.is_alive()):

            time.sleep(1)
            self.progress.emit(1)

        self.progress.emit(1)
        self.finished.emit()


class ThreadService(QMainWindow):

    broadcast = storeManager.StoreManager()
    cache = "WAITING DATA"

    def acabou(self):
        self.endApp()

    def runUpdate(self):
       
       self.progress()

    def run(self, beginApp, endApp, progress ):
        # Step 2: Create a QThread object
        self.thread = QThread()

        self.beginApp = beginApp
        self.endApp = endApp

        self.progress = progress

        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        
     
        self.worker.progress.connect(self.progress)


        # Step 6: Start the thread
        self.beginApp()
        self.thread.start()

        self.thread.finished.connect(self.acabou)