#check whether number falls in a given range by using function

def ran(n):
    if n in range(1,10):
        print(n,"Is present in a range.")
    else:
        print(n,"Not in range.")
k=int(input("Enter the number :"))
ran(k)
----------------------------------------------------------------------------------------------------
#WAP fuction that accept a string and calculate the number of upper case letters and lower case letter.
s=input("Enter the string:")

def stru(z):
    c=0
    k=0
    for i in s:
        if i.isupper():
            c=c+1
        elif i.islower():
            k=k+1
    print("NO of upper case letter is,",c)
    print("No of lower case letter is,",k)
stru(s)
------------------------------------------------------------------------------
#WAF that takes alist and return a new list with unique elements.
def uni(x):
    y=set(x)
    print("Unique ist is ,",list(y))
d=[]
n=int(input("Enter how many no do you want in list"))
for i in range(n):
    m=int(input("Enter the number:"))
    d.append(m)
uni(d)
