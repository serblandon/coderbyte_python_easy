list = [1, 5, 2, 3, 5, 1, 4, 3]
uniques = []

print(list)

for i in list:
    if i not in uniques:
        uniques.append(i)

print(uniques)