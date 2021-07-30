name = input('pls enter the first name: ')
family = input('pls enter the last name: ')

score1 = float(input('pls enter your first score: '))
score2 = float(input('pls enter your second score: '))
score3 = float(input('pls enter your third score: '))

avg = (score1+score2+score3)/3

print(f'Avg for {name} {family} is {avg:.2f} and his\her Condition is ', end='')

if 17 <= avg :
    print('Great')

elif 12 <= avg < 17 :
    print('Normal')

elif avg < 12 :
    print('Fail')