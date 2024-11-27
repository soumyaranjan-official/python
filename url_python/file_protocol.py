import os
import urllib.parse


def generate_file_url(file_path):
    """
    Generate a file:// protocol URL for the given file path.

    Args:
        file_path (str): The relative or absolute path to the file.

    Returns:
        str: A valid file:// protocol URL for the file.
    """
    # Convert to absolute path
    abs_path = os.path.abspath(file_path)

    # Check if the file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    # Replace backslashes with forward slashes for file URL compatibility
    abs_path = abs_path.replace("\\", "/")

    # Encode the path for URL safety
    file_url = "file:///" + urllib.parse.quote(abs_path)

    return file_url


# Example Usage
if __name__ == "__main__":
    # Specify the file path
    pdf_file_path = "E:\\demo_site\\url_python\\das7_TTPI Report_2024.pdf"

    try:
        # Generate the file URL
        file_url = generate_file_url(pdf_file_path)
        print(f"File URL: {file_url}")
    except FileNotFoundError as e:
        print(e)
