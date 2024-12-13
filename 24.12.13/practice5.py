a = 1
try:
    a += 1
    if a == 2:
        raise Exception
    a += 2
    print(f"a : {a}")
except:
    print("error", a)
