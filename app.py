from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "Server is running!"


@app.route("/github-webhook", methods=["POST"])
def github_webhook():

    data = request.json

    # Ignore ping events
    if "zen" in data:
        print("\nGitHub Ping Event Received")
        return "Ping received", 200

    repo_name = data["repository"]["full_name"]
    pusher = data["pusher"]["name"]
    branch = data["ref"].split("/")[-1]

    print("\n" + "=" * 50)
    print(f"Repository : {repo_name}")
    print(f"Branch     : {branch}")
    print(f"Pusher     : {pusher}")

    commits = data.get("commits", [])

    for commit in commits:

        print("\nCommit:")
        print(f"Message : {commit['message']}")
        print(f"Author  : {commit['author']['name']}")
        print(f"URL     : {commit['url']}")

    print("=" * 50)

    return "Webhook received", 200


if __name__ == "__main__":
    app.run(port=5000)