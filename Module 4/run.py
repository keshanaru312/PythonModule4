#!/usr/bin/env python3

import os
import re
import requests

description_dir = "./supplier-data/descriptions/"
description_fields = ["name", "weight", "description", "image_name"]
store_external_ip = "34.125.109.46"
store_url = "http://{}/fruits/".format(store_external_ip)

def convert_string_to_int(string):
    # Create an empty list to store the numbers
    numbers = []

    # Iterate through each character in the string
    for character in string:
        # Check if the character is a digit
        if character.isdigit():
            # Add the digit to the list of numbers
            numbers.append(character)

    # Convert the list of numbers to a string
    number_string = "".join(numbers)

    # Convert the string of numbers to an integer
    number = int(number_string)
    # print(number)

    # Return the integer
    return number

# Iterate through .txt files and extract feedback data
for filename in os.listdir(description_dir):
    if filename.endswith(".txt"):
        file_path = os.path.join(description_dir, filename)
        with open(file_path, "r") as f:
            fruit_content = f.read()
        current_fruit = {}

        fruit_lines = fruit_content.splitlines()

        current_fruit[description_fields[0]] = fruit_lines[0]
        current_fruit[description_fields[1]] = convert_string_to_int(fruit_lines[1])
        current_fruit[description_fields[2]] = fruit_lines[2]
        current_fruit[description_fields[3]] = filename.replace(".txt", ".jpeg")

        # print(current_fruit)
        response = requests.post(store_url, json=current_fruit)

        if response.status_code == 201:
            print("Successfully submitted ", filename)
        else:
            print("Failed to submit ", filename)
            print("Error submitting feedback. Status code:", response.status_code)