lst = [[1,2,3],[4,5,6],[7,8,9]]
lst2 = []
for i in range(len(lst)):
    lst3 = []   
    for j in range(len(lst[i])):
        lst3.append(lst[j][i])
    lst2.append(lst3)
print(lst2)
for i in lst2:
    print(max(i))

    

