import threading
from threading import Thread
from DownloadThread import DownloadThread
from UnpackingThread import UnpackingThread
from DeletedThread import DeletedThread 





		



class MainThread(Thread):
    
    def __init__(self, filePath, label, version_base, version_new, main_win, fl, file_id):
        Thread.__init__(self)
        self.fl = fl
        self.filePath = filePath
        self.label = label
        self.version_base = version_base
        self.version_new = version_new
        self.main_win = main_win
        self.file_id = file_id
        
    
    def run(self):

        
        list_lock = threading.Lock()


        #удаление папки mods
        
        self.label.setText('Deleted old version\nPlease stand by')
        thread = DeletedThread(self.filePath, list_lock)
        thread.start()
        thread.join()
        
        
        if self.fl == 1:
            
            #скачивание архива
            self.label.setText('Download file\nPlease stand by')
            thread = DownloadThread(self.filePath, list_lock, self.file_id)
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
            
            f = open("version.txt", "w")
            f.write(self.version_base)
            f.close()
        else:
            self.label.setText('Deleted complete')
            f = open("version.txt", "w")
            f.write("0.0.0")
            f.close()
        


