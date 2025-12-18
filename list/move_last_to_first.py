list = [1,2,3,4,5,6,7,8,9,2,0,4]
temp = list[len(list)-1]
for i in range(len(list)):
    list[i],temp=temp,list[i]
print(list)
