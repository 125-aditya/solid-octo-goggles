def right_aligned_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
right_aligned_triangle(5)
