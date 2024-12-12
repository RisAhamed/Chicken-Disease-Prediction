from src.CNN_Classifier import logger
from src.CNN_Classifier.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.CNN_Classifier.pipeline.base_model_pipeline import PrepareBaseModelTrainingPipeline


STAGE_NAME  = "Data Ingestion Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e



stage_name = 'Base  Model Preparation'

if __name__ =='__main__':
    try:
        logger.info(f">>>>>> stage {stage_name} started <<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========")
    
    except Exception as e:
        logger.exception(e)
        raise e
    
        