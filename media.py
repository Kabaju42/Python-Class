import fresh_tomatoes
import webbrowser

class Movie:
    """
    Movie class for reviews
    """
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self._title = title
        self._storyline = storyline
        self._poster_image_url = poster_image_url
        self._trailer_youtube_url = trailer_youtube_url
        pass

    def show_trailer(self):
        """
        Open a browser and play the trailer of the movei
        :return:
        """
        webbrowser.open(self._trailer_youtube_url)
        pass



def main():
    movies = []
    toy_story = Movie("Toy Story", "A story about toys",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                      "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    bugs_life = Movie("Bugs Life", "",
                      "https://upload.wikimedia.org/wikipedia/en/thumb/c/cc/A_Bug%27s_Life.jpg/220px-A_Bug%27s_Life.jpg",
                      "https://www.youtube.com/watch?v=OAQ_fkSQ2_s")
    cars = Movie("Cars", "",
                 "https://upload.wikimedia.org/wikipedia/en/thumb/3/34/Cars_2006.jpg/220px-Cars_2006.jpg",
                 "https://www.youtube.com/watch?v=SbXIj2T-_uk")
    muppets_xmas_carol = ("Muppets Christmas Carol", "Muppets play on a classic story",
                            "https://upload.wikimedia.org/wikipedia/en/9/95/Muppet_christmas_carol.jpg",
                            "https://www.youtube.com/watch?v=clK-T5oI7Lg")
    # toy_story.show_trailer()

    movies.append(toy_story)
    movies.append(bugs_life)
    movies.append(cars)
    movies.append(muppets_xmas_carol)

    fresh_tomatoes.open_movies_page(movies)


if __name__ == '__main__':
    main()
    exit(0)

