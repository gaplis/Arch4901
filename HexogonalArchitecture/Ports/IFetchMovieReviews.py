from abc import ABC, abstractmethod
from HexogonalArchitecture.Domain.MovieSearchRequest import MovieSearchRequest


class IFetchMovieReviews(ABC):

    @abstractmethod
    def fetch_movie_reviews(self, movie_search_request: MovieSearchRequest):
        pass
