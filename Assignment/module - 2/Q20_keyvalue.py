# Q - 20  ) Write a Python program to separate keys and values from a dictionary using keys() and values() methods.

dict1={

    'id':101,
    'name':'Raj',
    'city':'Rajkot',
    'subject':'python',
    'cource':'mca',
    'gender':'male'

}

key1 = list(dict1.keys())
values1 = list(dict1.values())

print(key1)
print(values1)
