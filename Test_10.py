#Check whether number is perfect number or not.

n=int(input("Enter the number"))
d=[]
for i in range(1,n):
    if n%i==0:
        d.append(i)
if n==sum(d):
    print(n,"Perfect number")
else:
    print(n,"not perfect number")
