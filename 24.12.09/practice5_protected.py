class Movie:
    count = 0

    def __init__(self, title, audience):
        self._title = title
        self._audience = audience
        Movie.count += 1

    def get_title(self):
        return self._title

    def set_title(self, title):
        self._title = title


movie1 = Movie("파묘", 100)
# print(movie1.__title)
print(movie1.get_title())

movie1._title = "오징어게임"  # 변수 값 변경 불가
print(movie1._title)
# movie1.set_title("오징어 게임")
# print(movie1.get_title())
