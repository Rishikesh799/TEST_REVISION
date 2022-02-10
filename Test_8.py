#Wap to sort list of tuples using lambda.
x=[("english",88),("science",90),("maths",97),("social sccience",82)]
print(sorted(x,key=lambda x:x[1],reverse=False))
[('social sccience', 82), ('english', 88), ('science', 90), ('maths', 97)]
-----------------------------------------------------------------------------------------
