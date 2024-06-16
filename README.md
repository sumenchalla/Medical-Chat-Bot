# Medical-Chat-Bot

## Introduction
This is the project that helped me to know what is the importance of attension mechanisam and use case of LLM for chatbots.I already build 3 projects(chat with pdf,voice chatbot,MCQ generator with LLM) using LLM and while creating those projects I never appreciated vector embedding, attension mechanisam or RAG. This project helped to learn all of those things while creating every module manullay to handle all the edge. In this project I dint used any LLM or vecctor database. This is chatbot purely works ML algorithm.


## Dataset

I took the dataset from [kaggle](https://www.kaggle.com/datasets/sushil9/disease-and-their-symptoms). This link will redirect you to the dataset description. I short the data set contains symptoms and respective disease.


## Modeling

I used natural language processing for modeling of this problem. converted all the symptoms into single column and extraing all the symtoms to single list and did some NLP processing like removing stopwords and stemming the words. from that words I made a dictionary which contain unique words in the processed list as keys and then assigned number as value for that keys.By using this dictionary, converted all the symptoms into numercial values and using this numerical values trained all classification models in sklearn and got the best model(Random forest classifer).

## How to intract

Just enter the symptoms that you are feeling currently. This model will predict the possible disease it might be, there nothing to be serious.Its trained on just 400 entries but just once do the chekup for the prescribed disease for safe side.


## working images
![image](https://github.com/sumenchalla/Medical-Chat-Bot/assets/76592358/99f73c18-60e1-41b5-a586-75a244abe5c9)
![image](https://github.com/sumenchalla/ML-AI_basics/assets/76592358/bd9c0a08-b8ac-4f69-bce8-dd71a05264cb)
![image](https://github.com/sumenchalla/ML-AI_basics/assets/76592358/3c7d5c58-1b52-42f7-82f8-bd09418fd46b)
![image](https://github.com/sumenchalla/ML-AI_basics/assets/76592358/f76b1ba6-8d12-40ce-a3ac-5e51bb4d4b65)




