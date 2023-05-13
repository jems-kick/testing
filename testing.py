num = 64
binary_num = bin(num)[2:]  # convert decimal to binary and remove '0b' prefix
num_digits = len(binary_num)
print(num_digits)