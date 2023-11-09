Uses Python 3.

Without the cleanse flag, it iterates through a list of folders in a directory and tells you how much data they contain in bytes.  

With the cleanse flag, it will cleanse all of the folders with a size of 0. 
The help flag will simply show you the below message:

Usage: cleanup_dir.py [-h] -i <directory> [-c]
-i is the directory flag
-h is the help flag
-c is the cleanse flag
--kb is the kilobytes flag
--mb is the megabytes flag
--gb is the gigabytes flag

By default, data is desplayed in bytes.