score = {"Alice": 85, "Bob": 90, "Charlie": 95}
# print(type(score))
# print(score)

score["David"] = 80
# print(score)
score["Alice"] = 88
# print(score)
del score["Bob"]
# print(score)

for i in score.keys():
    print(f"{i} : {score.get(i)}", end=" ")
