with open("./output/poodle.jpg", "rb") as f1:
    img = f1.read()
with open("./output/poodle11.jpg", "wb")as f2:
    f2.write(img)
