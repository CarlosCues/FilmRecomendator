
from django.shortcuts import render
from RecomendacionApp.models import dataReturn


def index(request):
    dataFilm = dataReturn()

    if request.method == 'POST':
        movieName = request.POST.get('movieName')

        datos = dataFilm.consultaFilms(movieName)

        contexto = {
            "lista_datos": datos
        }
        dataFilm.updateBBDD()
        dataFilm.closeConnection()
        print(contexto)
        return render(request, "Index.html", contexto)

    dataFilm.updateBBDD()
    dataFilm.closeConnection()
    return render(request, 'Index.html')
