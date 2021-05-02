import pyheif
import os
from PIL import Image

for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        if ".heic" in name.lower() and root == ".":
            try:
                heif_file = pyheif.read(name)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                new_file = name.replace(".heic", ".jpg")
                new_file = new_file.replace(".HEIC", ".jpg")

                image.save(new_file, "JPEG")
                print(f"created {new_file}")
            
            # take this out after
            except Exception as e:
                if str(e) == "Input is not a HEIF/AVIF file":
                    new_file = name.replace(".heic", ".jpg")
                    new_file = new_file.replace(".HEIC", ".jpg")
                    os.rename(name, new_file)
                    
