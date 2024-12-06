from src.CNN_Classifier.utils.common import *
from src.CNN_Classifier.constants import params_file_path,config_file_path
import os
from box.exceptions import BoxValueError
from pathlib import Path
from src.CNN_Classifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self,
                 config_file_path = config_file_path,
                 params_file_path = params_file_path):
        
        self.config_file = read_yaml(config_file_path)
        self.params_file = read_yaml(params_file_path)

        create_directory([self.config_file.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try: 
            config  = self.config_file.data_ingestion
            create_directory([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir = config.root_dir,
                source_url= config.source_url,
                local_data_path= config.local_data_path,
                unzip_dir = config.unzip_dir
            )

            return data_ingestion_config
        except Exception as e:
            raise e
        except BoxValueError as e:
            raise e
    