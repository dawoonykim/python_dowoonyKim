# name = input("이름 : ")
# password = input("비밀번호 : ")
# dic = dict()
# with open("./member/member.txt", "r") as f:
#     for line in f:
#         n, p = line.split()
#         dic[n] = p

#     print(dic)
#     if dic[name] == password:
#         print("로그인 성공!!")
#         phone_li = dict()
#         if not phone_li:
#             with open("./member/member_tel.txt", "a") as f:
#                 for line in f:
#                     exist_name, exist_phone = line.split()
#                     if exist_name=="":
#                         num = input("새로운 전화번호를 입력하세요 : ")
#                         f.write(f"{name} {num}\n")

#                     else:
#                         num = input("전화번호 수정 : ")
#                         f.write(f"{name} {num}\n")
#                     phone_li[name] = num

#     else:
#         print("로그인 실패")
