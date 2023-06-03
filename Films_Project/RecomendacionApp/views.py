from django.http import HttpResponse
from django.shortcuts import render
from RecomendacionApp.models   import MovieData



def index(request):
    dataFilm = MovieData()
    if request.method == 'POST':
        movieName = request.POST.get('movieName')

        idMovie = dataFilm.get_imdb_id(movieName)
        genero = dataFilm.return_genre(movieName)
        poster = dataFilm.getPoster(idMovie)
        rating = dataFilm.getRating(idMovie)

        datos = [
            poster, rating, genero
        ]

        contexto = {
            "lista_datos": datos
        }
        print(contexto)
        return render(request, "Index.html", contexto)

    return render(request, 'Index.html')
