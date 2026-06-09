import zipfile
import os

def create_zip(folder_path, output_zip):
    with zipfile.ZipFile(output_zip, "w") as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), file)
