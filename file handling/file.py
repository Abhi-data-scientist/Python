# File :-
#     file is a named location on the storage device into the computer
#       which is used to store the data permanently
#     ex. -> photo.jped, .pdf, .bin, .csv

#  Need to handle the file...
#     To store user logs...
#     May need to read the existing file of the user
#     May need to update the existing file of the user

#  Types of the files
#     Text files -> .txt (Textual data -> user logs etc)
#     Bin files  -> store the data into the binary form
#     Image      -> bin, audio -> not human readable
#     CSV        -> comma sperated values

# How the files are stored
#     The files are stored into the hard disk or ssd permanently
#     But when we use to change something into the using the script
#     then it loaded into the RAM(Random access memory)
#     Temporary storage

# when we have to operate any operation on the file than
#   we must have to open the file first 

# syntax of openning the file 
#  f = open('filename', 'mode') 

# here we have oppend the file 
#  here 'r' is the read mode while mean we have only permission to read file...
file = open('hello.txt','r')
content = file.read() 
print(content)