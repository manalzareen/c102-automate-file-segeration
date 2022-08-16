import os
import shutil

from_dir = "assests"
to_dir = "images"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for i in list_of_files:
    name,ext = os.path.splitext(i)
    if ( ext == "" ):
        continue
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        path1 = from_dir + "/" + i  # Example path1 : assets/badminton.gif
        path2 = to_dir + "/" + "pictures" + i
        path3 = to_dir + "/" + "pictures"
        if os.path.exists(path2):
            print("Moving " + i + ".....")
            #shutil.move(source , destination)
            shutil.move(path1,path2)
        else :
            os.makedirs(path3)
            print("Moving " + i + ".....")
            shutil.move(path1,path2)