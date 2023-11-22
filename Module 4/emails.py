#!/usr/bin/env python3
import smtplib


def generate(sender, recipient, subject, body, attachment_path="none"):
    from email.message import EmailMessage
    message = EmailMessage()
    # print(message)

    message['From'] = sender
    message['To'] = recipient
    # print(message)

    message['Subject'] = subject
    message.set_content(body)

    if (attachment_path != "none"):
        import os.path
        attachment_filename = os.path.basename(attachment_path)
        import mimetypes
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)

        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                   maintype=mime_type,
                                   subtype=mime_subtype,
                                   filename=os.path.basename(attachment_path))

    return message


def send_email(message, sender="none", mail_pass="none"):
    mail_server = smtplib.SMTP("localhost")
    mail_server.set_debuglevel(1)

    if (mail_pass != "none"):
        mail_server.login(sender, mail_pass)

    mail_server.send_message(message)
    mail_server.quit()
