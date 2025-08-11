# Q - 8 Write a Python program to write multiple strings into a file.
multi = [
    "this is python\n",
    "this is good\n",
    "this topic is file handling"
]

file = open("strfile.txt","w")
file.writelines(multi)
