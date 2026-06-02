import os
import random
from dotenv import load_dotenv
from slack_bolt import App  # Fixed: Imported App cleanly from slack_bolt
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Load local environment variables safely
load_dotenv()

if not os.environ.get("SLACK_BOT_TOKEN") or not os.environ.get("SLACK_APP_TOKEN"):
    print("Error: Missing SLACK_BOT_TOKEN or SLACK_APP_TOKEN in .env file.")
    exit(1)

# Initialize the Slack Engine
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# --- CORE EVENTS ---

@app.event("app_mention")
def handle_mainframe_requests(event, say):
    user_id = event.get('user')
    raw_text = event.get('text', '')
    text = raw_text.lower()  # Normalize to lower-case for keyword scanning
    
    print(f"📟 Terminal intercepting request from <@{user_id}>: '{raw_text}'")

    # FEATURE 1: MECHANICAL DEPT DIAGNOSTICS
    if "status" in text or "diagnostic" in text:
        say(
            f"```\n"
            f"=== SILO MAIN ENGINE TERMINAL REBOOT ===\n"
            f"• STRUCTURAL STATUS: 144 Levels Nominal\n"
            f"• MECHANICAL DEPT: Steam pressure stable (410 PSI)\n"
            f"• AIR FILTRATION: Axial fan flow rates at 94%\n"
            f"========================================\n"
            f"System monitoring active 24/7. Keep the steam flowing.```"
        )

    # FEATURE 2: THE OUTSIDE INTERACTIVE WARNING ALERT (BLOCK KIT)
    elif "outside" in text or "leave" in text or "cleaning" in text:
        say(
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "⚠️ PACT VIOLATION DETECTED ⚠️",
                        "emoji": True
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f"*Attention Citizen <@{user_id}>:*\nYour recent inquiry regarding the exterior infrastructure or unauthorized evacuation protocols constitutes a severe infraction against *Section 4, Article 2 of the Pact*."
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text": "🚨 _Status: Transcript automatically forwarded to Judicial Security Sub-stations. Do not look at the lens._"
                        }
                    ]
                }
            ]
        )

    # DEFAULT FALLBACK RESPONDER
    else:
        say(
            f"📟 **Silo IT Mainframe Online.**\n"
            f"Greetings citizen <@{user_id}>. Your transmissions are being logged.\n"
            f"Available protocols: Mention me with `status` for a system readout."
        )

if __name__ == "__main__":
    print("⚡️ Silo IT Terminal booting up from the Deep Down...")
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()