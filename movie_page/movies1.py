#movies//
#Title, Poster_image, Youtube Trailer, some story_line
import webbrowser
class Movie():
    """ This is a sample webpage, created in the process of learning about classes, objects and other few stuff about Python. """

    VALID_RATINGS = ["G","PG","PG-13","R"]

    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer): #self is itself or a instance being created
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
