import os
import urllib.request
import shutil
from threading import Thread



class DeletedThread(Thread):
    
    def __init__(self, filePath, list_lock):
        """Инициализация потока"""
        Thread.__init__(self)
        self.list_lock = list_lock
        self.filePath = filePath
    
    def run(self):
        """Запуск потока"""
        print('Deleted old version')
        self.list_lock.acquire(1)
       	try:
        	directory_exe = self.filePath + '\\mods'
        	print(directory_exe)
        	path = os.path.join(os.path.abspath(os.path.dirname(__file__)), directory_exe)
        	shutil.rmtree(path)
        except IOError:
        	print("delete error")
        try:
            directory_exe = self.filePath + 'SCLegacy.zip'
            print(directory_exe)
            path = os.path.join(os.path.abspath(os.path.dirname(__file__)), directory_exe)
            shutil.rmtree(path)
        except IOError:
            print("delete arh error")
        self.list_lock.release()