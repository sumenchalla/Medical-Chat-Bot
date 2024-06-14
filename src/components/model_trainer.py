from sklearn.linear_model import RidgeClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from src.logger import logging
from os.path import join

from src.utils import save_object
from src.utils import evaluate_model
from src.config.configuration import dataingestionconfig




class ModelTrainer:
    def __init__(self):
        self.ingestion = dataingestionconfig()
    def initate_model_training(self,X_train,y_train,X_test,y_test):
        try:
            logging.info('Splitting Dependent and Independent variables from train and test data')

            models={
            'RidgeClassifier':RidgeClassifier(),
            'KNeighborsClassifier':KNeighborsClassifier(),
            'RandomForestClassifier':RandomForestClassifier(),
            'GaussianProcessClassifier':GaussianProcessClassifier(),
            'DecisionTree':DecisionTreeClassifier()
        }
            
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n====================================================================================\n')
            logging.info(f'Model Report : {model_report}')

            # To get best model score from dictionary 
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , Accuracy : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , Accuracy : {best_model_score}')

            save_object(
                 file_path=join(self.ingestion.unzip_path,"model.pkl"),
                 obj=best_model
            )
          

        except Exception as e:
            logging.info('Exception occured at Model Training')
            raise e