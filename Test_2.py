"""
QQQ=WAP accesing nth element from tuple in list

x=[(23,"rishi"),(24,"game")]
for i in x:
    print("The player name,",i[len(i)-1])

-------------------------------------------------------------------------------------------
QQQ=WAP to ind sum of all items in a dict.
x={"1":3,"5":6,"9":3}
d=[]
for i ,j in x.items():
    c=int(i)+j
    d.append(c)
print(sum(d))
-------------------------------------------------------------------------------------------
QQQ=WAP to check if a string has at least one letter and one number 
x="welcomeourcountry"
d=[]
e=[]
for i in x:
    if i.isalpha():
        d.append(i)
    elif i.isdigit():
        e.append(i)
if len(d)>0 and len(e)>0:
    print("True")
else:
    print("False")
-----------------------------------------------------------------------------------------
QQQ=WAP to find cumulative sum of list
x=[10,20,30,40,50]
d=[]
c=0
for i in x:
    c=c+i
    d.append(c)
print(d)
"""
