# Q - 2 Write a Python program to access elements at different index positions.

city = ['rajkot','junagadh','baroda','surat','ahemdabad','bhavnagar','morbi','jamnagar']

print(city[0])
print(city[1])
print(city[1:5])
print(city[1:])
print(city[:6])
print(len(city))
print(city[-1])

for i in range(len(city)):
    print(f"{i} : {city[i]}")

    