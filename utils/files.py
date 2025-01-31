import os

def get_file_extension(filename: str) -> str:
    """
    Function/Method Description: The `get_file_extension` function takes a filename as input and returns its extension.
    Parameters:
        filename (str): The name of the file for which to extract the extension.
    Returns:
        str: The file extension.
    Example:
        >>> get_file_extension("example.txt")
        ".txt"
    Notes:
        This function assumes that the filename always ends with a dot followed by the file extension, such as .txt, .json, etc.
    """
    base_name, extension = os.path.splitext(filename)
    return extension

def get_files(dir_path, suffix):
    """
    Retrieves a list of files with the specified suffix from the given directory.

    Args:
        dir_path (str): The path to the directory.
        suffix (str): The file suffix to filter by (e.g., '.txt', '.py').

    Returns:
        list: A list of file paths that match the specified suffix.
    """
    try:
        # Initialize an empty list to store matching files
        matching_files = []

        # Iterate through each item in the directory
        for filename in os.listdir(dir_path):
            # Construct the full path to the current item
            filepath = os.path.join(dir_path, filename)

            # Check if the current item is a file and has the specified suffix
            if os.path.isfile(filepath) and filename.endswith(suffix):
                # If it matches, add it to the list of matching files
                matching_files.append(filepath)

        # Return the list of matching files
        return matching_files

    except FileNotFoundError:
        print(f"The directory '{dir_path}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []