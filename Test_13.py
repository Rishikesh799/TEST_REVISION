#Program to print duplicates from list of integers
x=[10,20,30,20,20,30,40,50,-20,60,60,-20,-20]
d=[]
for i in x:
    if x.count(i)>1:
        d.append(i)
print(list(set(d)))
--------------------------------------------------------
