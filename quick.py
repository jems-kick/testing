def merge_quick(array):
    if len(array) <= 1:
        return array
    pivit = array[-1]
    index = 0
    while True:
        if array[index] == pivit:
            break
        if array[index] > pivit:
            array.append(array[index])
            array.pop(index)
        else:
            index += 1

    return (merge_quick(array[:array.index(pivit)])+ merge_quick(array[array.index(pivit):]))

if __name__ == "__main__":
    array = [9, 7, 5, 3, 1, 2, 10, 50,654,5545,6, 8, 4, 11, 100]
    print(merge_quick(array))