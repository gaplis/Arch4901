class MovieSearchRequest:
    def __init__(self, name):
        self.request = name

    def get_movie_name(self):
        return self.request
