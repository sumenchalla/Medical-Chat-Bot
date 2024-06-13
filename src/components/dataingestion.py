from src.logger import logging
from src.config.configuration import dataingestionconfig
import zipfile
import os
import urllib.request


class DataIngestion:
    def __init__(self,config:dataingestionconfig):
        self.congif = config
    
    def download_file(self):
        try:
            dataset_url = self.congif.source_url
            zip_download_dir = self.congif.unzip_path
            os.makedirs(os.path.dirname(zip_download_dir), exist_ok=True)
            logging.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            urllib.request.urlretrieve(dataset_url, zip_download_dir)

        except Exception as e:
            logging.info(f"Error occured during downloading from {dataset_url}")
            raise e
        
    def unzip_file(self):
        try:
            unzip_path = self.congif.unzip_path
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)


        except Exception as e:
            logging.info(f"Error occured while extracting file from {self.congif.download_path}")
            raise e