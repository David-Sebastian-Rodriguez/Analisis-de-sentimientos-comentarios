import pandas as pd
import numpy as np
import json
import random
import string
import joblib
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
#Carga los datos de entrenamiento
with open('data.json') as dat:
  data = json.load(dat)

#mezcla los datos 
data = random.sample(data, len(data))

#organiza los datos
texto = []
estrellas = []
for dato in data:
  texto.append(dato['comentario'])
  estrellas.append(dato['estrellas'])

datos = {'estrellas': estrellas,'comentarios': texto}


#utiliza pandas para poner los datos en
#el formato adecuado para entrenar el modelo
df = pd.DataFrame(datos)
df.columns = ["label", "text"]

#Funcion utilizada para hacer una tokenizacion simple
punctuation = set(string.punctuation)

def tokenize(sentence):
    tokens = []
    for token in sentence.split():
        new_token = []
        for character in token:
            if character not in punctuation:
                new_token.append(character.lower())
        if new_token:
            tokens.append("".join(new_token))
    return tokens

#se dividen los datos en entrenamiento y prueba
train_text,test_text, train_labels, test_labels = train_test_split(df["text"], df["label"], stratify=df["label"])

#se modifica el vectorizador por defecto por el que se creo anteriormente                                          
vectorizer = CountVectorizer(tokenizer = tokenize, binary=True)
#se vectorizan los datos
train_X = vectorizer.fit_transform(train_text)
test_X = vectorizer.transform(test_text)
train_X.shape

#Se selecciona el modelo y se entrena
classifier = LinearSVC()
classifier.fit(train_X, train_labels)

#se prueba el desempeño del modelo
predicciones = classifier.predict(test_X)

accuracy = accuracy_score(test_labels, predicciones)

print(f"Accuracy: {accuracy:.4%}")

#se guarda el modelo y el vectorizador

joblib.dump(classifier,'modelclassifier.pkl')

with open('vectorizer.pkl', 'wb') as fw:
     pickle.dump(vectorizer.vocabulary_, fw)