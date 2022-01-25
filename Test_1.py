
"""--------- TEST  ON PYTHON BASICS PROBLEM---------------------------------------------------------------------
QQQ==Python programs to find uncommon words from two strings.
a="geeks for geeks"
b="learning from geeks for geeks"
x=a.split()
y=b.split()
print(list(set(y).difference(set(x))))
--------------------------------------------------------------------
QQQ==Pyhton program replace all chr of a list Except the given chr

x="G"
a=["G","F","G","I","S","B","E","S","T"]
d=[]
for i in a:
    if i == "G":
        d.append(i)
    else:
        d.append("*")
print(d)
---------------------------------------------------------------------
QQQ===Write python program to remove an empty tuple from list of tuple.



a=[(),(),("",),("a","b"),("a","b","c"),("d",)]
d=[]
for i in a:
    if len(i) == 0:
        pass
    else:
        d.append(i)
print(d)
----------------------------------------------
QQQ==Python program to find common elements in three lists .


a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]
d=[]
for i in a:
    for j in b:
        for k in c:
            if i == j == k:
                d.append(i)
print(d)
----------------------------------------------------------------------
QQQ==Covert list of list to dict.

a=[["a","b","1","2"],["c","d","3","4"],["e","f","5","6"]]
d = {}
for i in a:
    d[tuple(i[:2])]=i[2:]
print(d)
"""













