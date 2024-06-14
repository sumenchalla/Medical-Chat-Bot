import pandas as pd
import numpy as np
from src.logger import logging
from sklearn.model_selection import train_test_split
import sys,os
from src.config.configuration import DataTransformationconfig,dataingestionconfig
from os.path import join
import ast


class DataTransformation:
    def __init__(self):
        self.config = DataTransformationconfig()
        self.injection = dataingestionconfig()

    def initiate_datatransformation(self):
        logging.info("Features gropuing for processing is initited")

        try:
            df = pd.read_csv(join(self.injection.unzip_path,"dataset.csv"),on_bad_lines="skip")

            #merging all the symptoms into one column which contains all the symptoms
            df['symptoms'] = df.apply(lambda row: ' '.join(row.iloc[1:].values.astype(str)), axis=1)

            #removing nan values and splitting to convert it into numerical category
            for i in range(len(list(df["symptoms"]))):
                df["symptoms"][i]=str(df["symptoms"][i]).replace(" nan","")
                df["symptoms"][i]=str(df["symptoms"][i]).split()
            
            logging.info("Feature grouping is done")
            

            #trying to add all the words in symptoms into single list
            Tokens=[]
            for i in df["symptoms"]:
                Tokens.append(i)

            total_words=[]
            for i in Tokens:
                for j in i:
                    total_words.append(j)

                
            #converting the symptoms into numerical 
            word_dict={}
            j=1
            for i in total_words:
                if i not in word_dict.keys():
                    word_dict[i]=j
                    j+=1

            logging.info("Initiated to converstion of symptomps into numerical features")
            
            df["features"]= None
            for i,lst in enumerate(df["symptoms"]):
                features=[] 
                for j in lst:
                    features.append(word_dict[j])
                df["features"][i] = features

            logging.info("converstion of symptomps into numerical features is done")

            # adding padding
            for i in range(len(list(df["features"]))):
                lst = list(df["features"])[i]
                for j in range((17-len(lst))):
                    lst.append(0)
                df["features"][i] = lst

            logging.info("Padding done succesfully")

            Xtrain= df["features"][:3000].tolist()
            Ytrain = df["Disease"][:3000].tolist()
            Xtest= df["features"][3000:].tolist()
            Ytest = df["Disease"][3000:].tolist()

            

        except Exception as e:
            logging.info("Error occured while data transformation")
            raise e
        
        return Xtrain,Ytrain,Xtest,Ytest
