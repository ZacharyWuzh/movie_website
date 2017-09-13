from media import Movie
from fresh_tomatoes import open_movies_page
fifty_shades_darker = Movie('Fifty Shades Darker','https://i.ytimg.com/vi/mxU3C\
lfuI80/movieposter.jpg','https://www.youtube.com/watch?v=aRrVHR5zuQg')
kingsman_the_secret_service = Movie('Kingsman: The Secret Service','https://imag\
es-na.ssl-images-amazon.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NT\
IwNDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg','https://www.youtube.com/watch?v=xkX\
8jKeKUEA')
titanic = Movie('Titanic','https://images-na.ssl-images-amazon.com/images/M/MV5\
BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._\
V1_UY1200_CR88,0,630,1200_AL_.jpg','https://www.youtube.com/watch?v=2e-eXJ6HgkQ')



movies = [fifty_shades_darker,kingsman_the_secret_service,titanic]
open_movies_page(movies)
