import os,zipfile
from urllib import request 
from src.CNN_Classifier import logger
from src.CNN_Classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
from src.CNN_Classifier.utils.common import *

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.data_ingestion_config = config

    def download_file(self):
        header = None  # Initialize header

        if not os.path.exists(self.data_ingestion_config.local_data_path):
            file, header = request.urlretrieve(
                url=self.data_ingestion_config.source_url,
                filename=self.data_ingestion_config.local_data_path
            )
            logger.info(f"{file} Downloaded !!! path {header}")
        else:
            logger.info(f"File is already present at {self.data_ingestion_config.local_data_path}")

    def extract_zip_file(self):
        path = Path(self.data_ingestion_config.local_data_path)
        unzip_path = Path(self.data_ingestion_config.unzip_dir)
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)