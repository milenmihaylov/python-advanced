numbers_dictionary = {}

try:
    line = input()
    while line != "Search":
        try:
            number_as_string = line
            number = int(input())
            numbers_dictionary[number_as_string] = number
        except ValueError:
            print("The variable number must be an integer")
        finally:
            line = input()

    line = input()
    while line != "Remove":
        try:
            searched = line
            print(numbers_dictionary[searched])
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()

    line = input()
    while line != "End":
        try:
            searched = line
            del numbers_dictionary[searched]
        except KeyError:
            print("Number does not exist in dictionary")
        line = input()

finally:
    print(numbers_dictionary)
