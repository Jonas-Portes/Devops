#!/usr/bin/python3
import time
# So, let's get to Variables and Data Types?

print("Here we will see Variables, Data Types and some other things")

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
time.sleep(3)

print(f"""Here I'll show you the type and the value,
      
wordType:
type: {type(wordType)} // value: {wordType} 

wordsType:
type: {type(wordsType)} // value: {wordsType} 

numberType:
type: {type(numberType)} // value: {numberType} 
        
floatType:
type: {type(floatType)} // value: {floatType} 
        
arrayType:
type: {type(arrayType)} // value: {arrayType} 
        
dictionaryType:
type: {type(dictionaryType)} // value: {dictionaryType} 
        
ClassType:
type: {type(ClassType)} // value: {ClassType} 
        
instanceType:
type: {type(instanceType)} // value: {instanceType} 

""")


time.sleep(2)
print("That was huge, there's plenty of types ")
time.sleep(3)

print("We can also change the values on these variables, we just assign them like is the first time",end="\n\n")

print("Before:", wordType)
wordType = "Still a string but longer"
time.sleep(2)
print("After:", wordType,end="\n\n")
time.sleep(2)

print("We can do it with other types and change types midway")
time.sleep(2)

age = 20
print(f"This is my age {age} and ageType {type(age)}")
time.sleep(2)
age = "twenty"
print(f"This is my new age {age} and new ageType {type(age)}",end="\n\n")
time.sleep(2)


print("We can also do operations, be it with +, -, /, *, ** (Exponentiation), % (Remainder of a division) and // (Floor division)",end="\n\n")


print("We can calculate things on print and also on variables, like so (we are using 10 for the operations)")

addition = 10 + 10
subtraction = 10 - 10
multiplication = 10 * 10
exponentiation = 10 ** 10
division = 10 / 10
remainderDivision = 10 % 10
floorDivision = 10 //10

print(f"""
These are the results:
addition: {addition}
subtraction: {subtraction}
multiplication: {multiplication}
exponentiation: {exponentiation}
division: {division}
remainderDivision: {remainderDivision}
floorDivision: {floorDivision}
""")    
time.sleep(3)
print("Just as demonstration, 10 + 10 is:", 10+10)
time.sleep(1)

print("We also use variables as Counters, so we know where we are in a loop")
time.sleep(2)
print("For example",end="\n\n")
time.sleep(2)


ten_counter = 0        
while True:
    if(ten_counter <= 5):
        print(f"We are in the loop for the {ten_counter} time")
        time.sleep(1)
        ten_counter += 1
        pass
    else:
        break

print("\nCounter can be incremented in various ways")
time.sleep(2)

print("Be it using 'variable += number' 'variable = OPERATOR number' 'variable = OPERATOR VARIABLE'",end="\n\n")
time.sleep(2)

print("We have two types of variables, global and temporary, globals are defined outside loops and functions")
time.sleep(2)
print("Temporay variables are defined inside loops or functions, they exists until the function is finished or exiting the loop",end="\n\n")
time.sleep(2)

global_string = "I'm global"
def functionEX():
    temp_string = "I'm temporary"
try:
    print(temp_string) # type: ignore
except:
    pass

print("I can print variable global_string but I can't even print temp_string")
print(global_string,end="\n\n")
time.sleep(3)

print("There's boolean flags too, True or False, we can use it to safeproof function and only allow somethiing if it's true")
time.sleep(1)
print("I've used the True statement to utilize the loop as you can se above",end="\n\n")

print("As another example:",end="\n\n")

toggle = True
for y in range(2):
    if toggle:
        print(f"Toggle is {toggle}")
    else:
        print(f"Toggle is {toggle}")
    toggle = not toggle
time.sleep(3)


print("\n\nThere's a way to use functions with the prints, but with limitations")
print("I'll show it using another print")
time.sleep(2)

def greet(verbose = False):
    if verbose:
        print("We are using verbose True here")
    else:
        print("We are False here")

greet()
time.sleep(2)

greet(verbose = True)
time.sleep(2)
print()

print("As for built-in functions, we can sort numbers")
time.sleep(2)

print(sorted([3,2,8,4,1,6,8,22,99,9,32]),end="\n\n")
time.sleep(2)

print("We can reverse it too")
time.sleep(2)

print(sorted([3,2,8,4,1,6,8,22,99,9,32], reverse=True))
time.sleep(3)
print("\n\n")

print("I'll present now some other operations as well")

print("So, True and False with comparations")
time.sleep(3)

age = 21
is_adult = age > 18

if(is_adult):
    print(f"We are adults, the statement is {is_adult}")
