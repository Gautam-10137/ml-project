import os
import sys   # to handle exception
from src.exception import CustomException   #to handle custom exception
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  # to make class variables     -- is in python 3.9 & above

from src.component.data_transformation import DataTransformation
from src.component.data_transformation import DataTransformationConfig

from src.component.model_trainer import ModelTrainerConfig
from src.component.model_trainer import ModelTrainer

@dataclass    # using dataclass as decorator with  DataIngestionConfig
class DataIngestionConfig:   # to maintain inputs of modules we will call here
    # inputs like in which file I have to save the output
    train_data_path: str=os.path.join('artifacts',"train.csv")   # class variable    will act as input for data ingestion components
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"raw.csv")   

# use dataclass only when you class variable , but if you also have functions then you  define __init__ in place of dataclass
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()  # all 3 class variable come inside it.
    def initiate_data_ingestion(self): # here we define how we'll read data wheteher localy or from mongoDB, etc. 
                                       # will call function we defined in utils to get data from database
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")

            # making directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )            
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":    # to execute it when we run it
    obj=DataIngestion()
    train_path,test_path=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_path,test_path)

    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))



