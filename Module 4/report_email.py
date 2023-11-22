#!/usr/bin/env python3

import sys
import emails
import os
import datetime
import reports

description_dir = "./supplier-data/descriptions/"
pdf_dir = "./tmp/processed.pdf"
pdf_table_dir = "./tmp/processed_table.pdf"
description_fields = ["name:", "weight:", "description", "image_name"]
fruits = []
title = "Processed Update on " + datetime.date.today().strftime("%B %d, %Y")


def populate_fruits_array(file_path):
    with open(file_path, "r") as f:
        fruit_content = f.read()
    current_fruit = {}

    fruit_lines = fruit_content.splitlines()

    current_fruit[description_fields[0]] = fruit_lines[0]
    current_fruit[description_fields[1]] = fruit_lines[1]

    return current_fruit


def populate_fruits(file_path):
    with open(file_path, "r") as f:
        fruit_content = f.read()
    current_fruit = {}

    fruit_lines = fruit_content.strip().splitlines()

    name = "{} {}".format(description_fields[0], fruit_lines[0])
    weight = "{} {}".format(description_fields[1], fruit_lines[1])

    return "{}<br/>{}<br/><br/>".format(name, weight)


def main(argv):
    body = ""
    for filename in os.listdir(description_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(description_dir, filename)
            body += populate_fruits(file_path)
            fruits.append(populate_fruits_array(file_path))

    # print(body)
    # print(fruits)

    # reports.generate_report_table(pdf_table_dir, title, fruits)
    reports.generate_report(pdf_dir, title, body)

    # TODO: send the PDF report as an email attachment
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate(sender, receiver, subject, body, pdf_dir)
    # print(message)
    emails.send_email(message)


if __name__ == "__main__":
    main(sys.argv)
