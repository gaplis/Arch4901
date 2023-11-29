class MovieReviews:
    def __init__(self, movie_name, movie_score, remark):
        self.movie_name = movie_name
        self.movie_score = movie_score
        self.remark = remark

    def __str__(self):
        return f'{self.movie_score} {self.remark}'
