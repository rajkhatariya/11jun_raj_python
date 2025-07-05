# Q - 12 Write a Python program to check if a person is eligible to donate blood using a nested if.

age = int(input("enter your age :"))
wight = float(input("enter your wight :"))

if age>=18:

    if wight>=50:
        print("your are aligable to donate blood")
    else:
        print("your are no aligable to doante blood because your wight is less than 50")
        
else:
    print("you are not eligible to donate blood because your age is less than 18")

