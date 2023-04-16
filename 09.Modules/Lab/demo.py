import sys
# from io import StringIO
import random
import this
from io import StringIO

test_input = '''1
2
3
'''

sys.stdin = StringIO(test_input)

x = int(input())
y = int(input())
z = int(input())

print(x+y+z)
print(sys.path)
