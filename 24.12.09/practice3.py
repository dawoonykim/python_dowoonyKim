# class Movie:
#     def __init__(self):
#         print("Hello")


# movie = Movie()

class Movie:
    count = 0

    def __init__(self, title, audience):
        self.title = title
        self.audience = audience

    def __init__(self, title="오징어게임", audience=300):
        self.title = title
        self.audience = audience


movie1 = Movie("파묘", 100)
movie2 = Movie("파묘2", 200)

print(movie1.title, movie1.audience)
print(movie2.title, movie2.audience)

movie3 = Movie()
print(movie3.title, movie3.audience)