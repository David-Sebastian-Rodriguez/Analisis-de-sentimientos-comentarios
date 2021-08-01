#!pip install google-play-scraper
from  google_play_scraper  import  Sort , reviews 
from pprint import pprint
import json
import random
# funcion que retorna todos los datos de la playstore
def extraer_datos(n,score): # si Score es None selecciona todas las calificaciones

  result , continuation_token  =  reviews ('com.clarocolombia.miclaro' ,
      lang = 'es' , country = 'co' , sort = Sort.NEWEST,
      count = n , filter_score_with = score )
    
  result , _  =  reviews ('com.clarocolombia.miclaro',
                          continuation_token = continuation_token )
  return result

# Funcion que extrae n comntarios y puntuaciones para cada 
# valor para cada una de las 5 puntuaciones por ende
# el numero total de comentarios final es de 5*n
def extraerNumeroData(n):
  data = []
  result = []

  for i in range(1,6):#recorre cada valor de puntuacion del 1 al 5
    result = extraer_datos(n,i)   #extrae n datos de la playstore 
    for res in result: # para cada dato filtra solo comentarios y puntuacion
      aux = {'comentario': res['content'], 'estrellas': res['score']}
      data.append(aux)

  with open('data.json', 'w') as file: #genera un archivo JSON donde guarda los datos
    json.dump(data, file, indent=4,ensure_ascii= False)

  return data #retorna los datos como un arreglo de diccionarios  

#Funcion que extrae datos para entrenamiento del predictor de connotacion
#unicamente trae puntuaciones 1 y 2 como negativas y 4 y 5 como positivas
def extraerTrain(n): 
  result = []
  data = []
  for i in [1,2,4,5]: #itera para puntuaciones positivas y negativas
    result = extraer_datos(n,i)    
    for res in result: #filtra el contenido y puntuacion
      if(res['score']==1 or res['score']==2): #para puntuacion 1 y 2 pone etiqueta negativa (neg)
        aux = {"text":res["content"],"label":'neg'}
        data.append(aux)
      else: #para puntuacion 4 y 5 pone etiqueta positiva (pos)
        aux = {"text":res["content"],"label":'pos'}
        data.append(aux)

  data = random.sample(data, len(data)) #desordena los datos arbitrariamente
  ntrain = round(0.8*len(data)) 
  trainData = data[0:ntrain] #selecciona el 80% para entrenamiento
  validationData = data[ntrain:len(data)] #deja el 20% restante para validacion

  with open('trainData.json', 'w') as file:  #guarda datos de entrenamiento
    json.dump(trainData, file, indent=1,ensure_ascii= False)

  with open('validationData.json', 'w') as file: #guarda datos de validacion
    json.dump(validationData, file, indent=1,ensure_ascii= False)

  return [trainData,validationData] #retorna ambos datos

data = extraerNumeroData(1000)
print(len(data))