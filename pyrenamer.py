import os
from tqdm import tqdm
import magic #to detect the files format

PYTHON_IGNORE = True #if you want to modify .py files, set this to False
extensions_to_ignore = [ # add every file extension you want to ignore
    #'.pdf',
    #'.jpeg',
]

def get_extension(file_path): #if the file doesnt have the extension, this detects it automatically
    mime = magic.Magic(mime=True)
    file_type = mime.from_file(file_path)
    mime_to_extension = {
        'image/jpeg': '.jpg',   # JPEG images
        'image/jpg': '.jpg',    # Alternative MIME type for JPEG images
        'image/png': '.png',    # PNG images
        'image/webp': '.webp',  # WebP images
    }

    return mime_to_extension[file_type]

def is_file(directory, filename):
    """
    Check if the path is a file. You can add your parameters of which type of file you don't want
    to be modified in the variable extensions_to_ignore
    """
    if os.path.isfile(os.path.join(directory, filename)) == False:
        return False

    _, file_extension = os.path.splitext(filename)
    if file_extension.lower() == '.py' and PYTHON_IGNORE:
        return False

    if file_extension.lower() in extensions_to_ignore:
        return False

    return True

def replace_file(directory, old_filename, new_filename): #replaces the files
    old_path = os.path.join(directory, old_filename)
    filename, ext = os.path.splitext(old_filename)

    """
    Get the extension if it doesnt have it and adds it to the file name
    """

    if ext != '':
        new_filename = new_filename + ext
    else:
        ext = get_extension(old_path) # gets the extension
        new_filename = new_filename + ext

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

    if prefix != '':
        prefix += '_'
        type_pf = str()
    else:
        type_pf = int() # type int for prefixs nulls

    preprefixed = {} # changed to a dict to keep the extensions
    secondary = [] #list of the files who cannot be overwritten

    for filename in files: #check for prefixed files

        if type_pf != int(): #if the prefix is empty, the idea is to name the files with only a number
            if prefix in filename:
                splitted_filename = filename.split('_')
                if len(splitted_filename) == 2: #fake prefix (prefix_asd_31)
                    try:
                        filename_temp, ext = os.path.splitext(splitted_filename[-1]) # splits the extension from the file to int the name
                        number_prefix = int(filename_temp) #to int because it could be prefix_a
                        preprefixed[number_prefix] = ext
                    except:
                        secondary.append(filename)
                else:
                    secondary.append(filename)
            else:
                secondary.append(filename)
        else:
            try:
                filename = int(filename) # same logic as before, if it can be overwritten, rename them first
                num_sort.append(filename)
            except:
                secondary.append(filename)


    num_sort = sorted(preprefixed)

    for number_of_file in num_sort:
        filename = prefix + str(number_of_file) + preprefixed[number_of_file]  #num_sort has the names of the files who have the prefix given, so i can get the name like this
        # if the file has the extension, it won't need to be added later
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

while True:
    directory_path = str(input('Enter the path of your directory (you can use ./ (relative path) or ~/ (absolute path):\n'))
    directory_path = os.path.expanduser(directory_path)
    if os.path.exists(directory_path): # checks if the path is valid
        break
    else:
        print('The path assigned doesn`t exists')

prefix = str(input('Enter the prefix of the files (photo, backup, etc):\n'))
print('\n')

rename_files(directory_path, prefix)
