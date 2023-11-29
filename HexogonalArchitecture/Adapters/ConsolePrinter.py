from HexogonalArchitecture.Ports.IPrintMovieReviews import IPrintMovieReviews


class ConsolePrinter(IPrintMovieReviews):

    def write_movie_reviews(self, movie_reviews):
        for movie_review in movie_reviews:
            print(movie_review)
