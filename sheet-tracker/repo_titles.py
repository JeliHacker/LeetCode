import os
import re

# Define the regular expression pattern to match the file names
pattern = r'^(\d+)_'

# Specify the directory path of your Git repository
repo_path, directory = '/Users/jeligooch/Desktop/git/LeetCode/Python3', '/Users/jeligooch/Desktop/git/LeetCode/Python3'

# Get the list of files in the repository directory
files = os.listdir(repo_path)

# Iterate through each file
for file_name in files:
    # # Check if the file name matches the pattern
    # if re.match(pattern, file_name):
    #     # Extract the number part from the file name
    #     match = re.search(pattern, file_name)
    #     number_part = match.group(1)
    #
    #     # Pad the number part with leading zeros to make it four digits
    #     padded_number = number_part.zfill(4)
    #
    #     # Construct the new file name by replacing the number part
    #     new_file_name = re.sub(pattern, padded_number + '_', file_name)
    #
    #     # Rename the file
    #     old_path = os.path.join(repo_path, file_name)
    #     new_path = os.path.join(repo_path, new_file_name)
    #     os.rename(old_path, new_path)
    #     print(f'Renamed "{file_name}" to "{new_file_name}"')

    old_path = os.path.join(directory, file_name)

    if os.path.isfile(old_path):  # Ensure it's a file, not a directory
        # Replace underscores with dashes
        new_file_name = file_name.replace("_", "-")

        new_path = os.path.join(directory, new_file_name)
        os.rename(old_path, new_path)
        print(f'Renamed "{file_name}" to "{new_file_name}"')
