def introduce(**kw):
    print(type(kw))
    for k, v in kw.items():
        print(f"{k} : {v}")

introduce(name="Alice", age=25, city="New York")
