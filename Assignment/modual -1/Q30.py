# Q - 30  Write a Python program to demonstrate string slicing. 

str = "PythonProgramming"

# Slicing examples
print("Original string:", str)

# Slice from index 0 to 5 (not including 5)
print("Slice [0:5]:", str[0:5])      

# Slice from index 6 to the end
print("Slice [6:]:", str[6:])       

# Slice from beginning to index 5
print("Slice [:6]:", str[:6])        

# Slice with step of 2 (every second character)
print("Slice [::2]:", str[::2])     

# Slice in reverse
print("Slice reversed [::-1]:", str[::-1])  
