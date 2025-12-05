#!/usr/bin/python3
import time
# <- Used to Comment
# Syntax defines a set of rules that are used to create a Program.
# Python Syntax have has many similarities to Perl, C, and Java Programming Languages.
# However, there are some definite differences between the languages.
# Python is an iterpreted language (But it can be compiled)

# To enter Python interavtive Mode from Terminal (or prompt) use 'python3'
# Basic Syntaxes

print("Hello world!") # Bless the first print ever
time.sleep(1)
print("# Starting with Python Basic Syntaxes")

time.sleep(2)
print() # Used to give space to text and give context

print("Here we can write thing we want the program to...")
time.sleep(1)
print("print")
time.sleep(2)
print()

print("By default, on the end of all pythons 'prints' there's this regex '\\n'") # \n
time.sleep(2)
print()

print("But of course we can change it using 'args', basically we say 'end='XXX'' where XXX is the new regex or word, character, you choose")
print("It also need a comma between the real text, ex:  print(\"original text\", end='I know Python')")
time.sleep(3)
print()

print("To test it, let's use 'I know Python' on the end", end='I know Python')
print("But... we are TOO CLOSE")
time.sleep(3)
print()

print("Removing the normal '\\n' makes the next one to print together with the first, so we may need to use spaces, like so")

print("To test it, let's use 'I know Python' on the end ", end='I know Python ')
print("But... we are still CLOSE")
time.sleep(3)
print()

print("This can be used better with regex or when intentionally leaving things for the user to read")
print("That way, we can use variables and not repeat code or prints...")

time.sleep(3)
# As we start with this, i'll change the some to include a sleep (time.sleep()), everything just trowing this is strange
# Done

# Starting with Python Identifiers
print("# Starting with Python Identifiers",end="\n\n")
time.sleep(3)
# A Python identifier is a name used to identify a variable, function, class, module or other object.
# An identifier starts with a letter A/a to Z/z or an underscore (_) followed by zero or more letters, underscores and digits (0 to 9).
# Python does not allow punctuation characters such as &commat;, $, and % within identifiers.

# We also have NAMING CONVERNTIONS for Python identifiers

# Python Class names start with an uppercase letter. All other identifiers start with a lowercase letter. -> def Function():
# Starting an identifier with a single leading underscore indicates that the identifier is private identifier. -> def _PrivateFunction():
# Starting an identifier with two leading underscores indicates a strongly private identifier. -> def __VeryPrivateFunction():)
# If the identifier also ends with two trailing underscores, the identifier is a language-defined special name. -> def __Start__():

print("Python Identifiers are variables and classes (ultimately identifiers) that we set or are already set",end="\n\n")

print("These are created functions:")

print("Normal identifier -> Function // Starting with capital letter",end="\n\n")
time.sleep(1)

print("Private identifier -> _Function // Starting with underscore AND capital letter",end="\n\n")
time.sleep(1)

print("VERY private identifier -> __Function // Starting with 2 underscore AND capital letter",end="\n\n")
time.sleep(1)

print("Intern python identifiers -> __start__  // These are from python identifiers, not created by the user",end="\n\n")

time.sleep(2)


# Python Lines and Identantion... we are already kind of using the Lines and Identation is easy

# So we are going fast Here

print("# Python Lines and Identantion",end="\n\n")
time.sleep(2)

print("On python, we get to write everyhing on it's own lines, don't mix both functions on the same line")
time.sleep(1)

print("Going to idententions, you will have to see the code on this .py",end="\n\n")

if True:
    print("We are inside a True if condition using the correct identention")
else: 
    print("We are inside a True if condition that will never execute because we are on the else part (Meaning, we are not True)")

time.sleep(1)


if True:
   print ("We can get everything inside the condition ")
   print ("Only IF they are typed correctly",end="\n\n")
else:
   print ("well...")
   print ("we are the else")

# Multi-Line statements

time.sleep(3)

print("We also have Multi-Line Statements, we will go trought via code too")
print("We will also starting using variables")
time.sleep(1)

print("Essentialy, variables are objects that we can assign values")


onePrint = "One"
twoPrint = "Two"
threePrint = "Three"

toPrint = onePrint + \
            twoPrint + \
            threePrint

print("toPrint have all the others variables and use a multi-line statements")
time.sleep(1)
print()
print("We can bassically do it with many types of variables")
print("Let's print it to see everything is correct")
time.sleep(1)
print()
print(toPrint)
print()

days = ['Monday', 'Tuesday', 
        'Wednesday',
        'Thursday', 'Friday']

print("Like so, when using [], () and {} we don't have to use \\ to separate it ")

time.sleep(3)


# Quotations 

print("#Quotations in Python",end="\n\n")

time.sleep(2)

print("We can use various types of quotations, be it \"   \' or \"\"\" ")
time.sleep(1)

print("normaly we use double quotations (\"MESSAGE\") and inside it, we can use this \'MESSAGE\' ")
time.sleep(1)

print("and we also have \"\"\"MESSAGE\"\"\", the difference is, we use for paragraphs",end="\n\n")

"""
It can also be used to comment on codes
not only when printing
and that's fun
"""

'''
This is also a
Multi-Line comment,
funny right?
'''


print("""We can use it,
      on prints,
      variables
      and 
      comments on code
      like this
      """)

time.sleep(3)

print("There's also the possibility to have multiple Statements on a single Line using ; "); print("Like this"); 

time.sleep(1)

print("So, these are the basics Syntaxes, next we will use Varuables and Data Types")
print()

print("Thank you!")