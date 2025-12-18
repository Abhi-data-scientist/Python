list = [1,2,3,4,5,6,7,8,9,2,0,4]
max , sec= float("-inf"),float("-inf")
for i in list:
    if max<i:
        sec = max 
        max = i
    elif i>sec and i!=max:
        sec = i
print(max , sec)