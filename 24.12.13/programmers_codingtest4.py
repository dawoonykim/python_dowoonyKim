# 프로그래머스 - 로그인 성공

def solution(id_pw, db):
    answer = ''
    id = id_pw[0]
    pw = id_pw[1]

    for i in range(len(db)):
        print(f"db.id : {db[i][0]}, db.pw : {db[i][1]}, id : {id}, pw : {pw}")
        if id == db[i][0] and pw == db[i][1]:
            return "login"
        elif id == db[i][0] and pw != db[i][1]:
            return "wrong pw"
    else:
        return "fail"


print(solution(["meosseugi", "1234"], [["rardss", "123"],
      ["yyoom", "1234"], ["meosseugi", "1234"]]))
print(solution(["programmer01", "15789"], [["programmer02", "111111"], [
    "programmer00", "134"], ["programmer01", "1145"]]))
print(solution(["rabbit04", "98761"], [["jaja11", "98761"],
                                       ["krong0313", "29440"], ["rabbit00", "111333"]]))
