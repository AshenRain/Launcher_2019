import threading
from threading import Thread
from DownloadThread import DownloadThread
from UnpackingThread import UnpackingThread
from DeletedThread import DeletedThread 





		



class MainThread(Thread):
    
    def __init__(self, filePath, label, version_base, version_new, main_win):
        Thread.__init__(self)
        self.filePath = filePath
        self.label = label
        self.version_base = version_base
        self.version_new = version_new
        self.main_win = main_win
        
    
    def run(self):

        
        list_lock = threading.Lock()

        #удаление папки mods
        self.label.setText('Deleted old version\nPlease stand by')
        thread = DeletedThread(self.filePath, list_lock)
        thread.start()
        thread.join()

        #скачивание архива
        self.label.setText('Download file\nPlease stand by')
        thread = DownloadThread(self.filePath, list_lock)
        thread.start()
        thread.join()

        #разархивирование
        self.label.setText('Unpacking\nPlease stand by')
        thread = UnpackingThread(self.filePath, list_lock)
        thread.start()
        thread.join()
        self.label.setText('Update complete')
        self.version_base = self.version_new
        self.main_win.setText(self.version_base)

