#!/usr/bin/python3
import time
# So, let's get to Variables and Data Types?

wordType = "I'm a string"
wordsType = "I'm also a string"

numberType = 42

floatType = 3.14

arrayType = ["one", "two", "Three"]

dictionaryType = {1: "first", 2: "second", 3: "third"}

class ClassType: pass

instanceType = ClassType()

print("So, the left side is called a variable, capable of storing a value, the right side is called value",end="\n\n")
time.sleep(2)

print("Beware, this will be big")
time.sleep(2)

print(f"""Here I'll show you the type and the value,
      
wordType:
type: {type(wordType)}
value: {wordType} 

wordsType:
type: {type(wordsType)}
value: {wordsType} 

numberType:
type: {type(numberType)}
value: {numberType} 
        
floatType:
type: {type(floatType)}
value: {floatType} 
        
arrayType:
type: {type(arrayType)}
value: {arrayType} 
        
dictionaryType:
type: {type(dictionaryType)}
value: {dictionaryType} 
        
ClassType:
type: {type(ClassType)}
value: {ClassType} 
        
instanceType:
type: {type(instanceType)}
value: {instanceType} 

""")

time.sleep(2)
print("That was huge, there's plenty of types ")
time.sleep(3)

print("We can also change the values on these variables, we just assign them like is the first time",end="\n\n")

print("Before:", wordType)
wordType = "Still a string but longer"
time.sleep(2)
print("After:", wordType)
time.sleep(2)

print("We can do it with other types and change types midway")
time.sleep(2)

age = 20
print(f"This is my age {age} and ageType {type(age)}")
time.sleep(2)
age = "twenty"
print(f"This is my new age {age} and new ageType {type(age)}")
time.sleep(2)

print()
print("We can also do operations, be it with +, -, /, *, ** (Exponentiation), % (Remainder of a division) and // (Floor division)")
print()




