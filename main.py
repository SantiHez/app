#Importo Librerias
from firebase_admin import credentials
from firebase_admin import firestore
from faker import Faker
import firebase_admin
import random

#Inicializo Firebase
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

#Inicializo Faker
fake = Faker()

#Genero de Peliculas
genero = ['Accion', 'Aventura', 'Comedia', 'Drama', 'Fantasia', 'Terror', 'Romance', 'Ciencia Ficcion', 'Musical', 'Documental', 'Animacion', 'Crimen', 'Misterio', 'Biografia', 'Guerra', 'Historia', 'Familia', 'Deporte', 'Western', 'Thriller']

#Longitud de Genero
lengenero = len(genero)

#Diccionario de Peliculas
pelicula = {
    "Titulo":"",
    "FechaEstreno":"",
    "Actores":"",
    "Categoria":"",
    "Descripcion":"",
    "DuracionMinutos":"",
    "Puntuacion":""
}

#Ciclo para agregar Peliculas
for i in range(1,50):
    pelicula["Titulo"] = "Pelicula " + str(i)
    pelicula["FechaEstreno"] = str(fake.date())
    pelicula["Actores"] = str(fake.name())
    pelicula["Categoria"] = str(genero[random.randint(0, lengenero-1)])
    pelicula["Descripcion"] = "Descripcion " + str(i)
    pelicula["DuracionMinutos"] = random.randint(60, 180)
    pelicula["Puntuacion"] = random.randint(1, 5)
    print(pelicula)
    db.collection("Peliculas").add(pelicula)