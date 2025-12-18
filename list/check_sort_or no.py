list = [1,2,3,4,5,6,7,8,9,2,0,4]
for i in range(len(list)-1):
    if list[i]>list[i+1]:
        print("Nhi hai sorted")
        break
