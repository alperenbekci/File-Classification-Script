import os
import shutil

# Specify the path to the main directory for the operation
main_directory_path = '/path/to/main_directory'

# List all files and folders in the main directory
all_files = os.listdir(main_directory_path)

# Separate files based on their extensions and move them to appropriate folders while deleting the original files
for file in all_files:
    file_path = os.path.join(main_directory_path, file)

    # Get the file extension
    extension = file.split('.')[-1].lower()

    # Determine the destination folder path
    destination_folder_path = os.path.join(main_directory_path, extension)

    # Create the destination folder (if it doesn't exist)
    if not os.path.exists(destination_folder_path):
        os.makedirs(destination_folder_path)

    # Move the file to the destination folder
    destination_file_path = os.path.join(destination_folder_path, file)
    shutil.move(file_path, destination_file_path)

# Delete the original files after moving them
for file in all_files:
    file_path = os.path.join(main_directory_path, file)
    if os.path.isfile(file_path):
        os.remove(file_path)

print("Files have been successfully classified, and the original files have been deleted.")
