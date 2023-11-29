from typing import List
import random
from HexogonalArchitecture.Domain.MovieReviews import MovieReviews

from HexogonalArchitecture.Ports.IFetchMovieReviews import IFetchMovieReviews
from HexogonalArchitecture.Ports.IPrintMovieReviews import IPrintMovieReviews


class MovieApp:
    def __init__(self, fetch_movie_reviews: IFetchMovieReviews, print_movie_reviews: IPrintMovieReviews):
        self.fetch_movie_reviews = fetch_movie_reviews
        self.print_movie_reviews = print_movie_reviews

    def filter_random_reviews(self, movie_reviews_list: List[MovieReviews]):
        result = []
        for index in range(5):
            if len(movie_reviews_list) < 1:
                break
            random_index = self.get_random_element(len(movie_reviews_list))
            movie_review = movie_reviews_list[random_index]
            movie_reviews_list.remove(movie_review)
            result.append(movie_review)

        return result

    def get_random_element(self, size):
        return random.randint(0, size - 1)

    def accept(self, movie_search_request):
        movie_reviews_list = self.fetch_movie_reviews.fetch_movie_reviews(movie_search_request)
        random_reviews = self.filter_random_reviews(list(movie_reviews_list))
        self.print_movie_reviews.write_movie_reviews(random_reviews)
