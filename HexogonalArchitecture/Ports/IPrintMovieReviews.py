from abc import ABC, abstractmethod


class IPrintMovieReviews(ABC):

    @abstractmethod
    def write_movie_reviews(self, movie_reviews):
        pass
