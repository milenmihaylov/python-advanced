def age_assignment(*args, **kwargs):
    names_dict = {}
    for name in args:
        first_letter = name[0]
        if first_letter in kwargs:
            names_dict[name] = kwargs[first_letter]
    return names_dict


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))