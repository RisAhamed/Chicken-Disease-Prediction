from src.CNN_Classifier.utils.common import *
from src.CNN_Classifier.constants import params_file_path,config_file_path
import os
from pathlib import Path
from src.CNN_Classifier.entity.config_entity import  *
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
        
   
    def get_prepare_base_model_config(self)->PrepareBaseModelConfig:
        config = self.config_file.prepare_base_model
        params = self.params_file
        create_directory([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_batch_size=params.BATCH_SIZE,
            params_learning_rate = params.LEARNING_RATE,
            params_classes  =params.CLASSES,
            params_epochs  = params.EPOCHS,
            params_image_size  = params.IMAGE_SIZE,
            params_include_top = params.INCLUDE_TOP,
            params_weights = params.WEIGHTS
        )
        return prepare_base_model_config


    