import requests
from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import numpy as np





"""movie_title= 'Andrew Dice Clay: Dice Rules (1991)'
match = df_Movies.loc[df_Movies['title'] == movie_title, 'ImdbRating']

if np.isnan(match.values[0]):

    match = 0.0  # Replace NaN with 0.0 or any other desired value

else:
    print('False')"""


def getRating(id: str):
    """
    Funcion que devuelve el rating de una pelicula
    :param id str: id de la pelicula de la que mostrar el rating
    :return: rating otorgado por imdb
    """
    result = None

    df_Movies = pd.read_excel(r'C:\Users\ccues\PycharmProjects\HackatonFixed\files\datasetMoviesExcel.xls')
    print(df_Movies.columns)
    print(df_Movies['imdbId'])
    print(df_Movies.info())

    match = df_Movies.loc[df_Movies['imdbId'] == id, 'ImdbRating']
    print('AA',match)
    if np.isnan(match.values[0]):

        ApiKey = os.getenv('IMDB_KEY')
        api_url = f"https://imdb-api.com/API/Ratings/{ApiKey}/tt{id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            rating = response.json()
            imdbRating = rating['imDb'] if rating else "No hay Rating"
            df_Movies.loc[df_Movies['imdbId'] == id, 'ImdbRating'] = imdbRating

        df_Movies.to_excel('updated_datasetMoviesExcel.xls', index=False)
        print(imdbRating)
        return imdbRating

    else:
        print('False')








getRating('101726.0')

