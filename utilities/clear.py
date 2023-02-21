import os
import shutil


# Directory path to remove files from
directory = './'

# List of file names to exclude from removal
exceptions = ['.venv', 'utilities']

# Get a list of all the files and directories in the directory
all_files = os.listdir(directory)

# Remove every file and directory except the exceptions
for file_name in all_files:
    file_path = os.path.join(directory, file_name)
    if not os.path.isdir(file_path) and not file_name.endswith('.py') and not file_name.endswith('.txt'):
        os.remove(file_path)
    elif os.path.isdir(file_path) and file_name not in exceptions:
        shutil.rmtree(file_path)