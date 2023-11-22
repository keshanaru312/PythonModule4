#!/usr/bin/env python3
import os
import psutil
import socket
import emails

# Define thresholds for alerts
CPU_THRESHOLD = 80
DISK_THRESHOLD = 20
MEMORY_THRESHOLD = 500  # in MB

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > CPU_THRESHOLD:
        send_alert_email(f"Error - CPU usage is over {CPU_THRESHOLD}%")

def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    percent_free = disk_usage.percent
    if percent_free < DISK_THRESHOLD:
        send_alert_email(f"Error - Available disk space is less than {DISK_THRESHOLD}%")

def check_memory_usage():
    available_memory = psutil.virtual_memory().available
    if available_memory < MEMORY_THRESHOLD * 1024 * 1024:  # Convert MB to bytes
        send_alert_email(f"Error - Available memory is less than {MEMORY_THRESHOLD}MB")

def check_hostname_resolution():
    try:
        socket.gethostbyname("localhost")
    except socket.gaierror:
        send_alert_email("Error - Cannot resolve hostname 'localhost' to '127.0.0.1'")

def send_alert_email(subject):
    # Replace with your email configuration
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    body = "Please check your system and resolve the issue as soon as possible."
    message = emails.generate(sender, receiver, subject, body)
    emails.send_email(message)
    print(message)

if __name__ == "__main__":
    check_cpu_usage()
    check_disk_space()
    check_memory_usage()
    check_hostname_resolution()

