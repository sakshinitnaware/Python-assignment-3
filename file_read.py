from datetime import datetime
import time,dataclasses

# read from the text file
# the func will take the name of the text file and print content on the console


# function to open the file with write read mode 
def file_open_read(filename,content):
    # setting the date and time format and assigning it to a variable timestamp 
    # try and except to perform file open function  
    try:
        # print statement to confirm if in try method
        # opening a file with write rights 
        with open(filename,'w') as f :
            # writing file with content using f.write function 
            f.write(content)
             # print statement to confirm writing to the file created
            print("file creation successfully")      
        # opening a file with read timestamps to it    
        with open(filename,'r') as f :
            # print statement to print the content with f.read function
            print(f.read())
            # print statement to confirm read
            print("file was read successfully")
             # exception if there is is problem while opening the file.
    except IOError as e:
        print(f"file was not created")
      
 # function call
file_open_read("python_file.txt","this is the first line in the file")
