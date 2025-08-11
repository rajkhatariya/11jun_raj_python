# Q - 28 Write a Python program to match a word in a string using re.match().

import re

text = "Python is a powerful programming language."

word = "Pyth"

if re.match(word, text):
    print(f"'{word}' matched  the the string!")
else:
    print(f"'{word}' did not match  the the string.")
