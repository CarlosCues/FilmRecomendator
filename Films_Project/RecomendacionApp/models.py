import pandas as pd
import requests
from dotenv import load_dotenv
load_dotenv()
import os



class MovieData:

    def __init__(self):
        self.id = 0
        self.df_Movies = pd.read_excel(r'C:\Users\ccues\PycharmProjects\HackatonFixed\files\datasetMoviesExcel.xls')

    def get_imdb_id(self, movie_title: str):

        df_Movies = self.df_Movies
        match = df_Movies.loc[df_Movies['title'] == movie_title, 'imdbId']
        imdb_id = str(match.values[0]).zfill(7)

        self.id = imdb_id
        return imdb_id



    def return_genre(self, movie_title: str):

        df_Movies = self.df_Movies
        match = df_Movies.loc[df_Movies['title'] == movie_title, 'genres']
        genre = match.values[0].split("|")
        print(genre)

        return genre

    def getPoster(self,id: str):
        """
        Funcion que devuelve el Poster de una pelicula
        :param id str:  id de la pelicula de la que mostrar el poster
        :return: link  a de la imagen
        """
        result = None

        ApiKey = os.getenv('IMDB_KEY')
        api_url = f"https://imdb-api.com/en/API/Posters/{ApiKey}/tt{id}"

        response = requests.get(api_url)
        if response.status_code == 200:
            poster = response.json()
            result = poster['posters'][0]['link'] if poster['posters'] else "No hay Poster"
            return result

        return result

    def getRating(self,id: str):
        """
        Funcion que devuelve el rating de  una pelicula
        :param id str:  id de la pelicula de la que mostrar el rating
        :return: rating otorgado por imdb
        """
        result = None
        ApiKey = os.getenv('IMDB_KEY')
        api_url = f"https://imdb-api.com/API/Ratings/{ApiKey}/tt{id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            rating = response.json()

            result = rating['imDb'] if rating else "No hay Rating"

            return result

        return result



