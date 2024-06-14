from src.components.dataingestion import DataIngestion
from src.components.datatransformation import DataTransformation
from src.components.model_trainer import ModelTrainer


if __name__ == "__main__":
    ingestion = DataIngestion()
    #As i have the downloaded file I'm directly unzip actually we have to download zip file then unzip it
    ingestion.unzip_file()

    transformation = DataTransformation()

    #initiating data transformation i,e getting xtrain,ytrain,xtest,ytest
    xtrain,ytrain,xtest,ytest=transformation.initiate_datatransformation()

    #Initiating data ingestion
    train_data,test_data=ingestion.initiate_data_ingestion()
    


    #training the model
    trainer = ModelTrainer()

    trainer.initate_model_training(xtrain,ytrain,xtest,ytest)