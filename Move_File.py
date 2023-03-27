import os
import shutil

from_dir= "You Source"
to_dir= "Your Destinaion"
list_of_files=os.listdir(from_dir)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    if ext=="":
        continue
    if ext in [".pdf",".docx",".doc",".txt"]:
        path1 = from_dir + "/" + i 
        path2 = to_dir + "/" "Document_Files"
        path3 = to_dir + "/" "Document_Files" + "/" + i

        if(os.path.exists(path2)):
            print("Moving " + i + "...")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("Moving " + i + "...")
            shutil.move(path1,path3)   
