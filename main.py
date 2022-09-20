a = ["A", "B", "C"]
b = ["B", "A"]
c = all(map(lambda x: x in a, b))
print(c)
