#Task 1
centimeter=float(input('Enter the zander centimeter: '))
if centimeter<42:
    print(f'Your fish has escaped, your zander need to be {42-centimeter} centimeters longer to catch the fish')
else:
    print('You successfully catch the fish')

#Task 2
cabin=input('Enter the cabin class: ')
if cabin=='LUX':
    print('Upper-deck cabin with a balcony.')
elif cabin=='A':
    print('Above the car deck, equipped with a window.')
elif cabin=='B':
    print('Windowless cabin above the car deck.')
elif cabin=='C':
    print('Windowless cabin below the car deck.')
else:
    print('Invalid cabin class')

#Task 3
gender=input('Enter your gender: ')
hemoglobin=int(input('Enter your hemoglobin: '))
if gender=='Male':
    if 134<=hemoglobin<=167:
        print('Your hemoglobin is normal')
    elif hemoglobin>167:
        print('Your hemoglobin is high')
    elif hemoglobin<134:
        print('Your hemoglobin is low')
elif gender=='Female':
    if 117<=hemoglobin<=155:
        print('Your hemoglobin is normal')
    elif hemoglobin>155:
        print('Your hemoglobin is high')
    elif hemoglobin<117:
        print('Your hemoglobin is low')

#Task 4
year=int(input('Enter a year: '))
if year%4==0 and year%100!=0 or year%400==0:
    print('This year is a leap year')
else:
    print('This year is not a leap year')

#Task 5
import math
d1=float(input('Enter the 1st pizza diameter: '))
p1=float(input('Enter the price: '))
d2=float(input('Enter the 2nd pizza diameter: '))
p2=float(input('Enter the price: '))
v1=p1/((d1/2)**2*math.pi)
v2=p2/((d2/2)**2*math.pi)
if v1<v2:
    print('The 1st pizza provide better value for money')
else:
    print('The 2nd pizza provide better value for money')