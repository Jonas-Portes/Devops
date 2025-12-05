#!/usr/bin/python3
# dictionarys = collection of {key:value} pairs.
# Ordered anc changeable. No duplicates

dic0 = {
    "id": 126548,
    "age": 22,
    "weight": 80,
    "feet": 37,
    "house": 1
}

print("\n")
# Problem: Sort Dictionary by Value
print("# Problem: Sort Dictionary by Value")

sortedDic0 = sorted(dic0.items(), key=lambda item: item[1])
ordenDic0 = dict(sortedDic0)
print("R: ", ordenDic0)

del ordenDic0, sortedDic0


print("\n")
# -----------------------------------------------------------------
# Problem: Add Key to Dictionary
print("# Problem: Add Key to Dictionary")

dic0.update({"cats": 2})
print("R: ", dic0)

print("\n")
# -----------------------------------------------------------------
# Problem: Concatenate Dictionaries
print("# Problem: Concatenate Dictionaries")

dic1 = {
    1:10, 
    2:20
}

dic2 = {
    3:30, 
    4:40
}

dic3 = {
    5:50,
    6:60
}


concDics = dic1.copy()
concDics.update(dic2)
concDics.update(dic3)

print("R: ", concDics)

del concDics


print("\n")
# -----------------------------------------------------------------
# Problem: Check Key Existence in Dictionary
print("# Problem: Check Key Existence in Dictionary")

checker = "age"

def checkFunc():
    if(dic0.get(checker)):
        print("R: This key is valid!")
    else:
        print("R: This key is not valid")
        
        

checkFunc()
checker = "europe"
checkFunc()

del checker, checkFunc

print("\n")
# -----------------------------------------------------------------
# Problem: Iterate Over Dictionary Using For Loops
print("# Problem: Iterate Over Dictionary Using For Loops")

for key, value in dic0.items():
    print(f"R: Key: {key} and Value: {value}")


print("\n")
# -----------------------------------------------------------------
# Problem: Generate Dictionary of Numbers and Their Squares
print("# Problem: Generate Dictionary of Numbers and Their Squares")



n = 10
dic4 = dict()

for x in range(1, n + 1 ):
    dic4[x] = x * x

print("R: ", dic4)

del dic4, n 

print("\n")
# -----------------------------------------------------------------
# Problem: Dictionary with Keys 1 to 15 and Their Squares
print("# Problem: Dictionary with Keys 1 to 15 and Their Squares")

dicSquares = dict()

for x in range(1,16):
    dicSquares[x] = x * x
    

print("R: ", dicSquares)

del dicSquares



print("\n")
# -----------------------------------------------------------------
# Problem: Merge Two Python Dictionaries
print("# Problem: Merge Two Python Dictionaries")

merged = dic0.copy()
merged.update(dic1)

print("R: ", merged)


print("\n")
# -----------------------------------------------------------------
# Problem: Remove a Key from a Dictionary

print(dic0)

dic0.pop("age")
print(dic0)

