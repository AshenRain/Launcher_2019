import os
import urllib.request
import zipfile
from threading import Thread


class UnpackingThread(Thread):
    
    def __init__(self, filePath, list_lock):
        """Инициализация потока"""
        Thread.__init__(self)
        self.list_lock = list_lock
        self.filePath = filePath
    
    def run(self):
        """Запуск потока"""
        print('Unpacking')
        self.list_lock.acquire(1)
        fantasy_zip = zipfile.ZipFile(self.filePath + '\\SCLegacy.zip')
        fantasy_zip.extractall(self.filePath[:-33])
        fantasy_zip.close() 
        self.list_lock.release()

