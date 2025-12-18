# Tuples :-
    # ordered
    # immutable
    # initialize with () and commas
    # faster than list

# initialising the tuple
# t = (1,2,3,4)
# print(type(t))

# initialising the tuple with one ele with one comma 
# t1 = (5,)
# print(type(t1))

# initialising empyt tuple
# t2 = ()
# print(type(t2))

# immutable
# t = (1,2,3)
# t[0]=100 #=>it gives error

# tuple packing :-this process completes when we assign some values by seperating comma 
# vars = 1,2,3
# print(type(vars))


# # here list is changed the tuple is not 
# t = ([1,2],[3,4])
# t[0][1]=100
# print(t)


# li = [(1,2),(3,4)]
# li[0][1]=0
# print(li) => it gives error


# Tuple unpackaging
# vars = 1,2,3
# a,b,c = vars
# print(a,b,c)


# method
# 1. count
# t = (1,3,5,2,3,4,5)
# print(t.count(3)) #=>give frequency of element
# print(t.index(4)) #=>give the index of element

# concatination :- returns new tuple
# t1 = (1,2,3)
# t2 = (4,5,6)
# print(t1+t2)

# Q1 sum of tuple 
# t = (1,2,3,4,5,6,7,8)
# sum=0
# for i in t:
#     sum+=i
# print(sum)

# Q2 convert a tuple of string into one string
# t = ('A','B','H','I')
# name = ''
# for i in t:
#     name+=i 
# print(name)