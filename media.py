class Movie():
    '''
    This is the movie class, the movie class contain the title, poster images
    and trailer attribute
    '''
    def __init__(self,movie_title,poster_image_url,trailer_youtube_url):
        self.title = movie_title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