if(not is_adult):
    print(f"We are not adults, the statement is {is_adult}")
time.sleep(2)
print("\n\n")

print("There's also loop with variables")
time.sleep(3)


colors = [
     "red",
     "orange",
     "yellow"
     ]

for color in colors:
     print(color)
print()
time.sleep(3)

print("Now we'll see some about ditcs, sets in general")

contacts = [
    ("Linda", "111-2222-3333", "linda@example.com"),
    ("Joe", "444-5555-6666", "joe@example.com"),
    ("Lara", "7777-8888-9999", "lara@example.com"),
]
for contact in contacts:
    print(contact)

print("\n\n")
time.sleep(3)
print("With this, we can go around the contacts, but there's everything together, let's strip this thing")
print("\n\n")
time.sleep(2)

print("Let's start with giving a name to those variables, we have 3 datas, lets name them espectively")
time.sleep(2)
print("\n\n")
print("Name, Phone and Email, we will only print the name and phone here")

for name, phone, email in contacts:
    print(name, phone)

print("\n\n")


print("We will go a bit about matrix right now")
time.sleep(2)
print("Basically, we make tuples together")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for i in matrix:
    for j in i:
        print(f"Matrix number: {j}")
        time.sleep(1)

print("\n\n")

print("Working with Public and Non-Public variables names")
print("")
time.sleep(2)

_timeout = 30

print(f"Use them in functions")

def get_timeout():
    return _timeout

print(f"We can print them: {_timeout}")

print("But a non-public variable is a variable that shouldn't be used outside its defining module")

time.sleep(3)
print("\n\n")

print("Variables can use type hints")

# variable: data_type = value

number: int = 30

print(f"Number we defined: {number}")
time.sleep(2)
print("This way, you can define specifically what type you want without mixing double, int and everything else")
print("\n\n")
print("When working with list, tuples, dicts and sets things can get messy, but with these hints it's easier to manage, know and define the types correctly")


colors: dict[str, tuple[int, int, int]] = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
}

print()
print("These types can get new values appending the list or delete it poping it")

array = ["type", "theType"]
print("Original array:", array)
time.sleep(2)

array.append ("The Hype Type")
print("Appended array:", array)
time.sleep(2)


array.pop(2)
print("Popped array:", array, end="\n\n")
time.sleep(3)


print("Parallel assignment", end="\n\n")

print("Python allows you to run multiple assignments using a single line, which makes it easier to preset some values")
time.sleep(2)

is_adult = is_logged = is_mobile = False

print("Here, we've set 3 variables as False\n")


print(f"is_adult = {is_adult}, is_logged = {is_logged}, is_mobile = {is_mobile}")
time.sleep(2)

print("This is usefull when resetting a program or just assigning mutiple things in one line", end="\n\n")
time.sleep(2)

print("We can set other variables using the list from before")

# Remember contacts? no? it's here just to refresh our memory

contacts = [
    ("Linda", "111-2222-3333", "linda@example.com"),
    ("Joe", "444-5555-6666", "joe@example.com"),
    ("Lara", "7777-8888-9999", "lara@example.com"),
]

person = ("Lara", "7777-8888-9999", "lara@example.com")

print("Every value inside a list has it's own index, and we use this index to attribute the value")
time.sleep(2)

name = person[0]
number = person[0]
email = person[0]

print(f"Name: {name}, number: {number}, email: {email}", end="\n\n")
time.sleep(2)

print("We have done this before using a loop, here I'm just demonstrating that we can assign these manually one by one")
time.sleep(3)

print("Also, as we used on the for loop, we can assign recpectively")
time.sleep(2)

person = ("Robert", "1234-1234-9999", "robert.jr@example.com")

name, number, email = person

print(f"Name: {name}, number: {number}, email: {email}", end="\n\n")
time.sleep(2)

contacts = [
    ("Linda", "111-2222-3333", "linda@example.com"),
    ("Joe", "444-5555-6666", "joe@example.com"),
    ("Lara", "7777-8888-9999", "lara@example.com"),
]

print("It's possible to do it with matrix too")
time.sleep(2)

name, number, email = contacts[1] # We use 1 here because we want to show the second list, Joe information

print(f"Name: {name}, number: {number}, email: {email}", end="\n\n")
time.sleep(3)


# User input

print("We can have the user make inputs too, this way we can manipulate data" \
"an the user can interact with the program." \
"Right now we'll see inputs from CMD/terminal")

user_input = input("Type some text here: \n\n")

print(f"As you've seen, the programs waits to read the user input, you wrote: {user_input}", end="\n\n")
time.sleep(3)



# Loops, we have seen some for and while


