# PyRenamer
PyRenamer is a Python script designed to rename all files in a specified directory with a given prefix.

It is designed to rename images of a dataset because this changes the name of **ALL THE FILES** of the directory. It doesn´t recognize between types of files

## How to use it
To use the script, follow these steps:

* Download or clone the script: It has a variable to ignore python files, by default is `True` but you can change it.

* Run the script:

Navigate to the directory containing the script in your terminal or command prompt and execute the script using Python 3.

` python3 rename.py `

* Provide the required inputs:

The script will prompt you to enter the path to the directory containing the files you want to rename and the prefix to be added to the new file names.

*Directory Path: Enter the absolute or relative path to the directory containing the files. (You can use ./)*

*Prefix: Enter the prefix you want to prepend to each file's new name.*

## Example of using
You run the program on the shell

` python3 rename.py `

It will ask you to enter the data

```
Enter the path of your directory:
/path/to/photos

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
