# Q - 5 Write a Python program to open a file in write mode, write some text, and then close it. 

file = open("file1.txt","w")
file.write("hello this is first file")
file.close()

print("Text written to example.txt successfully.")