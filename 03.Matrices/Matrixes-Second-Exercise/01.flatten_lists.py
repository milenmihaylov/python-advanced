matrix = [el.split() for el in input().split('|')]
print(' '.join([' '.join(matrix[i * (-1) - 1]) for i in range(len(matrix)) if matrix[i * (-1) - 1]]))

#
# numbers = input().split('|')
#
# for el in reversed(numbers):
#     tmp_list = el.split()
#     tmp_string = " ".join(tmp_list)
#     if tmp_string:
#         print(tmp_string, end=' ')