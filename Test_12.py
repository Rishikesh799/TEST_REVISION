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
