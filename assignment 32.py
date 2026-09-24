def count_odds(n: int) -> int:
    return (n + 1) // 2 if n > 0 else 0

# Example usage:
n = 10
print(f"Number of odd numbers from 1 to {n}: {count_odds(n)}")
n = 11
print(f"Number of odd numbers from 1 to {n}: {count_odds(n)}")
