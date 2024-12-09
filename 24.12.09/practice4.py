class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience
        Movie.count += 1

    # def __init__(self, title="오징어게임", audience=300):
    #     self.title = title
    #     self.audience = audience


movie1 = Movie("파묘", 100)
print(Movie.count)
movie2 = Movie("파묘2", 200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

Movie.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)

movie1.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)

Movie.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)
Movie.count += 1
print(movie1.count)
print(movie2.count)
print(Movie.count)