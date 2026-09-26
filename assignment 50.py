def number_pyramid(rows):
    for i in range(1,rows+1):
        print(" " * (rows - i), end="")
        print(str(i)*(2 * i - 1))

number_pyramid(5)
