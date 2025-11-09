from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline
# from src.textSummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerTrainingPipeline
# from src.textSummarizer.pipeline.stage_4_model_evaluation_pipeline import ModelEvaluationTrainingPipeline


# -------------------------------------------------------------------------
# 🧩 Stage 1: Data Ingestion
# -------------------------------------------------------------------------
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} initiated <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


# -------------------------------------------------------------------------
# 🧩 Stage 2: Data Transformation
# -------------------------------------------------------------------------
STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} initiated <<<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


'''
# -------------------------------------------------------------------------
# 🧩 Stage 3: Model Training
# -------------------------------------------------------------------------
STAGE_NAME = "Model Trainer Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} initiated <<<<<<")
    model_trainer_pipeline = ModelTrainerTrainingPipeline()
    model_trainer_pipeline.initiate_model_trainer()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e


# -------------------------------------------------------------------------
# 🧩 Stage 4: Model Evaluation
# -------------------------------------------------------------------------
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} initiated <<<<<<")
    model_evaluation_pipeline = ModelEvaluationTrainingPipeline()
    model_evaluation_pipeline.initiate_model_evaluation()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")
except Exception as e:
    logger.exception(e)
    raise e
'''
