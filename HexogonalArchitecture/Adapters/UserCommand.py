from HexogonalArchitecture.Application.MovieApp import MovieApp
from HexogonalArchitecture.Domain.Model import Model
from HexogonalArchitecture.Ports.IFetchMovieReviews import IFetchMovieReviews
from HexogonalArchitecture.Ports.IPrintMovieReviews import IPrintMovieReviews
from HexogonalArchitecture.Ports.IUserInput import IUserInput


class UserCommand(IUserInput):
    def __init__(self, fetch_movie_reviews: IFetchMovieReviews, print_movie_reviews: IPrintMovieReviews):
        movie_app = MovieApp(fetch_movie_reviews, print_movie_reviews)
        self.model = Model(movie_app)

    def handler_user_input(self, user_command):
        self.model.run(user_command)
