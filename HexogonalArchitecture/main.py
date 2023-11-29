
from HexogonalArchitecture.Adapters.ConsolePrinter import ConsolePrinter
from HexogonalArchitecture.Adapters.MovieReviewsRepo import MovieReviewsRepo
from HexogonalArchitecture.Adapters.UserCommand import UserCommand
from HexogonalArchitecture.Application.MovieUser import MovieUser
from HexogonalArchitecture.Domain.MovieSearchRequest import MovieSearchRequest


if __name__ == '__main__':

    fetch_movie_reviews = MovieReviewsRepo()
    print_movie_reviews = ConsolePrinter()

    user_command = UserCommand(fetch_movie_reviews, print_movie_reviews)

    movie_user = MovieUser(user_command)

    star_wars_request = MovieSearchRequest("Star Wars")
    star_track_request = MovieSearchRequest("Star Track")

    print(f"Displaying reviews for movie {star_wars_request.get_movie_name()}")
    movie_user.process_input(star_wars_request)

    print(f"Displaying reviews for movie {star_track_request.get_movie_name()}")
    movie_user.process_input(star_track_request)
