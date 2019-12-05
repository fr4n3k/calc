
import sys

print ('Write down to integer')
str1 = input('Write down first number: ')
str2 = input('Write down second number: ')
try:
    num1 = int(str1)
    num2 = int(str2)
except:
    print('Those are not integers')
    sys.exit(0)

print ('what do you want to do?')
print ('1 - addition')
print ('2 - subtraction')
print ('3 - multiplication')
print ('4 - division')
kind_of_calculation = input()

equals = 0

if kind_of_calculation == '1':
    equals = num1 + num2
elif kind_of_calculation == '2':
    equals = f"This is awesome! {num1 - num2}"
elif kind_of_calculation == '3':
    equals = num1 * num2
elif kind_of_calculation == '4':
    equals = num1 / num2
else:
    print ('sth went wrong')

print (equals)
