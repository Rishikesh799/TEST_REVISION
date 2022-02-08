-----------------------------------------------------------------------------------
#write apython program to shuffle and print a specified list
from random import shuffle
c=["red","pink","blue","green","black"]
shuffle(c)
print(c)
['pink', 'red', 'green', 'blue', 'black']
-----------------------------------------------------------------------------------------
#wap to get the diff between the two list
l=[1,3,5,7,9]
k=[1,2,4,6,7,8]
def diff(x,y):
    j=set(x)
    i=set(y)
    print(list(j.symmetric_difference(i)))
diff(l,k)
[2, 3, 4, 5, 6, 8, 9]
------------------------------------------------------------------------------
