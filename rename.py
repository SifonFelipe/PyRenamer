import os
from tqdm import tqdm

PYTHON_IGNORE = True #if you want to modify .py files, set this to False
extensions_to_ignore = [ # add every file extension you want to ignore
    #'.pdf',
    #'.jpeg',
]

def is_file(directory, filename): #check if it is a directory or a .py file
    if os.path.isfile(os.path.join(directory, filename)) == False:
        return False

    _, file_extension = os.path.splitext(filename)
    if file_extension.lower() == '.py' and PYTHON_IGNORE:
        return False

    if file_extension.lower() in extensions_to_ignore:
        return False

    return True

def replace_file(directory, old_filename, new_filename):
    old_path = os.path.join(directory, old_filename)
    new_path = os.path.join(directory, new_filename)
    os.rename(old_path, new_path)

def rename_files(directory, prefix):
    """
    It's a bit long because there is a problem -> if you have photos or files with the prefix,
    they will be overwritten when the files are renamed. sorted() does not solve the problem.
    The logic of this is to first split and rename the files that have a name like: prefix_[a number]
    from the others who cannot be overwritten.
    """
    files = sorted([filename for filename in os.listdir(directory) if is_file(directory, filename)]) #split files from directories

    file_index = 0 #prefix addon

    prefix += '_'
    num_sort = [] #list of the files with prefixs, only numbers to be able to sort
    secondary = [] #list of the files who cannot be overwritten

    for filename in files: #check for prefixed files
        if prefix in filename:
            splitted_filename = filename.split('_')
            if len(splitted_filename) == 2: #fake prefix (prefix_asd_31)
                try:
                    number_prefix = int(splitted_filename[-1]) #to int because it could be prefix_a
                    num_sort.append(number_prefix)
                except:
                    secondary.append(filename)
            else:
                secondary.append(filename)
        else:
            secondary.append(filename)


    num_sort = sorted(num_sort)
    for number_of_file in num_sort:
        filename = prefix + str(number_of_file) #num_sort has the names of the files who have the prefix given, so i can get the name like this
        new_filename = prefix + str(file_index)
        replace_file(directory, filename, new_filename)
        file_index += 1

    for filename in tqdm(secondary, desc='Renaming remaining files'):
        new_filename = prefix + str(file_index)
        replace_file(directory, filename, new_filename)
        file_index += 1

    print('Done.')
    print(f'Renamed Files: {len(files)}')
    ignored_files = len(os.listdir(directory)) - len(files) if len(os.listdir(directory)) - len(files) > 0 else 0
    print(f'Ignored files or directories: {ignored_files}')


directory_path = str(input('Enter the path of your directory (you can use ./ (relative path) or ~/ (absolute path):\n'))
directory_path = os.path.expanduser(directory_path)

prefix = str(input('Enter the prefix of the files (photo, backup, etc):\n'))
print('\n')

rename_files(directory_path, prefix)
