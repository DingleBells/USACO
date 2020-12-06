"""
ID: kanghee2
LANG: PYTHON3
TASK: test
"""
textin = open('test.in', 'r')
textout = open('test.out', 'w')
x,y = map(int, textin.readline().split())
textout.write (str(x+y) + '\n')
textout.close()