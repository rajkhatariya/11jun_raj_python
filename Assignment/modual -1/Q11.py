# Q - 11 Write a Python program to calculate grades based on percentage using if-else ladder.

s1=int(input("enter the marksh of sub 1 :"))
s2=int(input("enter the marksh of sub 1 :"))
s3=int(input("enter the marksh of sub 1 :"))
s4=int(input("enter the marksh of sub 1 :"))

total = s1+s2+s3+s4
pr=total/4

print("the total is :",total)
print("the precantage is :",pr)

if pr>=70:
    print("the grade is A")
elif pr>=60:
    print("the grade is B")
elif pr>=50:
    print("the grade is C")
elif pr>=40:
    print("the grade is D")
else:
    print("fail")
