class Movie():
    """ A class with a constructor to create instances of Move oject with title, storyline, poster image and url to movie"""

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
