# File-Sorter-Windows-OS-
A script that automates the moving and sorting of files into designated folders.

## Requirements:
- Windows OS.
- os, shutil, schedule, time libraries.

## What the algorithm does:
- The program requires a directory path to work in, in this file I used the Downloads folder. (Using the os library)
- Checks all the files in the directory and file types.
- Creates folders from a list given the folders do not exist in the directory. (Using the os library)
- After creating folders,it scans for file extensions in the file names in the directory, creates a copy in the clipboard and moves it to the designated folder then deletes the copy. (Using the shutil library)
- Repeats this after 15 days using the schedule provided. (Using the schedule and time library)




