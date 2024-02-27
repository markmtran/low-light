import os


def get_image_files(dir):
    """
    Get a list of image files in the specified directory.

    Args:
    - dir (str): Path to the directory containing image files.

    Returns:
    - image_files (list): List of image file names.
    """
    all_files = os.listdir(dir)

    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]
    image_files = [
        file
        for file in all_files
        if any(file.lower().endswith(ext) for ext in image_extensions)
    ]

    return image_files
