"""
d={"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","0":"zero"}
x = 456987
for i in str(x):
    if i in d:
        print(d[i],end=" ")
-----------------------------------------------------------------------
d={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
x="two three four"
for i in x.split():
    if i in d:
        print(d[i],end="")

-------------------------------------------------------------------------
s="geeksforggeks is best for geeks"
c=s.split()
x="best"
y=c.index(x)
print(y)
---------------------------------------------------------------------------
x="geeksforgeeks"
a=7
y=x[a:]+x[:a]
print(y)
b=3
z=y[len(y)-b:]+y[:len(y)-b]
print(z)
--------------------------------------------------------------------

x=["geeksforgeeks","is","bessset","for","geeks"]
a="s"
y=sorted(x,key=lambda i:i.count(a),reverse=True)
print(y)

---------------------------------------------------------------------
x=["a","e","i","o","u"]
a="aeiounjkl"
c=0
y=a.lower()
for i in x:
    if i in y:
        c=c+1
    if c==5:
        print("str contain all vowels",a)
"""



