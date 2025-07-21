# Q - 8   Write a Python program to insert elements into an empty list using a for loop and append(). 

city = []

n=int(input("how many element do you want to add :"))

for i in range(n):
    city_name = input(f"enter the city name :{i+1}")
    city.append(city_name)



print("final list :",city)


    

