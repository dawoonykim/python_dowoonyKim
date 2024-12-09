class Movie:
    name = ''

    def print_msg(msg):
        print(msg)

    def modify(self, movie):
        self.name = movie

    def print_name(self):
        print(self.name)


movie1 = Movie()
movie2 = Movie()

Movie.print_msg("프린트하기")
# Movie.modify(movie1,"print하기 2")
movie1.modify("print하기 3")
movie1.print_name()
movie2.modify("프린트하기 4")
print(f"movie2.name : {movie2.name}")
# movie1.print_msg("ttt")
