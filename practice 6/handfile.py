#1Create a text file and write sample data
with open("sample.txt", "w") as f:
    f.write("Hello\n")
    f.write("This is a sample file\n")


#2Read and print file contents
with open("sample.txt", "r") as f:
    print(f.read())
    
    
    
#3Append new lines and verify content
with open("sample.txt", "a") as f:
    f.write("New line added\n")
with open("sample.txt", "r") as f:
    print(f.read())
    
    
#4Copy and back up files using shutil
import shutil
shutil.copy("sample.txt", "backup.txt")


#5Delete files safely
import os
if os.path.exists("backup.txt"):
    os.remove("backup.txt")