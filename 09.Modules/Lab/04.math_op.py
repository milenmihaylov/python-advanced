import matematical_operations

number_1, sign, number_2 = input().split()
result = matematical_operations.calculate(float(number_1), int(number_2), sign)
try:
    print(f"{result:.2f}")
except ValueError:
    print(result)
