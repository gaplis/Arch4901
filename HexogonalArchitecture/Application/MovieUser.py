from HexogonalArchitecture.Domain.MovieSearchRequest import MovieSearchRequest
from HexogonalArchitecture.Ports.IUserInput import IUserInput


class MovieUser:
    def __init__(self, user_input_driver_port: IUserInput):
        self.user_input_driver_port = user_input_driver_port

    def process_input(self, movie_search_request: MovieSearchRequest):
        self.user_input_driver_port.handler_user_input(movie_search_request)
