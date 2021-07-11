import os
import shutil
import time

path = input("enter dir to be clean ")+"/"
if(os.path.exists(path)):
    for (root, dir, files) in os.walk(path):
        for file in files:
            filename = ''
            if(root[-1] == '/'):
                filename = root+file
            else:
                filename = root+"/"+file

            print(f"{time.time() - os.stat(filename).st_ctime }")
            if time.time() - os.stat(filename).st_ctime < 59200:
                if os.path.isdir(filename):
                    shutil.rmtree(filename)
                else:
                    os.remove(filename)
else:
    print("path not found ")
