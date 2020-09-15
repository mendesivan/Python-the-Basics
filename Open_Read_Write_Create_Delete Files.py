# Open file

# Reference Guide

    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    # "a" - Append - Opens a file for appending, creates the file if it does not exist

    # "w" - Write - Opens a file for writing, creates the file if it does not exist

    # "x" - Create - Creates the specified file, returns an error if the file exists

    # "t" - Text - Default value. Text mode

    # "b" - Binary - Binary mode (e.g. images)"""

txtfile = open("C:/Users/IvanMendes/Spyder Py Files/Python_Tutorials_w3School/Python File Handling/demotext.txt","r") #read and text
print(txtfile) #prints location of file/attributes

print(txtfile.read()) #print txt file.
print(txtfile.readline()) #read one line of the file.

# Loop through file, line by line.

for x in txtfile:
    print(x)

txtfile.close() #closes the file.

# Write to file.

txtfile = open("C:/Users/IvanMendes/Spyder Py Files/Python_Tutorials_w3School/Python File Handling/demotext.txt","w") #read and text

txtfile.write("Nice to meet you Ivan, My name is Mike.")

txtfile.close() #closes the file.

#open and read the file after the appending:
txtfile = open("C:/Users/IvanMendes/Spyder Py Files/Python_Tutorials_w3School/Python File Handling/demotext.txt","r") #read and text
print(txtfile.read())

txtfile.close() #closes the file.

#Create new file.
newfile = open("NEW","x") #new file method
newfile = open("NEWbyWriting","w") #creates new if not already present






