import psutil
import socket

# Define thresholds for alerts
CPU_THRESHOLD = 80
DISK_THRESHOLD = 20
MEMORY_THRESHOLD = 500  # in MB

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent()
    if cpu_percent > CPU_THRESHOLD:
        send_alert_email("CPU Usage Alert", f"CPU usage is over {CPU_THRESHOLD}%.")

def check_disk_space():
    disk_usage = psutil.disk_usage("/")
    percent_free = disk_usage.percent
    if percent_free < DISK_THRESHOLD:
        send_alert_email("Disk Space Alert", f"Available disk space is less than {DISK_THRESHOLD}%.")

def check_memory_usage():
    available_memory = psutil.virtual_memory().available
    if available_memory < MEMORY_THRESHOLD * 1024 * 1024:  # Convert MB to bytes
        send_alert_email("Memory Usage Alert", f"Available memory is less than {MEMORY_THRESHOLD}MB.")

def check_hostname_resolution():
    try:
        socket.gethostbyname("localhost")
    except socket.gaierror:
        send_alert_email("Hostname Resolution Alert", "Cannot resolve hostname 'localhost' to '127.0.0.1'.")

def send_alert_email(subject, message):
    # Replace with your email configuration
    from_email = "your_email@example.com"
    to_email = "recipient_email@example.com"

    import smtplib
    from email.mime.text import MIMEText

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        server.sendmail(from_email, to_email, msg.as_string())

if __name__ == "__main__":
    check_cpu_usage()
    check_disk_space()
    check_memory_usage()
    check_hostname_resolution()
