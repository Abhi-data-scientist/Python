# Initialising the list 

# new_list = [1,2,3]
# print(type(new_list))
# print(list)

# details = ["Abhi",'A23',100]
# print(details)

# Accessing the elements of the list 
# Since, the list are sequence data type so we can access this using index

# print(f"Name : {details[0]}")
# print(f"Batch : {details[1]}")
# print(f"Roll_number : {details[0]}")

# print("Name : {} Batch : {} Roll_number : {}".format(details[0],details[1],details[2]))

# print(f"Name : {details[-3]}")
# print(f"Batch : {details[-2]}")
# print(f"Roll_number : {details[-1]}")  


# list slicing
# list = [1,2,3,4,5]
# index => 1,2,3,4
# print(list[1:5])

# Taking 2 steps
# print(list[::2])
# print(list[-5::2])

# reverse list 
# print(list[::-1])


# string immutable => After creation of the srting it couldn't be change
# s = "String"
# s[0] = 'G'
# print(s) =>Error

# List is mutable : it could be change after the creation or initialization
# new_list = [10,20,30,40]
# new_list[0]=100
# print(new_list)

# implementin the first loop on the list using the indices
# for index in range(len(new_list)):
#     print(new_list[index], end = " ")

# Accessing the elements without using index
# for i in new_list:
#     print(i , end = ' ')

# list = [1,2,3,4,5]
# list[3] = 20
# print(list)

# # sum of list 
# list = [1,2,3,4,5]
# sum = 0
# for i in list:
#     sum += i
# print(sum)

# # product of list
# pro = 1
# for i in list:
#     pro *= i 
# print(pro)

# print Odd numbers
# list = [1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2!=0:
#         print(i,end=" ")

# list = [1,2,3,4,5,6,7,8,9,10]
# for i in range(1,len(list),2):
#     print(list[i])

# +2 every element
# list = [1,2,3,4]
# for i in range(len(list)):
#     list[i]+=2
# print(list)

# add two list
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# for i in range(len(list1)):
#     list1[i]+=list2[i]
# print(list1)

# add two list by positive and negative index
# list1 = [1,2,3,4]
# list2 = [5,6,7,8]
# for i in range(len(list1)):
#     list1[i]+=list2[len(list2)-i-1]
# print(list1)

# largest and smallest and second largest
# list = [10,2,3,4,5,6,7,8,9]
# max,small,sec=list[0],list[0],list[0]
# for i in range(1,len(list)):
#     if max<list[i]:
#         sec=max
#         max=list[i]
#     if small>list[i]:
#         small=list[i]

# print(f"max : {max} small : {small} second_max : {sec}")

# second max 
# list = [10,2,3,4,5,6,7,8,9]
# max,sec_max = 0,0
# for i in list:
#     if i>max:
#         sec_max=max 
#         max=i
#     elif i>sec_max:
#         sec_max=i
# print("Second max is : ",sec_max)

# Second smallest 
# list = [10,2,3,4,5,6,7,8,9]
# small,sec = float('inf'),float('inf')
# for i in list:
#     if i<small:
#         sec=small 
#         small=i
#     elif i<sec:
#         sec=i
# print("Second max is : ",sec)

# float('inf') => small
# float('-inf') => large

# swap first and last
# list = [10,20,30,40]
# list[0],list[-1]=list[-1],list[0]
# print(list)

# Reverse a list 
# list = [1,2,3,4,5,6,7]
# left=0
# right=len(list)-1
# while left<right:
#     list[left],list[right]=list[right],list[left]
#     left+=1
#     right-=1
# print(list)

# square the odd indx in first list 
# cube the even indx in second list
# list = [1,2,3,4,5,6,7,8,9,10]
# sq,cube=[],[]
# for i in range(len(list)):
#     if i%2!=0:
#         sq.append(list[i]**2)
#     else:
#         cube.append(list[i]**3)
# print("Square list : ",sq)
# print("Cube list : ",cube)

# find the length of list 
# list = [1,2,3,4,5,6,7,8,9,10]
# count=0
# for i in list:
#     count+=1
# print(f"Length of list is : {count}")

# print common number
# list1 = [1,2,3,4,5]
# list2 = [4,5,6,7,8]
# for i in list1:
#     if i in list2:
#         print(i)

