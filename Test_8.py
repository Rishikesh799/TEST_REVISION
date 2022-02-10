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
