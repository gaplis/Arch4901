from HexogonalArchitecture.Domain.MovieReviews import MovieReviews
from HexogonalArchitecture.Domain.MovieSearchRequest import MovieSearchRequest
from HexogonalArchitecture.Ports.IFetchMovieReviews import IFetchMovieReviews


class MovieReviewsRepo(IFetchMovieReviews):
    def __init__(self):
        self.movie_review_map = {}
        self.initialize()

    def initialize(self):
        self.movie_review_map = {
            "Star Wars": [MovieReviews('1', 7.5, "Good")],
            "Star Track": [MovieReviews('1', 9.5, "Excellent"), MovieReviews('1', 8.5, "Good")],
        }

    def fetch_movie_reviews(self, movie_search_request: MovieSearchRequest):
        return self.movie_review_map.get(movie_search_request.get_movie_name(), [])
