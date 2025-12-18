list = [1,2,3,4,5,6,7,8,9]
small = float("inf")
for i in list:
    if small>i:
        small = i 
print("max is : ",small)

# also use min(list)