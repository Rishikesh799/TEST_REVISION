##Convert chr of matrix into string
x=[["g","f","g"],["i","s"],["b","e","s","t"]]
d=[]
for i in x:
    d.append("".join(i))
print(str("".join(d)))
---------------------------------------------------------------------
##Python programs replace all chr of a list except the given chr.
x=["G","F","G","I","S","E","S","T"]
v=["*"]
y=["G"]
d=[]
for i in x:
    if i != "G":
        d.append("*")
    else:
        d.append(i)
print(d)
------------------------------------------------------------------------------------
x=["G","F","G","I","S","E","S","T"]
v=["*"]
print(["*" if i!="G" else i for i in x])
---------------------------------------------------------------------------------------------
##Python program to find the chr position of kth word from a list of strings.
x=["geekforgeeks","is","best","for","geeks"]
k=15
d=[]
for i in enumerate(x):
    for j in enumerate(i[1]):
        d.append(j[0])
print(d[k])
--------------------------------------------------------------------------
##Remove the words list of chr.
x=["gfg","is","best","for","geeks"]
y=["g","o"]
k=[]
for i in x:
    for j in y:
        if j in i:
            break
    else:
        k.append(i)
print(k)