# list is palindrome or not
# list=[1,2,3,4,5]
# org=list
# st,end=0,len(list)-1
# while(st<end):
#     list[st],list[end]=list[end],list[st]
#     st+=1
#     end-=1
# if org==list:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# print palindrome names
# list = ['aman','naman','ram']
# for i in list:
#     if i==i[::-1]:
#         print(i)

# reverse list by negative index
# list=[1,2,3,4,5]
# for i in range(len(list)-1,0,-1):
#     print(list[i]) 

# methods:

# 1. list.sort() => it sort the list
# 2. sorted(list) => gives new sorted list
# 3. sum(list) => it gives sum of list

# check a list is sorted or not 
# list = [5,7,9,1]
# if list==sorted(list):
#     print("sorted")
# else:
#     print("Not sorted")

#  2nd way
# for i in range(len(list)-1):
#     if list[i]>list[i+1]:
#         print("List is not sorted")
#         break
# else:
#     print("Sorted hai")

# find the k element from the list , if the element exists print the index
# list = [7,9,5,4,86,3,2,1]
# k=4
# for i in range(len(list)-1):
#     if k==list[i]:
#         print("k element index is : ",i)
#         break 
# else:
#     print("Not exists")

# print all number with their indices
# list = [7,9,5,4,86,3,2,1]
# for i in range(len(list)):
#     print(f"{i} => {list[i]}")

# list = [7,9,5,4,86,3,2,1]
# for idx , element in enumerate(li):
#     print(idx,element)
# enumerate function is used to return or print the idx along with the values

# apend 4 numbers in list 
# list = []
# sum=0
# for i in range(4):
#     list.append(int(input("Enter number : ")))
#     sum += list[i]
# print(list)
# print(sum)

# new way to create a list without loop 
# li = input("Enter numbers of list : ").split()
# li = list(map(int,input("Enter numbers of list : ").split()))
# li = list(map(int,li))
# print(li)
# print(sum(li))

# map = list ke her element per iterate krne ke liye use hota hai 

# target sum nikalo
# list = [1,2,3,4,5,6,7,8,9]
# target = 7
# for i in range(len(list)-1):
#     for j in range(i+1,len(list)):
#         if list[i]+list[j]==target:
#             print(f"{i+1} {j+1}")

# find largest word
# list = ['this','is','sentence']
# max = len(list[0])
# word = ""
# for i in range(1,len(list)):
#     if max<len(list[i]):
#         max=len(list[i])
#         word = list[i]
# print(word)

# sorted list find missing value
# list = [1,2,3,5]
# sum_l=0
# for i in range(1,5+1):
#     sum_l+=i
# print(sum_l-sum(list))

# remove duplicate element
# list = [1,2,2,3,4]
# li=[]
# for i in list:
#     if i not in li:
#         li.append(i)
# print(li)

# find 7 element in 2d list
# list = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         if list[i][j]==7:
#             print(i,j)

# sum of all element
# list = [[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         sum+=list[i][j]
# print(sum)

# find largest
# list = [[1,2,3],[4,5,6],[7,8,9]]
# max=float('-inf') 
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         if max<list[i][j]:
#             max=list[i][j]
# print(max)

# flat the 2d list into 1d list 
# list = [[1,2,3],[4,5,6],[7,8,9]]
# li = []
# for i in range(len(list)):
#     li.extend(list[i])
# print(li)

# seperate out the odd and even 
# list = [[1,2,3],[4,5,6],[7,8,9]]
# evenlist,oddlist=[],[]
# for i in range(len(list)):
#     for j in range(len(list[i])):
#         if list[i][j]%2==0:
#             evenlist.append(list[i][j])
#         else:
#             oddlist.append(list[i][j])
# print(evenlist)
# print(oddlist)

# diagonal sum of the matrix 
# list = [[1,2,3],[4,5,6],[7,8,9]]
# sum=0
# for i in range(len(list)):
#     sum+=list[i][i]
# print(sum)

# Reverse each row of matrix
# list = [[1,2,3],[4,5,6],[7,8,9]]
# for i in range(len(list)):
#     list[i]=list[i][::-1]
# print(list)

# largest element of each list
# list = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
# for i in list:
#     print(max(i))

