import os
import shutil

# Define your target directory
source_dir = 'C:/Users/Admin/Downloads'  # Change this to your folder path

# File type mappings
file_mappings = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []
}

def organize_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension
        _, ext = os.path.splitext(filename)
        ext = ext.lower()

        # Match file extension to category
        moved = False
        for folder, extensions in file_mappings.items():
            if ext in extensions:
                target_folder = os.path.join(directory, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, filename))
                moved = True
                break

        # Move to 'Others' if no match
        if not moved:
            target_folder = os.path.join(directory, 'Others')
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, filename))

    print("File organization complete.")

if __name__ == "__main__":
    organize_files(source_dir)
