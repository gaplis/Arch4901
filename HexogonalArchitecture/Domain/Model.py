from HexogonalArchitecture.Application.MovieApp import MovieApp


class Model:

    def __init__(self, movie_app: MovieApp):
        self.movie_app = movie_app

    def run(self, user_command):
        self.movie_app.accept(user_command)
