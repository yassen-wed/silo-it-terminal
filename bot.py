import os
from dotenv import load_dotenv
from slack_bot import app
from slack_bot.adapter.socket_mode import SocketModeHandler

load_dotenv()

if not os.environ.get("SLACK_BOT_TOKEN") or not os.environ.get("SLACK_APP_TOKEN"):
    print("Error: Missing SLACK_BOT_TOKEN or SLACK_APP_TOKEN in .env file.")
    exit(1)

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.event("app_mention")
def reply_to_mention(event, say):
    user_id = event.get('user')
    say(f"Hey <@{user_id}>! I am wide awake and on duty 24/7. No slacking off here! 🚀")

if __name__ == "__main__":
    print("⚡️ Starting Slack Bot in Socket Mode...")
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()

    print("✅ Bot is running and listening for mentions!")
