from datetime import datetime
import time,dataclasses

# function to open the file with write read mode 
def file_open_read(filename,content):
    # setting the date and time format and assigning it to a variable timestamp 
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # try and except to perform file open function  
    try:
        # print statement to confirm if in try method
        print("file open successfully")
        # opening a file with write timestamps to it 
        with open(filename.format(timestamp=timestamp),'w') as f :
            # writing file with timestamps 
            f.write(content.format(timestamp=timestamp))
             # print statement to confirm writing
            print("file wrote successfully\n")      
        # opening a file with read timestamps to it    
        with open(filename.format(timestamp=timestamp),'r') as f :
            print("----------------------------------------------------------------")
            # print statement to print the content with f.read function
            print(f.read())
            print("----------------------------------------------------------------\n")
            # print statement to confirm read
            print("file was read successfully")
             # exception if there is is proble while opning the file.
    except IOError as e:
        print(f"file was not read")
      
# Define file name with timestamp  
filename = "date{timestamp}.txt"
# Define content with timestamp
content ="how was you day {timestamp}" 
 # function call
file_open_read(filename,content)
