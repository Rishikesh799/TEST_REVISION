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
