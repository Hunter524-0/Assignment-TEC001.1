#Task 1
a = 1
while a <= 1000:
    if a % 3 == 0:
        print(a)
    a += 1

#Task 2
while True:
    inch = float(input("Enter inches: "))
    centimeter = inch * 2.54
    if inch < 0:
        break
    print(f'{centimeter:.2f} centimeter')

#Task 3
Numbers = []
while True:
    Num = input("Enter a number (Break to exit): ")
    if Num == "":
        break
    Num = int(Num)
    Numbers.append(Num)
largest = Numbers[0]
for x in Numbers:
    if x > largest:
        largest = x
print(f'The largest number is {largest}')
smallest = Numbers[0]
for y in Numbers:
    if y < smallest:
        smallest = y
print(f'The smallest number is {smallest}')

#Task 4
import random
secret = random.randint(1, 10)
print("Guess the number between 1 and 10!")
while True:
    guess = int(input("Your guess: "))
    if guess < secret:
        print("Too low")
    elif guess > secret:
        print("Too high")
    else:
        print("Correct!")
        break

#Task 5
attempts = 0
while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == 'python' and password == 'rules':
        print("Welcome")
        break
    else:
        print("Wrong username or password")
        attempts += 1
if attempts == 5:
    print("Access denied")

#Task 6
def mid_char():
    char = input("Enter a word: ")
    length = len(char)
    mid = length // 2
    if length % 2 == 0:
        return char[mid - 1:mid + 1]
    else:
        return char[mid]
print(f'The middle character is: {mid_char()}')

#Task 7
def acronym(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        if word:
            result += word[0].upper()
    return result

user_phrase = input("Enter a phrase: ")
print(f'Acronym: {acronym(user_phrase)}')