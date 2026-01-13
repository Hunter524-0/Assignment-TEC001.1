#Task 2

a=input('Your name: ')
print(f'Hello, {a}!')

#Task 3
import math
radius=float(input('Circle radiant: '))
circumference=radius*2*math.pi
print(f'Circle circumference: {circumference:.2f}')

#Task 4
length=float(input('Length: '))
width=float(input('Width: '))
perimeter=(length+width)*2
area=length*width
print(f'Perimeter: {perimeter:.2f}')
print(f'Area: {area:.2f}')

#Task 5
x=int(input('#1: '))
y=int(input('#2: '))
z=int(input('#3: '))
summ=x+y+z
product=x*y*z
average=summ/3
print(f'Sum: {summ:2f}')
print(f'Product: {product:.2f}')
print(f'Average: {average:.2f}')

#Task 6:
talent=float(input('Talent: '))
pound=float(input('Pound: '))
lot=float(input('Lot: '))
talent_to_gram=talent*20*32*13.3
pound_to_gram=pound*32*13.3
lot_to_gram=lot*13.3
total_gram=talent_to_gram + pound_to_gram + lot_to_gram
kilogram=int(total_gram/1000)
gram=float(total_gram-kilogram*1000)
print(f'Kilogram: {kilogram} and gram: {gram:.2f}')

#Task 7
import random
b1=random.randint(0,9)
b2=random.randint(0,9)
b3=random.randint(0,9)
print(f'3-digit code {b1}{b2}{b3}')
c1=random.randint(1,6)
c2=random.randint(1,6)
c3=random.randint(1,6)
c4=random.randint(1,6)
print(f'4-digit code {c1}{c2}{c3}{c4}')