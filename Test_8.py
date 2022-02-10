#Wap to sort list of tuples using lambda.
x=[("english",88),("science",90),("maths",97),("social sccience",82)]
print(sorted(x,key=lambda x:x[1],reverse=False))
[('social sccience', 82), ('english', 88), ('science', 90), ('maths', 97)]
-----------------------------------------------------------------------------------------
#wap to sort list of dict using lambda
x=[{"make":"nokia","model":216,"color":"black"},{"make":"mimax","model":2,"color":"gold"},{"make":"samsung","model":7,"color":"blue"}]
print(sorted(x,key=lambda x:x["model"]))
[{'make': 'mimax', 'model': 2, 'color': 'gold'}, {'make': 'samsung', 'model': 7, 'color': 'blue'}, {'make': 'nokia', 'model': 216, 'color': 'black'}]
--------------------------------------------------------------------------------------------
#wap to given list create square of each number and create new list.
x=[1,2,3,4,5,6,7,8]
print(list(map(lambda x:x**2,x)))
[1, 4, 9, 16, 25, 36, 49, 64]
------------------------------------------------------------------------------------------------
#Wap to find intersection of two given array by using lambda.
x=[1,2,3,5,6,8,9]
y=[1,2,3,7,6,4]
print(list(filter(lambda i:i in y,x)))
[1, 2, 3, 6]
-------------------------------------------------------------------
#wap to count even no and  odd no in given array.
x=[1,2,3,4,5,6,7,8,9]
print("The count of even no is",len(list(filter(lambda x:x%2==0,x))))
print("The count of odd no is",len(list(filter(lambda x:x%2!=0,x))))
The count of even no is 4
The count of odd no is 5
------------------------------------------------------------------------------------
