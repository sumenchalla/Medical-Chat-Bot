from src.drug import drugs
from src.utils import load_object
from src.config.configuration import ModelTraningconfig
from src.config.configuration import dataingestionconfig
import json
from os.path import join
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re
from nltk.stem import PorterStemmer
nltk.download('punkt')
stopword = stopwords.words('english')

stemmer = PorterStemmer()

maxlen = 28 #founded that max number of features are 28, saving this number for padding of data



class prediction_pipeline:
    def __init__(self,input:str):
        self.input =  input
        self.model_config = ModelTraningconfig()
        self.ingestion = dataingestionconfig()

    def predict(self,features):
        model = load_object(join(self.ingestion.unzip_path,"model.pkl"))
        output=model.predict([features])
        return output
    

    def input_data_transformation(self):
        with open(join(self.ingestion.unzip_path,"word_vec.json"),"r") as file:
            word_vec = json.load(file)

        input_data = self.input.lower()
        only_alpha = re.sub(r'[^a-zA-Z]', ' ', input_data)
        split_text = re.split(r'[ ,_:.]+', only_alpha)
        cleaned_data =[i for i in split_text if i not in stopword]
        cleaned_data =[stemmer.stem(word) for word in cleaned_data]
        data=[]
        for word in cleaned_data:
            if word not in data:
                data.append(word)
        data = sorted(data)
        feature_count = 0

        features=[]
        for i in data:
            if i in word_vec.keys() and feature_count<28 and word_vec[i] not in features:
                features.append(word_vec[i])
                feature_count+=1


        for i in range(28-len(features)):
            features.append(0)

        return features,data


        

    def disease_output(self):
        features,clean =  self.input_data_transformation()
        disease = self.predict(features)

        return f"These are the symptoms of {disease[0]}, we have listed some basic medication for {disease[0]}. Do you want to have a look at them"
    
    def medication_output(self):
        features,clean =  self.input_data_transformation()
        disease = self.predict(features)

        return drugs[disease[0]]