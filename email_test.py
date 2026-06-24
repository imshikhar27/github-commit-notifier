import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "imshikhar27@gmail.com"
APP_PASSWORD = "zykl yakz tuyg boph"

RECIPIENT_EMAIL = "imshikhar27@gmail.com"

msg = EmailMessage()

msg["Subject"] = "Python Email Test"
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL

msg.set_content(
    """
Hello Shikhar,

This email was sent from Python using Gmail SMTP.

Regards,
GitHub Commit Notifier
"""
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER_EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("Email sent successfully!")