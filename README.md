# Predictor de connotacion y puntuacion API
Algoritmo que extrae los comentarios de una app de Google Play, y basado en ellos, entrena a un modelo para que logre estimar la connotación positiva o negativa de un comentario de entrada, y otro el cual estime la calificación que recibiría.

Además, se implementa una API en Heroku, que permite obtener n comentarios de esta app y su respectiva predicción de connotación, también se puede obtener la connotación y puntuación de un comentario que el usuario ingrese.

## Como acceder la API

El link para acceder a la API es:

[https://app-predictor-connotacion.herokuapp.com/](http://app-predictor-connotacion.herokuapp.com/ "https://app-predictor-connotacion.herokuapp.com/")

Al entrar por primera vez es posible que la página tarde en cargar. Para acceder a n comentarios con sus respectivas predicciones de connotación, añada "connotación-n-valores/5", puede reemplazar "5" por el número de valores que desee obtener.

[https://app-predictor-connotacion.herokuapp.com/connotacion-n-valores/5](http://app-predictor-connotacion.herokuapp.com/connotacion-n-valores/5 "https://app-predictor-connotacion.herokuapp.com/connotacion-n-valores/5")

Para ingresar un comentario y obtener la prediccion de su connotacion y calificaion, acceda al siguiente link: 
[https://app-predictor-connotacion.herokuapp.com/connotacion-y-calificacion](http://app-predictor-connotacion.herokuapp.com/connotacion-y-calificacion "https://app-predictor-connotacion.herokuapp.com/connotacion-y-calificacion"), en el, posteriormente se cargaran los datos del comentario y las predicciones. 
Además, ingrese al link: 
[https://app-predictor-connotacion.herokuapp.com/docs](http://app-predictor-connotacion.herokuapp.com/docs "https://app-predictor-connotacion.herokuapp.com/docs"), allí cargara una interface donde podra ingresar el comentario a predecir. 
Acceda a la sección "post", luego "Try it out", y en la sub-sección "post" ingrese el comentario. Finalmente oprima "Execute" y recargue el primer link para ver el resultado.

![img](https://raw.githubusercontent.com/David-Sebastian-Rodriguez/Predictor-de-connotacion-y-puntuacion-API/main/Imagenes/1.png)


## Explicación de archivos
En la carpeta `Extraer datos y entrenamiento`, se encuentran 3 archivos .py, `extraer_datos.py` extrae los comentarios y puntuación para el entrenamiento de los archivos, con el se generaron, `data.json`, `trainData.json`, `validationData.json`.
`entrenador_estimador_de_connotacion.py` entrena el modelo del estimador de connotacion utilizando un NaiveBayesClassifier y lo extrae en `model.pkl`.
`entrenador_predictor_estrellas.py` entrena el predictor de calificación y lo extrae en `modelclassifier.pkl` y su vectorizador en `vectorizer.pkl`.
En la carpeta `Modelo y API` se guardan los modelos, y los archivos para la API. `predictorapp.py` tiene las funciones para utilizar los predictores, `app.py` implementa fastAPI para manejar la API, los demás archivos son los modelos y archivos necesarios para subir el modelo a Heroku.

