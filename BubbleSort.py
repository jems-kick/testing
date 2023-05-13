sort = [10, 2, 3, 5, 8, 6, 9, 1, 4, 7]
for i in range(len(sort)):
    for j in range(len(sort)):
        if j < len(sort)-1:
            if sort[j+1] < sort[j]:
                temp = sort[j]
                sort[j] = sort[j+1]
                sort[j+1] = temp
print(sort)