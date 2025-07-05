# Q - 17  Write a generator function that generates the first 10 even numbers.

def even_num():
    num = 2
   
    while num <= 20:
        yield num
        num += 2

for even in even_num():
    print(even)
    
