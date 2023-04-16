def fact_rec(number):
    if number == 1:
        return 1
    elif number == 0:
        return 1
    return number * fact_rec(number - 1)


print(fact_rec(17))
