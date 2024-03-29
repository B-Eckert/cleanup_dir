from pathlib import *
from glob import *
from getopt import *
import os
import shutil
import sys

# credit to stack overflow user monkut for the get_size method
def get_size(start_path):
    size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not(os.path.islink(fp)):
                size += os.path.getsize(fp)
    return size

cleanse_dir = "C:/Users/gamin/Desktop/Workspaces/test"
cleanse = False
dirspecified = False
kilobytes = False
megabytes = False
gigabytes = False

if(len(sys.argv) > 0):
    for x in range(0, len(sys.argv)):
        if(sys.argv[x] == "-h"):
            print("Usage: cleanup_dir.py [-h] -i <directory> [-c]\n-i is the directory flag\n-h is the help flag\n-c is the cleanse flag\n" +
                  "--kb is the kilobytes flag\n--mb is the megabytes flag\n--gb is the gigabytes flag\n\nBy default, data is desplayed in bytes.")
            sys.exit(2)
        elif(sys.argv[x] == "-i"):
            if(x == len(sys.argv) - 1):
                print("Usage: cleanup_dir.py [-h] -i <directory> [-c]")
                sys.exit(2)
            cleanse_dir = sys.argv[x+1] 
            dirspecified = True
        elif(sys.argv[x] == "-c"):
            cleanse = True
        elif(sys.argv[x] == "--kb"):
            kilobytes = True
            megabytes = False
            gigabytes = False
        elif(sys.argv[x] == "--mb"):
            kilobytes = False
            megabytes = True
            gigabytes = False
        elif(sys.argv[x] == "--gb"):
            kilobytes = False
            megabytes = False
            gigabytes = True
if(not dirspecified):
    print("Run cleanup_dir.py -h for how to use this. No directory specified.")
    sys.exit(1)

if(not os.path.isdir(cleanse_dir)):
    print("Invalid directory")
    sys.exit(2)

dirs = glob(cleanse_dir + "/*/")
for x in range(0, len(dirs)):
    size = get_size(dirs[x])
    extra = "B"
    if(kilobytes):
        size /= 1000.0
        extra = "KB"
    elif(megabytes):
        size /= 1000000.0
        extra = "MB"
    elif(gigabytes):
        size /= 1000000000.0
        extra = "GB"
    print(dirs[x][len(cleanse_dir):] + " : " + str(size) + " " + extra)
    if((size == 0) and cleanse):
        print("\t\tDeleting " +  dirs[x][len(cleanse_dir):])
        try:
            shutil.rmtree(dirs[x])
        except:
            print("\t\tFolder" + dirs[x][len(cleanse_dir):] + " currently being used. Deletion failed. Moving on.")
