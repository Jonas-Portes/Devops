#!/usr/bin/python3
n = 7

x = 7

addition = n + x
subtraction = n - x

multiplication = n * x
exponentiation = n ** x
division = n / x
remainderDivision = n % x
floorDivision = n //x


print(f"""
These are the results:
multiplication: {multiplication}
exponentiation: {exponentiation}
division: {division}
remainderDivision: {remainderDivision}
floorDivision: {floorDivision}
""")  


for n in range(1500, 2701):
    if( n % 7 == 0):
        if(n % 5 == 0):
            print(f"Number is {n} divisible by 7 and mutiple of 5")