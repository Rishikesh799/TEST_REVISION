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

------------------------------------------------------------------------
#WAP to convert the given list of tuples to a list of strings using map function.
l=["RED","GREEN","BLACK","BLUE"]
print(list(map(lambda x:list(x),l)))

-------------------------------------------------------------------------
