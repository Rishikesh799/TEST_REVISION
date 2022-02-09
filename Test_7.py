-------------------USE MAP FUNCTION-------------------------------------------
#WAP to square the number of list using the map function
l=[2,5,6,4]
print(list(map(lambda x:x**2,l)))
[4, 25, 36, 16]
-------------------------------------------------------------------------
#WAP to covert the all the chr in uppercase and lowercase and eliminate duplicate letters from given sequece
l=["a","b","e","f","A","i","O","u","a"]
y=set(l)
x=list(map(lambda x:(x.upper(),x.lower()),y))
print(x)
[('O', 'o'), ('I', 'i'), ('B', 'b'), ('U', 'u'), ('A', 'a'), ('E', 'e'), ('F', 'f'), ('A', 'a')]
------------------------------------------------------------------------
#WAP to convert the given list of tuples to a list of strings using map function.
l=["RED","GREEN","BLACK","BLUE"]
print(list(map(lambda x:list(x),l)))
[['R', 'E', 'D'], ['G', 'R', 'E', 'E', 'N'], ['B', 'L', 'A', 'C', 'K'], ['B', 'L', 'U', 'E']]
-------------------------------------------------------------------------
l=["RED","GREEN","BLACK","BLUE"]
d=[]
for i in l:
    d.append(list(i))
print(d)

--------------------------------------------------------------------------------
#WAP to count the same pair in two given list . use map
l=[1,2,3,4,5,6,7,8]
m=[2,2,3,5,5,7,7,9]
x=list(map(lambda i,j:i==j ,l,m)).count(True)
print(x)

-------------------------------------------------------------------------------
