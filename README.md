# files-organise
Image Organizer by Date and Push into Separate Folder using Python

This Python script organizes a directory containing images in JPG format based on a specified criteria. The script parses the filenames, which are in the format "YYYY-MM-DD_HH-MM-SS_UTC_1-10.jpg", to extract the date and time information. It then groups the files that were published on the same date and time into separate folders. The process is repeated until all files are organized into folders with proper arrangement.

The script prompts the user to enter the directory location containing the images. It then prints the total number of images in the directory and organizes them by date. As the images are moved into separate folders, the script simultaneously prints the number of files of a specific date that were pushed into each folder, where 'n' represents the number of files, 'x' represents the date of the posts grouped together into a folder, and 'y' is the name of the folder assigned.

The script utilizes Python's os and shutil modules for file manipulation and datetime module for parsing dates from filenames. It provides an efficient solution for organizing large sets of images based on their publication dates.
