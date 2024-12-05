import os
import urllib.request as request
import zipfile
from src.CNN_Classifier import logger
from src.CNN_Classifier.utils.common import *
from src.CNN_Classifier.entity.config_entity import DataingestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config: DataingestionConfig):
        self.config = config
    def download_file(self):
        if not os.path.exists(self.config.local_data_path) :
            file_name,header = request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_path
            )
            logger.info(f"Downloaded file: {file_name}")
        else:
            logger.info(f"File already exists at location: {self.config.local_data_path}")

    
    def extract_zip(self):
        try:
            path = Path(self.config.local_data_path)
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok= True)

            with zipfile.ZipFile(path, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
                logger.info(f"Extracted zip file at location: {unzip_path}")
        
        except Exception as e:
            logger.error(f"An error occurred: {e}")