print("There's a lot we can talk about loops, right now we will cover assigning expressions" \
"A 'while' loop runs until the first set condition is break." \
"A 'for' loop runs until is has finished the first set condition", end="\n\n")
time.sleep(3)

user_input = input("Type some text here: ")
user_input_list =[]

while user_input != "stop":
    print(f"you wrote: {user_input}")
    user_input = input("Type some text here: (text 'stop' to break the loop)")
    user_input_list.append(user_input)

print()
print("Everything you wrote was showed and stored within the loop, and you broke the loop with 'stop'" \
"Still, there's another way you can write the code above", end="\n\n")
time.sleep(3)

user_input = ""

while (user_input := input("Type some text here: (text 'stop' to break the loop)")) != "stop":
    print(f"you wrote: {user_input}")
    user_input_list.append(user_input)   


print("I's a bit shorter and we use new expressions, ':=' means that the key variable is set and comparared with it's outside the parentheses" \
"Meanwhile, '!=' means different, this way we have the same logic from the other code, but with expressions and sometimes, wirting this way can make the code runs faster")
time.sleep(3)



# Modular code, Scopes

print("Right now we will use here another piece code that's in another file")
time.sleep(2)

print("The file is called 'config.py' there's some settings there and we need it here." \
"So, we will import it 'like' I've been doing with time.sleep()")
time.sleep(3)

from config import settings

print("The import is different because we are only importing one variable, we can use it to import everything we write to, not just variables")
time.sleep(3)

print(f"We can call it like it was defined here: {settings["background"]}")
time.sleep(2)

print("Let's import some functions too, two in one line")
time.sleep(3)

from config import cars, plane

cars("Buggati")
plane()

print("As seen, we can use and even pass args trough them, the code was executed trough another script and anything that was set there won't be stored here.")
time.sleep(3)

# OOP -> Object Oriented Programming

print("Now we've come to a complicated topic, OOP, meaning Object Oriented Programming." \
"Here we will instantiate classes and initialize other things")
time.sleep(3)

print("Let's import a employ function from 'employees' and set some employees while instantiating the class")
time.sleep(1)


from employees import Employee

marcus = Employee("Marcus Rich", "Software Engineer", 30000)
robert = Employee("Robert Poor", "DataCenter Operator", 10000)

print("We have a display_profile function inside the class, let's see if what we did work.")
time.sleep(1)

marcus.display_profile()
robert.display_profile()

print("""Everything is working fine, the class was imported and instantiate, 
we can use functions here from another code and we are saving only what we need.\n""")
time.sleep(3)

print("Also, inside the class we have made a counter to keep track of our employees, we can also call that.")
time.sleep(2)

print(f"Total employees: {Employee.count}")
time.sleep(2)

print("""We can only call the Class directly when we are using variables from that code, like we did with the 'count'.
On the same not, we can actually call the 'count' from everything that uses that class, for example, we call call count using marcus or robert, meanwhile they are separated variables, we can modify as we see fit.
""")
time.sleep(4)

print(f"Marcus Count: {marcus.count}")
print("Then modify to 300")
marcus.count = 300
time.sleep(3)

print(f"Marcus Count: {marcus.count}")
print("Meanwhile, on robert or Employee")
time.sleep(3)


print(f"Robert Count: {robert.count}")
print(f"EmployeeClass Count: {Employee.count}\n")

print("As Marcus count is not linked anymore, when  we change EmployeeClass count, only the Class and the Robert will change")
time.sleep(3)


print(f"Marcus Count: {marcus.count}")
print(f"Robert Count: {robert.count}")
print(f"EmployeeClass Count: {Employee.count}\n")
time.sleep(3)


print("As we are finished here, let's show the last thing about Variables here, the Delete function")

print("I can't really show it without breking the code, but with the 'del' function we can delete our variables")
time.sleep(2)

del marcus

print("Deleting here only makes the variable inaccessible and free the memory, the class won't refresh the Employees count")
time.sleep(2)

print(f"EmployeeClass Count: {Employee.count}")

print("We can delete mutiple vars on the same line, even classes")
time.sleep(1)

del robert, Employee, wordType, contact, contacts, color, is_adult, age, y, toggle, global_string, ten_counter, floorDivision, remainderDivision, division, exponentiation, multiplication, subtraction, addition, instanceType, dictionaryType, arrayType, floatType, numberType, wordsType, settings, user_input_list, user_input, email, number, person, is_mobile, is_logged, array, _timeout, j, i, matrix, phone, name

print("It's possible to delete even functions and everything imported")

del functionEX, ClassType, time

print("We don't need to delete all variables vefore finishing a program, but we can use it so it won't be used anymore")
print("Well, see you next time!")

