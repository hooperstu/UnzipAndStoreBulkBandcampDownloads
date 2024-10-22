import os
import zipfile
import shutil

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
            print(f"Successfully unzipped {os.path.basename(zip_path)} to {extract_to}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")

def main():
    source_dir = r'C:\Users\disco\Downloads'
    dest_dir = r'D:\Media\Music'

    # Ensure the destination directory exists
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Get a list of all files in the source directory
    files = os.listdir(source_dir)
    zip_files = [f for f in files if f.lower().endswith('.zip')]

    if not zip_files:
        print("No zip files found in the source directory.")
        return

    print(f"Found {len(zip_files)} zip files to extract.")

    for i, file_name in enumerate(zip_files, start=1):
        zip_path = os.path.join(source_dir, file_name)
        folder_name = os.path.splitext(file_name)[0]
        extract_to = os.path.join(dest_dir, folder_name)

        # Ensure the extraction directory exists
        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        print(f"Unzipping {file_name} ({i}/{len(zip_files)})...")
        unzip_file(zip_path, extract_to)

if __name__ == "__main__":
    main()
