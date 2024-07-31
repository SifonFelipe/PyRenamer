# PyRenamer
PyRenamer is a Python script designed to rename all files in a specified directory with a given prefix.

It is designed to rename images of a dataset because i had this problem at the moment of renaming the files.

If you want to use it for another purpose, do it. You can set which types of files won´t be affected.

## How to use it
To use the script, follow these steps:

* Download or clone the script

If you want to customize some things about the script like the type of files to ignore, there is a variable that does that.

* Run the script:

Navigate to the directory containing the script in your terminal or command prompt and execute the script using Python 3.

` python3 rename.py `

* Provide the required inputs:

The script will prompt you to enter the path to the directory containing the files you want to rename and the prefix to be added to the new file names.

*Directory Path: Enter the absolute or relative path to the directory containing the files. (You can use ./ or ~/)*

*Prefix: Enter the prefix you want to prepend to each file's new name.*

## Example of using
You run the program on the shell

` python3 rename.py `

It will ask you to enter the data

```
Enter the path of your directory (you can use ./ (relative path) or ~/ (absolute path):
/path/to/photos/or/files/

Enter the prefix of the files (photo, backup, etc):
image
```
The output:

```
image_0.jpg
image_1.jpg
image_2.pdf
```

### Modify it to your liking
