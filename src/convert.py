import logging
import os
from typing import List

import pyheif
from PIL import Image

logger = logging.getLogger(__name__)


def heics_to_jpg(files: List[str], save_path: str = "~/h2j-converts"):
    """
    Convert a list of HEIC files to JPEGs. Consider defaulting to storing the files
    in the same folder that the file was in originally.

    :param list files: List of fs of HEICs to convert.
    :param str save_path: Optional folder to save converted files to.
    """

    for f in files:
        filepath, extension = os.path.splitext(f)
        filename = filepath.split("/")[-1]

        if extension.lower() in {".heic", ".heif"}:
            try:
                heif_file = pyheif.read(f)
                image = Image.frombytes(
                    heif_file.mode,
                    heif_file.size,
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )

                new_file = os.path.join(save_path, filename, ".jpg")
                image.save(new_file, "JPEG")
                logging.info(f"created {new_file}")
            except Exception as e:
                logger.error(f"failed to convert {f}: {e}")
        else:
            logger.warning(f"{f} is not a HEIC file, skipping")
