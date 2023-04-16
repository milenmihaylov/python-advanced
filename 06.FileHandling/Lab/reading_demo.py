import os
from os import path
# confirm = input("Do you want to delete this file? (y/n): ")
# if confirm == 'y':
#     if os.path.exists('asd.txt'):
#         os.remove('asd.txt')
#
# # [print(x) for x in os.listdir('.')]
#
# for file_name in os.listdir():
#     get_full_path = path.join(os.getcwd(), file_name)
#     print(os.getcwd())
#     print(get_full_path)

ss = [os.getcwd()]
while ss:
    current_dir = ss.pop()
    print(current_dir)
    if path.isfile(current_dir):
        continue

    for file_path in os.listdir(current_dir):
        absolute_path = path.join(
            current_dir,
            file_path
        )
        ss.append(absolute_path)
print(ss)
