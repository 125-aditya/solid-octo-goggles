def inverted_pyramid(rows):
    for i in range(rows):
     print(" " * i + "*" * (2 * (rows - i) - 1))
inverted_pyramid(5)
