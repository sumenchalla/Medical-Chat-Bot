from src.logger import logging
from src.config.configuration import dataingestionconfig
import zipfile
import os
import urllib.request
import pandas as pd
from sklearn.model_selection import train_test_split
from os import listdir
from os.path import isfile, join


class DataIngestion:
    def __init__(self):
        self.congif = dataingestionconfig()
    
    def download_file(self):
        try:
            dataset_url = self.congif.source_url
            zip_download_dir = self.congif.download_path
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
            with zipfile.ZipFile(self.congif.download_path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)


        except Exception as e:
            logging.info(f"Error occured while extracting file from {self.congif.download_path}")
            raise e
        
    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')
        data_path = self.congif.unzip_path

        try:
            df = pd.read_csv(join(data_path,"dataset.csv"), on_bad_lines='skip')   #for every different project we have to change this
            logging.info("Data was sucessfully read as Pandas DataFrame")
            train_data, test_data = train_test_split(df,test_size=0.2,random_state=17)
            logging.info("Data set is sucessfully divided into train and test sets")

            train_data.to_csv(join(self.congif.unzip_path,"train.csv"),index=False,header=True)
            test_data.to_csv(join(self.congif.unzip_path,"test.csv"),index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                join(self.congif.unzip_path,"train.csv"),
                join(self.congif.unzip_path,"test.csv")

            )
        except Exception as e:
            logging.info("Error occured during the data ingestion")
            raise e