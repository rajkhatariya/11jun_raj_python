# Q - 9 ) Write a Python program to check the current position of the file cursor using tell().

file = open("cursorfile.txt","w")

file.write("this is python!")
position = file.tell()
print("the position is :",position)
