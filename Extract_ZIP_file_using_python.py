import zipfile
import os

# Define the path to the zip file
zip_path = 'zip_path'

# Define the directory to extract to
extract_to = 'unzip_path'

# Create the directory if it doesn't exist
os.makedirs(extract_to, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction completed.")
