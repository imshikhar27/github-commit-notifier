from flask import Flask, request
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# ----------------------------
# Email Configuration
# ----------------------------
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

RECIPIENTS = [
    "imshikhar27@gmail.com",
    "bainganidarshan@gmail.com"
]


@app.route("/")
def home():
    return "Server is running!"


@app.route("/github-webhook", methods=["POST"])
def github_webhook():

    data = request.json

    # Ignore GitHub ping events
    if "zen" in data:
        print("GitHub Ping Event Received")
        return "Ping received", 200

    repo_name = data["repository"]["full_name"]
    pusher = data["pusher"]["name"]
    branch = data["ref"].split("/")[-1]

    commits = data.get("commits", [])

    for commit in commits:

        commit_message = commit["message"]
        author = commit["author"]["name"]
        commit_url = commit["url"]

        print("\n" + "=" * 50)
        print(f"Repository : {repo_name}")
        print(f"Branch     : {branch}")
        print(f"Pusher     : {pusher}")
        print(f"Message    : {commit_message}")
        print("=" * 50)

        # Create Email
        msg = EmailMessage()

        msg["Subject"] = f"[GitHub] New Commit in {repo_name}"
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(RECIPIENTS)

        msg.set_content(
            f"""
Repository : {repo_name}
Branch     : {branch}
Pusher     : {pusher}

Commit Message:
{commit_message}

Author:
{author}

Commit URL:
{commit_url}
"""
        )

        # Send Email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)

        print("Email Sent Successfully")

    return "Webhook received", 200


if __name__ == "__main__":
    app.run(port=5000)