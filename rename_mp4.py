import os
import glob

# Get the current directory
current_directory = os.getcwd()

# Specify the file extension to search for
extension = "*.mp4"

# Create a list of MP4 files in the current directory
mp4_files = glob.glob(os.path.join(current_directory, extension))

# Sort the list of files alphabetically
mp4_files.sort()

# Iterate over each MP4 file
for index, file_path in enumerate(mp4_files, start=1):
    # Get the original file name
    original_name = os.path.basename(file_path)

    # Extract the new file name by removing characters before and including the '-'
    new_name = original_name.split('-')[-1].strip()

    # Add the number at the beginning of the new file name
    new_name = f"{index} {new_name}"

    # Rename the file
    new_file_path = os.path.join(current_directory, new_name)
    os.rename(file_path, new_file_path)
