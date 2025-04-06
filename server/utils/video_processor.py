import requests
import os

def download_video(url, filename):
    """Download video from URL and save to file"""
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Video downloaded successfully as '{filename}'")
        return True
    else:
        print("Failed to download the video")
        return False