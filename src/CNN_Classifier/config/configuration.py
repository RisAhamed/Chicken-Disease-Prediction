from src.CNN_Classifier.constants import *
import os
from pathlib import Path
from src.CNN_Classifier.utils.common import *
from src.CNN_Classifier.entity.config_entity import *

class ConfigurationManager:
    def __init__(self,
                 config_file_path=config_file_path,
                 params_file_path = params_file_path):
        self.config_file_path = read_yaml(config_file_path)
        self.params_file_path = read_yaml(params_file_path)
        create_directory([self.config_file_path.artifacts_root])

    def get_data_ingestion_config(self)->DataingestionConfig:
        config = self.config_file_path.data_ingestion

        create_directory([config.root_dir])

        data_ingestion_config = DataingestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_path = config.local_data_path,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config