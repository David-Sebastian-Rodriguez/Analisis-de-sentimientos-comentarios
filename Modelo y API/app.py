from fastapi import FastAPI
import predictorapp as pred

app = FastAPI()

clasificacion = ['']


@app.get('/')
def read_root():
  return {"API predictora de connotación de comentarios y calificación"}

@app.get('/connotacion-n-valores/{n}')
def get_connotacion_n_valores(n: int):
  salida = pred.connotacion(n)
  print(salida)
  print(type(salida))
  return salida

@app.get('/connotacion-y-calificacion')
def get_posts():
  return clasificacion

@app.post('/connotacion-y-calificacion')
def prediccion_connotacion_y_calificacion(post):  
  clasificacion[0] = ({'texto':post,
      'prediccion_puntuacion': pred.prediccionEstrellas([post])[-1],
      'prediccion_connotacion': pred.estimadorTextoConnotacion(post)}) 
  return "Hecho"
  
