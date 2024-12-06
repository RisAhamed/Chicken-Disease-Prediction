from src.CNN_Classifier.config.configuration import ConfigurationManager
from src.CNN_Classifier.components.data_ingestion import DataIngestion
from src.CNN_Classifier import logger

stage_name = 'Data Ingestion Pipeline'

class DataIngestionTrainingPipeline:


    def __init__(self) -> None:
        pass 
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config  =config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        logger.info(f"{data_ingestion} completed,Downloading files")
        data_ingestion.download_file()
        logger.info(f"file downloading completed,extracting files")

        data_ingestion.extract_zip_file()

    