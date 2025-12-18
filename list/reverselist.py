li = [1,2,3,4,5,6,7,8,9]
rev = []
for i in range(len(li)-1,-1,-1):
    rev.append(li[i])
print(rev)

# rev = li[::-1]
# rev = list(reversed(li))
# print(rev)
