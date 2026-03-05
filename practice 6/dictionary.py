#1Create nested directories
import os
os.makedirs("folder1/folder2", exist_ok=True)


#2List files and folders
print(os.listdir("."))


#3Find files by extension
for file in os.listdir("."):
    if file.endswith(".txt"):
        print(file)
        
#4Move/copy files between directories
import shutil
shutil.move("sample.txt", "folder1/sample.txt")
