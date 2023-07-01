import pyodbc
import os
from dotenv import load_dotenv
load_dotenv()
import requests
from typing import NamedTuple



def get_rating(id: str):
    ApiKey = os.getenv('IMDB_KEY')
    #ApiKey = 'k_r6c0kpae'
    id = id.zfill(7)
    api_url = f"https://imdb-api.com/API/Ratings/{ApiKey}/tt{id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        imdbRating = float(response.json()['imDb'])
        return imdbRating

    else:
        return 'No hay rating'



def getPoster(id: str):

    """Funcion que devuelve el Poster de una pelicula
    :param id str:  id de la pelicula de la que mostrar el poster
    :return: link  a de la imagen"""
  
    #ApiKey = 'k_r6c0kpae'

    ApiKey = os.getenv('IMDB_KEY')
    id = id.zfill(7)
    api_url = f"https://imdb-api.com/en/API/Posters/{ApiKey}/tt{id}"

    response = requests.get(api_url)
    if response.status_code == 200:

        if len(response.json()['posters']) > 0:
            poster = response.json()['posters'][0]['link']

            return poster

        else:
            result = 'No hay poster disponible'

            return result








class dataReturn():

    def __init__(self):
        self.rating = 0
        self.genre = None
        self.poster = ""
        self.title = ''
        self.cursor = None
        self.connect_to_database()


    def connect_to_database(self):
        try:
            self.conection = pyodbc.connect("CONNECTION_STRING")
            self.cursor = self.conection.cursor()
        except pyodbc.Error as e:
            print(f"Database connection error: {e}")



    def consultaFilms(self, title: str):
        self.title=title
        cursor = self.cursor

        consultaSelect = ('SELECT genres, ImdbRating, PosterURL, imdbId FROM Films where title = ?')
        self.cursor.execute(consultaSelect,(self.title,))
        row = cursor.fetchone()

        imdbId = str(row[3])
        self.genre = row[0].split('|')
        self.rating = float(row[1].replace(',', '.')) if row[1] else get_rating(imdbId)
        self.poster = row[2] if row[2] != None else  getPoster(imdbId)

        result = [self.genre, self.rating, self.poster]

        return result

    def insertBBDD(self):

        cursor = self.cursor


        consultaUpd = 'update Films set ImdbRating=? , PosterURL = ? where title = ?'
        cursor.execute(consultaUpd,(self.rating, self.poster,self.title))
        self.conection.commit()




title = 'Nixon (1995)'

data = dataReturn()
retorno = data.consultaFilms(title)
bbdd = data.insertBBDD()
print(retorno)
print(bbdd)



"""

conn = pyodbc.connect('Driver={SQL Server};''Server=.;''Database=Films;''Trusted_Connection=yes;')
cursor = conn.cursor()
title = 'GoldenEye (1995)'
consulta  = ('SELECT genres, ImdbRating, PosterURL, imdbId FROM Films where title = ?')
print(consulta)
cursor.execute(consulta,(title,))
row = cursor.fetchone()
print(row)
imdbId = str(row[3])

genre = row[0].split('|')
rating = float(row[1].replace(',', '.')) if row[1] else get_rating(imdbId)
poster = row[2] if row[2] != None else  getPoster(imdbId)

print(genre, rating, poster)



consulta = ('update Films set ImdbRating=? , PosterURL = ? where title = ?')
cursor.execute(consulta,(rating,poster,title))
conn.commit()"""