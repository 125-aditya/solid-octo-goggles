def reversed_half_pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("1", end="")
        print("\r")

reversed_half_pyramid(5)