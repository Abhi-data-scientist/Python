lst = [1,2,3,4,5,6,7,8,9]
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]<lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)
