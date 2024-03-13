import os
import requests

# Replace these values with your actual URL and payload
url = "https://example.com/api"
payload = {"command": "your_command_here"}

try:
    # Send POST request with payload
    response = requests.post(url, json=payload)

    # Check status code
    if response.status_code == 200:
        print("Request successful! Status code: 200")
        print("Response content:", response.text)
    else:
        print(f"Request failed with status code: {response.status_code}")
        print("Response content:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Error sending request: {e}")

def remove_file(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            # Remove the file
            os.remove(file_path)
            print(f"File '{file_path}' removed successfully.")
        else:
            print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error removing file: {e}")

# Replace 'filename.txt' with the actual file name you want to remove
file_to_remove = '/Users/mirzamansooralibaig/Desktop/hello.txt'

remove_file(file_to_remove)

