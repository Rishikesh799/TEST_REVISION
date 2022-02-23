#Program to print duplicates from list of integers
x=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
d=[]
for i in x:
    if x.count(i)>1:
        d.append(i)
print(list(set(d)))
--------------------------------------------------------
#Replace index elements with elements in other list.
x=["gfg","is","best"]
y=[0,1,2,1,0,0,0,2,1,1,2,0]
d=[]
for i in y:
    d.append(x[i])
print(d)
--------------------------------------------------------------
