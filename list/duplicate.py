lst = [1,2,2,3,5,4,3,1,6]
org = []
for i in lst:
    if i not in org:
        org.append(i)
print(org)