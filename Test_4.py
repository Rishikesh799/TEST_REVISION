"""
def num(x,y):
    for i in range(x,y+1):
        if i % 7 == 0 and i % 5 == 0:
            print(i,end=" ")
num(1500,2700)
---------------------------------------------------
x=["abc","xyz","aba","1221"]
d=[]
for i in x:
    if len(i)>2:
        if i[0]==i[len(i)-1]:
            d.append(i)
print(len(d))
---------------------------------
x = [25,62,12,35,89]
x.sort()
print(x)
print(x[len(x)-2])
----------------------------------------
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
def dicc(*x):
    d={}
    for i in x:
        d.update(i)
    print(d)
dicc(d1,d2,d3)
---------------------------------------------------------
x=["Black","Red","Maroon","Yellow"]
y=["#0000","FF662","#80000","#FFF00"]
print([{"colour":i,"code":j} for i,j in zip(x,y)])
"""
