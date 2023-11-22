#!/usr/bin/env python3
import os
import requests

image_dir = "./supplier-data/images/"
url = "http://localhost/upload/"

for filename in os.listdir(image_dir):
    if filename.endswith(".jpeg"):
        file_path = os.path.join(image_dir, filename)

        with open(file_path, 'rb') as opened:
            response = requests.post(url, files={'file': opened})

            if response.status_code == 201:
                print("Successfully submitted ", filename)
            else:
                print("Failed to submit ", filename)
                print("Error submitting feedback. Status code:", response.status_code)

