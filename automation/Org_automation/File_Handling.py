file = open("test.py")
print(file.read())

#create a file

file = open("Text2.txt","x")

#write to file 

file = open("test.py","w")
file.write("hello gig")
file.close

#Read a file
file = open("Text.txt", "r")
print(file.read())
file.close

#Append a File:

file = open("newText.txt", "a")
file.write("This is an example of file appending.")
file.close