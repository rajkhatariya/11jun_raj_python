# Q - 32 Write a Python program to apply the map() function to square a list of numbers. 


def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(square, numbers))

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)
