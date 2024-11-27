import os
import urllib.parse
import urllib.request


def download_and_generate_file_url(web_url, save_directory, file_name):
    """
    Download the content from a web URL and save it locally, then generate a file:// URL.

    Args:
        web_url (str): The URL of the web resource (e.g., https://www.google.com/).
        save_directory (str): Directory to save the downloaded file.
        file_name (str): Name of the saved file (e.g., "google.html").

    Returns:
        str: The file:// URL of the downloaded file.
    """
    # Ensure the save directory exists
    os.makedirs(save_directory, exist_ok=True)

    # Full path of the saved file
    file_path = os.path.join(save_directory, file_name)

    # Download the web content and save to the file
    try:
        urllib.request.urlretrieve(web_url, file_path)
        print(f"Downloaded content from {web_url} to {file_path}")
    except Exception as e:
        print(f"Failed to download {web_url}: {e}")
        return None

    # Convert the local file path to a file:// URL
    abs_path = os.path.abspath(file_path).replace("\\", "/")
    file_url = "file:///" + urllib.parse.quote(abs_path)

    return file_url


# Example Usage
if __name__ == "__main__":
    # Web URL to download
    web_url = "https://www.google.com/"

    # Directory to save the file and the desired file name
    save_directory = "downloaded_files"
    file_name = "google.html"

    # Download and generate the file URL
    file_url = download_and_generate_file_url(web_url, save_directory, file_name)

    if file_url:
        print(f"File URL: {file_url}")
