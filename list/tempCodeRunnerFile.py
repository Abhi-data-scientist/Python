list = [1,2,3,4,5,6]
first,sec=[],[]
half = len(list)//2
for i in range(half):
    first.append(list[i])
    sec.append(list[i+half])
print(first , sec)