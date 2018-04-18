list1 = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
dict1 = {}

for i in range(len(list1)):
    var = list(list1[i])
    dict1[var[0]] = var[1]

print(dict1)
