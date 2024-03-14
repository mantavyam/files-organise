import os
import shutil
from datetime import datetime

def extract_date_from_filename(filename):
    parts = filename.split('_')
    if len(parts) >= 3:
        try:
            date_str = parts[0]
            time_str = parts[1]
            return datetime.strptime(f"{date_str}_{time_str}", "%Y-%m-%d_%H-%M-%S")
        except ValueError:
            pass
    return None

def organize_images_by_date(source_dir):
    # Create a dictionary to store images by date
    images_by_date = {}

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        if filename.endswith('.jpg'):
            file_date = extract_date_from_filename(filename)
            if file_date:
                if file_date not in images_by_date:
                    images_by_date[file_date] = []
                images_by_date[file_date].append(filename)

    # Create separate folders for each date
    for date, files in images_by_date.items():
        folder_name = date.strftime("%Y-%m-%d")
        folder_path = os.path.join(source_dir, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        for file in files:
            source_file = os.path.join(source_dir, file)
            destination_file = os.path.join(folder_path, file)
            shutil.move(source_file, destination_file)
        print(f"{len(files)} files of {date.strftime('%Y-%m-%d')} were pushed into folder '{folder_name}'")

if __name__ == "__main__":
    # Ask for directory location
    directory_location = input("Enter the directory location containing images: ")

    # Print total number of images in the directory
    total_images = sum(1 for _ in os.listdir(directory_location) if _.endswith('.jpg'))
    print(f"Total number of images in the directory: {total_images}")

    # Organize images by date
    organize_images_by_date(directory_location)
