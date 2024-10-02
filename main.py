def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Пример использования
x = 56
y = 98
print(f"НОД({x}, {y}) = {gcd(x, y)}")
