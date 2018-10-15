import webbrowser


# Movie class for saving data that will be displayed in the site
class Movie():

    # Constructor which receives:
    # 1) Movie Title, 2) storyline, 3) Poster Image, 4) youtube trailer link
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
