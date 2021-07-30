x = int(input('pls enter num1: '))
y = int(input('pls enter num2: '))
z = int(input('pls enter num3: '))

if x<y+z and y<x+z and z<x+y :
    print('You can create a Triangle')
else:
    print('You can\'t create a Triangle')