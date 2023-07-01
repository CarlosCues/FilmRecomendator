import os
import pyodbc
import requests

from dotenv import load_dotenv
load_dotenv()


def getRating(id: str):
        """Function that returns the rating of a movie
        :param id (str):  id of the film to display the rating .
        :return: the film´s rating if available, otherwise  it returns 'no hay rating'"""
        ApiKey = os.getenv('IMDB_KEY')

        id = id.zfill(7)
        api_url = f"https://imdb-api.com/API/Ratings/{ApiKey}/tt{id}"
        response = requests.get(api_url)

        if response.status_code == 200:
                imdbRating = float(response.json()['imDb'])
                return imdbRating
        else:
                return 'No hay rating'


def getPoster(id: str):
        """Function that returns the poster of a movie.
        :param id (str):  id of the film to display the poster.
        :return: the link of the film's poster if available, otherwise  it returns ''No hay poster disponible'"""


        ApiKey = os.getenv('IMDB_KEY')
        id = id.zfill(7)
        api_url = f"https://imdb-api.com/en/API/Posters/{ApiKey}/tt{id}"
        print(api_url)

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
                self.connectToDatabase()

        def connectToDatabase(self):
                """Establish a connection with the database
                :param :  None
                :return: None'"""
                try:
                        connectionString = os.getenv("CONNECTION_STRING")
                        self.conection = pyodbc.connect(connectionString)
                        self.cursor = self.conection.cursor()
                except pyodbc.Error as e:
                        print(f"Database connection error: {e}")

        def closeConnection(self):
                """Close the connection and cursor
                :param :  None
                :return: None'"""
                if self.cursor is not None:
                        self.cursor.close()
                if self.conection is not None:
                        self.conection.close()

        def consultaFilms(self, title: str):
                """Function that extract the rating, poster and genre from the database, if poster and
                rating equals null in it, it call the appropiate functions to do so
                :param tittle (str): ttile of the film to display the data. It is introduced by the user.
                :return: list of string with the information requiered'"""
                self.title = title
                cursor = self.cursor
                consultaSelect = ('SELECT genres, ImdbRating, PosterURL, imdbId FROM Films where title = ?')
                self.cursor.execute(consultaSelect, (self.title,))
                row = cursor.fetchone()

                imdbId = str(row[3])
                self.genre = row[0].split('|')
                self.rating = float(row[1].replace(',', '.')) if row[1] else getRating(imdbId)
                self.poster = row[2] if row[2] != None else getPoster(imdbId)

                result = [self.genre, self.rating, self.poster]

                return result

        def updateBBDD(self):
                """Function that insert new data in the ddbb
                :param: None
                :return: there is no return"""

                cursor = self.cursor

                consultaUpd = 'update Films set ImdbRating=? , PosterURL = ? where title = ?'
                cursor.execute(consultaUpd, (self.rating, self.poster, self.title))
                self.conection.commit()


