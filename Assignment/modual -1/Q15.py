# Q - 15   Write a Python program to find a specific string in the list using a simple for loop and if condition.

citys = ['rajkot','junagadh','baroda','ahemadabad','surat','porbandar']

find_city = input("enter the city name :")

for city in citys:
    if "rajkot" in citys:
        print("True")
        break
    else:
        print("false")
        break
