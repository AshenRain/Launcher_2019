import os
import urllib.request
import requests
from threading import Thread


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)


 
class DownloadThread(Thread):
    """
    Пример скачивание файла используя многопоточность
    """
    
    def __init__(self, filePath, list_lock):
        """Инициализация потока"""
        Thread.__init__(self)
        self.list_lock = list_lock
        self.filePath = filePath
    
    def run(self):
        """Запуск потока"""
        print('Download file')
        self.list_lock.acquire(1)
        file_id = '1J_h1W_ogDElBuU_OZKVQ6RdntchxIKN2'
        destination = self.filePath + '\\SCLegacy.zip'
        download_file_from_google_drive(file_id, destination)  
        msg = " закончил загрузку !" 
        print(msg)
        self.list_lock.release()



