try:
    print(input() * int(input()))
except ValueError:
    print("Variable times must be an integer")
