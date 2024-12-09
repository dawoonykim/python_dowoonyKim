a = dict()

a = set()


class b:
    pass
    # pass는 말 그대로 아무것도 안 하고 넘어가겠다는 뜻
    # class를 아예 비워놓으면 에러가 발생


bb1 = b()
bb2 = b()
bb3 = b()


class Movie:
    title = "범죄도시"


movie1 = Movie()
movie2 = Movie()

print(movie1.title)
print(movie2.title)

movie1.title = "파묘"
print(movie1.title)
print(movie2.title)

movie1.score = "1"
print(movie1.score)
# print(movie2.score)
