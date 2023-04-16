parentheses = [el for el in input()]
opening_parentheses = []
balanced_parentheses = True
for each_parenthesis in parentheses:
    if each_parenthesis == '(' or each_parenthesis == '{' or each_parenthesis == '[':
        opening_parentheses.append(each_parenthesis)
    elif len(opening_parentheses) > 0:
        if each_parenthesis == ')':
            if opening_parentheses.pop() == '(':
                continue
            else:
                balanced_parentheses = False
                break
        elif each_parenthesis == '}':
            if opening_parentheses.pop() == '{':
                continue
            else:
                balanced_parentheses = False
                break
        elif each_parenthesis == ']':
            if opening_parentheses.pop() == '[':
                continue
            else:
                balanced_parentheses = False
                break
    else:
        balanced_parentheses = False
        break


if balanced_parentheses:
    print('YES')
else:
    print('NO')
