#!/usr/bin/python3
#source: https://www.w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php

DEVELOPING = False
# 1. Divisible by 7 and Multiples of 5, between 1500 and 2700 (both included).
print("# 1. Divisible by 7 and Multiples of 5")

for n in range(1500, 2701):
    if(n % 7 == 0) and (n % 5 == 5):
            print(f"Number {n} is divisible by 7 and mutiple of 5")



print("\n\n")
# 2. Temperature Converter - [ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
print("# 2. Temperature Converter")

def temperatureConverter(degree, convention):
    if convention.upper() == "C":
        fahrenheit = int((degree * 9/5) + 32)
        print(f"{degree}ºC is {fahrenheit}ºF")
    
    elif convention.upper() == "F":
        celsius = int((degree - 32 ) * 5/9)
        print(f"{degree}ºF is {celsius}ºC")
    else:
        print("Not a valid temperature")

temp = '60C'
if DEVELOPING: temp = input("Input the temperature you'd like to convert (e.g., 45F, 102C etc.): ")
print()
tempNumber = int(temp[:-1])
tempConvention = temp[-1]
temperatureConverter(tempNumber, tempConvention)

del temp, tempConvention, temperatureConverter, tempNumber


print("\n\n")
# 3. Number Guessing Game
print("# 3. Number Guessing Game")


if DEVELOPING: pGuess = int(input("Guess what number between number 1 and 9 I'm thinking of: "))



guessed = False
import random
myGuess = random.randint(1,9)
if DEVELOPING: pGuess = myGuess

if DEVELOPING: 
    while not guessed:
        if pGuess == myGuess:
            break
        else:
            print("Wrong Number, try again!")
            pGuess = int(input("Guess what number between number 1 and 9 I'm thinking of: "))


print(f"Congrats, you guess was correct!, My number was {myGuess}")

try:
    del guessed, myGuess, pGuess
except:
    pass

print("\n\n")
# 4. Construct Pattern (Diamond Pattern)
print("# 4. Construct Pattern (Diamond Pattern)")


x = 5

def diamond():
    print("* ", end="")


for y in range(x):
    for j in range(y):
        diamond()
    print('')

for y in range(x, 0, -1):
    for j in range(y):
        diamond()
    print('')



del x

print("\n\n")
# 5. Reverse a Word
print("# 5. Reverse a Word")

word = 'yeah'
if DEVELOPING: word = input("Type a word, I'll reverse it: ")

print("The word reversed is: ", end='')

for char in range(len(word) -1, -1, -1):
    print(word[char], end='')
 


print("\n\n")
# 6. Count Even and Odd Numbers
print("# 6. Count Even and Odd Numbers")

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
evenCount = oddCount = 0
for x in numbers:
    if x % 2 == 0:
        evenCount+=1
    else:
        oddCount+=1

print(f"Number of even numbers : {evenCount}")
print(f"Number of odd numbers : {oddCount}")

del numbers, evenCount, oddCount

print("\n\n")
# 7. Print Items with Types
print("# 7. Print Items with Types")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for x in datalist:
    print(f"{x} is item type: {type(x)}")


print("\n\n")
# 9. Fibonacci Series Between 0 and 50 / Expected Output : 1 1 2 3 5 8 13 21 34
print("# 9. Fibonacci Series Between 0 and 50\n")

now = 1
then = 0

while then < 51:
    print(then)
    now, then = then, now + then

del now, then

print("\n\n")

# 10. FizzBuzz Variation from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and 
# for multiples of five print "Buzz". For numbers that 
# are multiples of three and five, print "FizzBuzz".

print("# 10. FizzBuzz Variation") # Why?


for x in  range(1,51):
    if( x % 3 == 0) and (x % 5 == 0):
        print("FizzBuzz")
        continue
    elif (x % 5 == 0):
        print("Buzz")
    elif ( x % 3 == 0):
        print("Fizz")
    else:
        print(x)







print("\n\n")
# 11. Two-Dimensional Array (Multiplication Table)
print("# 11. Two-Dimensional Array (Multiplication Table)")













print("\n\n")
# 15. Password Validity Checker
print("# 15. Password Validity Checker")












print("\n\n")
# 36. Triangle Type Checker
print("# 36. Triangle Type Checker")










print("\n\n")
# 37. Season Finder from Date
print("# 37. Season Finder from Date")










print("\n\n")
# 38. Astrological Sign Finder
print("# 38. Astrological Sign Finder")













print("\n\n")
# 41. Next Day Calculator
print("# 41. Next Day Calculator")










print("\n\n")
# 44. Nested Loop Number Pattern
print("# 44. Nested Loop Number Pattern")


