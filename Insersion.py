collection = [2, 10, 3, 5, 8, 6, 9, 1, 4, 7]
for index in range(1, len(collection)):
    while index > 0 and collection[index - 1] > collection[index]:
            collection[index], collection[index - 1] = collection[index - 1], collection[index]
            index -= 1

print(collection)