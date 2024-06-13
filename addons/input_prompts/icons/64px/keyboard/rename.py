import os

def remove_prefix_from_filenames(prefix):
    # Get the current working directory
    directory = os.getcwd()
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file name starts with the given prefix
        if filename.startswith(prefix):
            # Create the new file name by removing the prefix
            new_filename = filename[len(prefix):]
            # Get the full file paths
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} -> {new_filename}')

if __name__ == "__main__":
    prefix = input("Enter the prefix to remove from file names: ")
    remove_prefix_from_filenames(prefix)
