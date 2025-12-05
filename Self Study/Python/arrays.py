#!/usr/bin/python3
# Lists, Tuples, Sets and Dictionaries
# Let's begin

# Those as collections -> single "variable" used to store mutiple values
"""
List    = []    Ordered and changeable. Can duplicate.
Set     = {}    Unordered and immutable. Can add/remove. Cannot duplicate
Tuple   = ()    ordered and unchangeable. Can duplicate. Faster
"""

numbers = [1, 2, 1 , 12, 1, 2, 3, 4, 5, 5, 4, 8, 7, 12]
first = set(numbers)
second = {1, 42, 22, 10}
second.add(7)
second.remove(22)

print(f"Uniques: {first}, lenght: {len(first)}", end="\n\n")
print(f"Second: {second}, lenght: {len(second)}", end="\n\n")

# Starting with sets

set_union = (first | second) # Union of both sets
print("union", set_union, end="\n\n")

intersection = (first & second) # Are in both sets
print("intersection", intersection, end="\n\n")

difference = first - second # Removin the second set from the first
print("Difference", difference, end="\n\n")

unique_numbers = first ^ second # Are in only one of both
print("Unique Numbers between Sets", unique_numbers, end="\n\n")


if 12 in first:
    print("1 is there", end="\n\n")

# Sets are good in comparations between arrays

import random
for i in range(20):
    tmp = random.randint(0,15)
    second.add(tmp)
    print("The number added was", tmp)

print(second)
print("\n\n\n")



user_input = set()

try:
    while True:
        _user_input = int(input("Type which permissions do you want?(1, 2, 3, 4, 5 type one at a time, type a letter to finish): \n"))
        user_input.add(_user_input)
except:
    print("You have typed a letter, finishing set")


adm_set = set({0, 6, 7, 8, 9, 10, 11})

if(len(adm_set.intersection(user_input))) >= 1:
    print(f"This is an ADM permission, you can't have {adm_set.intersection(user_input)} permission ID")
else:
    print("Welcome, you are logged")



  


# Tuples

fruits = ("apple", "orange", "banana", "coconut", "strawberry","coconut")

print(fruits)

print("strawberry" in fruits)

print("THERE's this many coconuts:", fruits.count("coconut"))

print(fruits.index("orange"))

