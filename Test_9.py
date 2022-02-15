#TO check given number is armstrong or not

n=int(input("Enter the no to check armstrong :"))
i=n
s=0
while i>0:
    x=i%10
    s=s+x**3
    i=i//10
if n == s:
    print(n,"number is armstrong")
else:
    print(n,"not armstrong")
    ----------------------------------------------------------------------
#To check given no is prime or not
n=int(input("Enter the number:"))
co=0
for i in range(1,n+1):
    if n%i==0:
        co=co+1
if co==2:
    print(n,",The number is prime")
else:
    print(n,",number is not prime")
------------------------------------------------------------------------------------
#Check whether no is pallidrome or not
n=int(input("Enter the number:"))
i=n
s=0
while i>0:
    x=i%10
    s=s*10+x
    i=i//10
if n==s:
    print(n,"The number is pallidrome")
else:
    print(n,"The number is not pallidrome")
----------------------------------------------------------------------------------
#WAP to find the sum of digit of given number.
n=int(input("Enter the number:"))
i=n
s=0
while i>0:
    x=i%10
    s=s+x
    i=i//10
print("Sum of given number is",s)
