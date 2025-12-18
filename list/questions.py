# Move all zeroes to the end of a list.
# list = [1,2,3,0,4,5,0,1,2,0,3,6,0]
# zero = []
# count=0
# for i in list:
#     if i==0:
#         count+=1
#     else:
#         zero.append(i)
# zero = zero+[0]*count
# print(zero)

# -----------------------------------------------------------

# Move all zeroes to the end of a list without using extra list.
# list = [1,2,3,0,4,5,0,1,2,0,3,6,0]
# index = 0
# for i in range(len(list)):
#     if list[i]!=0:  
#         list[i],list[index]=list[index],list[i]
#         index+=1
# print(list)

# -----------------------------------------------------------

# Find the second largest element in a list.
# list = [1,6,5,4,78,9,2,4]
# max,sec = float("-inf"),float("-inf")
# for i in list:
#     if i>max:
#         sec = max 
#         max = i
#     elif sec < i and i!=max:
#         sec = i  
# print(max , sec)

# -----------------------------------------------------------

# Rotate a list to the right by 1 position.

# -----------------------------------------------------------


# Check if a list is a palindrome.
# list = [1,2,5,6,1]
# list1 = list.copy()
# st , end = 0 , len(list)-1
# while(st<end):
#     list[st],list[end] = list[end],list[st]
#     st+=1
#     end-=1
# print(list)
# print(list1)
# if list == list1:
#     print("Palindrome")
# else :
#     print("Not")

# -----------------------------------------------------------

# Split a list into two halves.
# list = [1,2,3,4,5,6]
# first,sec=[],[]
# half = len(list)//2
# for i in range(half):
#     first.append(list[i])
#     sec.append(list[i+half])
# print(first , sec)

# -----------------------------------------------------------

# Find common elements between two lists.
# list = [1,2,3,4]
# list1 = [1,2,5,6]
# for i in range(len(list)):
#     if list[i] == list1[i]:
#         print(list[i])

# -----------------------------------------------------------

# Replace all negative numbers in a list with 0.
# list = [1,2,4,-6,-8,5,-7]
# for i in range(len(list)):
#     if list[i]<0:
#         list[i]=0
# print(list)
