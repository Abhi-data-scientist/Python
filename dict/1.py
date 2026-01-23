# # dictionary is a datatype 
# # it stores the key and value pairs
# # dictonary is mutable
# # keys must be unique and also keys are immutable

# d={}
# print(type(d))

# student_data = {
#     'Name' : 'Abhi',
#     'Class' : 10,
#     'Roll No' : 25
# }

# print(student_data)
# print(student_data['Name'])

# # basic syntax d = {'Key' : 'Value'}

# di = {
#     (1,2) : 'rahul'
# }
# print(di[(1,2)])

# # Keys must be immutable 
# # strings, numbers, tuples

# print(dict(name='rahul', rollno=25, batch='A24'))
# # syntax dict(key=value)

# data = {
#     'name' : ['abhi', 'divyanse', 'vikash'],
#     'rollno': [5,10,50]
# }
# print(data['rollno'][0])
# print(data['name'][2])
# print(data.get('location','not present')) #it never give error if there is no key
#=> to acces any value from the dict we can also use .get() method
# => but there is a small difference using [] and .get()
#=> in [] it would give error if the key is not present in dict
#=> but into the .get() method it would not give any error

# print(data.keys())
# print(data.values())

# for key in data:
#     print(f'{key} : {data[key]}')


student_data = {
    'Name' : 'Abhi',
    'Class' : 10,
    'Roll No' : 25
}
# print(student_data.items())

# for item in student_data.items():
#     key,value=item
#     print(f'{key} : {value}')

# make a dict assign a new value to that key and print that new dict
# data ={
#     'name' : 'abhi',
#     'rollno' : 2
# }
# data['name'] = 'Abhishek'
# print(data['name'])

# # sum of all the values of the dictionary
# data = {
#     '1' : 1,
#     '2' : 2,
#     '3' : 3,
#     '4' : 2,
#     '5' : 7,
#     '6' : 5
# }

# sum = 0
# for i in data.items():
#     key,value=i
#     sum+=value 

# print(sum)

# # max value
# data = {
#     '1' : 1,
#     '2' : 2,
#     '3' : 3,
#     '4' : 2,
#     '5' : 7,
#     '6' : 5
# }

# max = float('-inf')
# for i in data.items():
#     key,value=i
#     if value>max :
#         max=value

# print(max)

# count the frequency of each element in a list
# li = [1,1,2,3,2,3,4,2,4]
# di = {}
# for i in range(len(li)):
#     if i not in di:

# print the key value pairs where the value is greater than 50  
data = {
    '1' : 16,
    '2' : 278,
    '3' : 365,
    '4' : 20,
    '5' : 70,
    '6' : 50
} 
# for i in data:
#     if data[i]>50:
#         print(f'{i} : {data[i]}')

# swap key value of the dict
# for i in data.items():
#     value, key = i
#     key, data[value] = data[value], key
# print(data)


