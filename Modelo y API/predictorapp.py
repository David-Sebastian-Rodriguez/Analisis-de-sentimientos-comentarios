#!pip install google-play-scraper
#!pip install -U textblob
#!pip install -U scikit-learn
import nltk
nltk.download('punkt')

from  google_play_scraper  import  Sort , reviews 
from pprint import pprint
import json
import random
import string
import nltk
import joblib
import json
import pickle
from textblob.classifiers import NaiveBayesClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#Carga de modelos predictores
estimador_connotacionn = joblib.load('model.pkl')
predictor_estrellas = joblib.load('modelclassifier.pkl')
#Carga el vectorizer
vectorizer = CountVectorizer(decode_error="replace", vocabulary=pickle.load(open('vectorizer.pkl', "rb")))

# funcion que retorna todos los datos de la playstore
def extraer_datos(n,score):# si Score es None selecciona todas las calificaciones

  result , continuation_token  =  reviews (
      'com.clarocolombia.miclaro' ,lang = 'es' , country = 'co' , 
      sort = Sort.NEWEST, count = n , filter_score_with = score )
  
  result , _  =  reviews ('com.clarocolombia.miclaro' ,
                          continuation_token = continuation_token)
  return result

#funcion que extrae determinado numero de datos y selecciona
#unicamente los comentarios y la puntuacion
def extraerNumeroData(n):
  data = []
  result = []
  #Extrae los n datos mas recientes, "None" hace que sean de cualquier puntuacion
  result = extraer_datos(n,None)   
  #Filtra para seleccionar solo los comentarios y la puntuacion 
  for res in result:
    aux = {'comentario': res['content'], 'estrellas': res['score']}
    data.append(aux)
  return data

#se ingresa un comentario y retorna solo su connotacion predicha
def estimadorTextoConnotacion(comentario):
  return estimador_connotacionn.classify(comentario)

#Toma como entrada la data con n valores y retorna los  n comentarios
#y la prediccion de connotacion para cada uno
def estimarConnotacion(texto):
  prediccion = []  
  for tex in texto:
    dic = {}
    dic.setdefault('comentario',tex)
    dic.setdefault('connotacion',estimador_connotacionn.classify(tex))
    prediccion.append(dic)

  return prediccion

#la entrada es el numero de comentarios y la salida es una lista de
#n diccionario cada una con un comentario y su prediccion de connotacion
def connotacion(n):
  return estimarConnotacion(comentarios(extraerNumeroData(n)))

  return prediccion

# filtra solo los comentarios de data
def comentarios(data):
  coment = []
  for dat in data:
    coment.append(dat['comentario'])

  return coment

# genera una predicion de puntuacion de una lista de comentarios
def prediccionEstrellas(comentarios):

  comentarios_X = vectorizer.transform(comentarios)
  predicciones = predictor_estrellas.predict(comentarios_X)
  return predicciones.tolist()

#Genera la prediccion de puntuacion de los primeros n comentarios
def estrellasPrimerosComentarios(n):
  prediccion = prediccionEstrellas(comentarios(extraerNumeroData(n)))
  coment = comentarios(extraerNumeroData(n))
  result = []
  for i in range(0,len(coment)):
    dic = {}
    dic.setdefault('comentario',coment[i])
    dic.setdefault('Prediccion',prediccion[i])
    result.append(dic)

  return result