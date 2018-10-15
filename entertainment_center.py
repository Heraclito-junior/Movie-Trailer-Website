import media
import fresh_tomatoes

# This file creates a list of movies that will be used by fresh_tomatoes.py
# Im using the media class which constructor  receives:
# 1) Movie Title, 2) storyline, 3) Poster Image, 4) youtube trailer link

toy_story = media.Movie(
    "Toy Story",
    "A Story of a Boy",
    "https://todateen.com.br/wp-content/uploads/" +
    "2018/04/frases-de-toy-story.jpg",
    "https://www.youtube.com/watch?v=tN1A2mVnrOM"
    )

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/pt/thumb/b/b0/" +
    "Avatar-Teaser-Poster.jpg/250px-Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=2MIvbG5u1l0"
    )

school_of_rock = media.Movie(
    "Shool of Rock",
    "Black jack teacher",
    "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/" +
    "School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie(
    "Ratatouille",
    "Rat controlled humans",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=I9K-ehX4RqA")

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "Never heard of it",
    "https://upload.wikimedia.org/wikipedia" +
    "/en/9/9f/Midnight_in_Paris_Poster.jpg",
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie(
    "Hunger Games",
    "Insert joke here, something funny but refined",
    "https://upload.wikimedia.org/wikipedia/en/thumb/3/39/" +
    "The_Hunger_Games_cover.jpg/220px-The_Hunger_Games_cover.jpg",
    "https://www.youtube.com/watch?v=mfmrPu43DF8")


# List of movies that fresh_tomatoes.open_movies_page() takes as paramater
movies = [toy_story, avatar, school_of_rock, midnight_in_paris, hunger_games]

# Function call of fresh tomatoes that generates a HTML page with the declared movies
fresh_tomatoes.open_movies_page(movies)
