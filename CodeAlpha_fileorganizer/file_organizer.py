import os
import shutil

# Folder containing the files
source_folder = "TestFiles"

# File categories
file_categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".doc", ".docx"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv", ".avi"]
}

# Check if the source folder exists
if not os.path.exists(source_folder):
    print("TestFiles folder not found.")
else:

    # Go through every file in the folder
    for filename in os.listdir(source_folder):

        file_path = os.path.join(source_folder, filename)

        # Make sure it is a file
        if os.path.isfile(file_path):

            # Get the file extension
            extension = os.path.splitext(filename)[1].lower()

            moved = False

            # Check which category the file belongs to
            for category, extensions in file_categories.items():

                if extension in extensions:

                    # Create category folder if it doesn't exist
                    category_folder = os.path.join(
                        source_folder, category
                    )

                    os.makedirs(category_folder, exist_ok=True)

                    # Move the file
                    destination = os.path.join(
                        category_folder, filename
                    )

                    shutil.move(file_path, destination)

                    print(f"Moved {filename} -> {category}")

                    moved = True
                    break

            # Files with unknown extensions
            if not moved:
                print(f"Skipped: {filename}")

    print("\nFile organization completed!")