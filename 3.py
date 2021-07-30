x = float(input('pls enter your Weight(kg): '))
y = float(input('pls enter your Height(m): '))
BMI = x/(y**2)
print(f'your BMI is {BMI:.2f} and ',end='')

if BMI<18.5 :
    print('You are Underweight')
elif 18.5<=BMI<=24.9 :
    print('You are Normal')
elif 25<=BMI<=29.9 :
    print('You are Overweight')
elif 30<=BMI<=34.9 :
    print('You are Obese')
elif 35<=BMI :
    print('You are Extremely Obese')