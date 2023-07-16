## Film Recomendator

### 💥💥 Desarrollo de una pagina web de recomendación de películas en arquitectura MTV bajo el framework Django.

Una vez el usuario introduce el nombre de una pélicula se devuelve informacion sobre el rating dde Imdb, el poster de la película y género categorizado por Imdb. 
Ademas en base al rating y a la categoría de la  pelécula se hace una recomendacion de películas similares, si el usaurio hace click en alguna recomendación, 
se muestra la informacion sobre dicha pélicula.

** Actualmente solo está publicado las capas de Modelo(M) y Templates(T). La capa de Vista(V) se publicará proximamente.

## How it works? 🔧🔧🔧
Al seleccionar una película en el buscador se hace una búsqueda a la BBDD. Si los datos de rating, poster y género se encuentran en la base de datos los devuelve para mostrarlos en el template. En el caso de que no estén los datos en la BBDD se hace una llamada a la APi de Imdb, se devuelven los datos encontrados al template y se guardan los datos en la BBDD para que la siguiente vez que se búsque esa película no tener que llamar a la APi.

## Fases del proyecto han sido(a falta de templates):

- Creación de una BBDD en SQL Server.
- Conexión con SQL Server.
- Conexión a la API de Imdb.
- Desarrollo de la capa de datos.
- Desarrollo de la lógica de negocio.


## Next Steps: 

--Mejora del sistema de recomendacion 
- Incluir resumen de la pélicula generado con ChatGpt.


Proyecto desarrollado integramente en Python

## Participantes del proyecto:
[Alejandro HM](https://github.com/Usrg30) 




