
import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "jpg_images"

# Create the folders if they do not exist
os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)

# Count moved files
moved_count = 0

# Find and move JPG files
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".jpg", ".jpeg")):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(
            destination_folder, filename
        )

        if os.path.isfile(source_path):
            # Avoid overwriting an existing file
            if os.path.exists(destination_path):
                print(f"Skipped: {filename} already exists")
                continue

            shutil.move(source_path, destination_path)
            print(f"Moved: {filename}")
            moved_count += 1

print(f"\nAutomation completed!")
print(f"Total images moved: {moved_count}")
