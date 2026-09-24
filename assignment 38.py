def print_factors(number):
    print(f"The factors of {number} are:")
    # Loop from 1 to the number itself
    for i in range(1, number + 1):
        if number % i == 0:
            print(i, end=" ")
    print()
# Example usage:
num = int(input("Enter a number: "))
print_factors(num)
