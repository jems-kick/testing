collection = [10, 2, 3, 5, 8, 6, 9, 1, 4, 7]

length = len(collection)
for i in range(length - 1):
    min = i
    for k in range(i + 1, length):
        if collection[k] < collection[min]:
            min = k
    collection[min], collection[i] = (
        collection[i], collection[min]
    )

print(collection)