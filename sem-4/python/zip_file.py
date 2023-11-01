import os
from zipfile import ZipFile

folder = input("Enter the folder name to be zipped: ")
zip_file = folder + ".zip"

with ZipFile(zip_file, "w") as zip_object:
    for folder_name, sub_folders, file_names in os.walk(folder):
        for file in file_names:
            file_path = os.path.join(folder_name, file)
            zip_object.write(file_path, os.path.relpath(file_path, folder))

# Check if the zip file was created successfully after the 'with' block is exited
if os.path.exists(zip_file):
    print(f"{zip_file} has been created successfully!")
else:
    print(f"{zip_file} was not created.")
