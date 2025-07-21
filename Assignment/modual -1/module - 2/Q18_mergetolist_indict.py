# Q - 18  • Write a Python program to merge two lists into one dictionary using a loop. 


list1=['id','name','city']
list2=[1,'Raj','rajkot']

dict1={}

for i in range(len(list1)):
    dict1[list1[i]]=list2[i]


print(dict1)
