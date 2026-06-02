import os
import random
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

if not os.environ.get("SLACK_BOT_TOKEN") or not os.environ.get("SLACK_APP_TOKEN"):
    print("Error: Missing SLACK_BOT_TOKEN or SLACK_APP_TOKEN in .env file.")
    exit(1)

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# --- CLASSIFIED RELIC DATA ---
FORBIDDEN_RELICS = [
    "📼 A cracked plastic cassette tape labeled 'Classic Rock Mix 1998'. It hums faintly with static electricity.",
    "📷 A broken digital camera containing a corrupted file showing a blue sky and green grass. Heavily subversive.",
    "🪙 A small silver coin dated 2024 with a strange profile of an eagle. Clearly prehistoric currency.",
    "📖 An antique picture book titled 'The Ocean Ecosystem'. It describes massive bodies of untamed water. Highly dangerous."
]

# --- SECURITY PRIVILEGES ---
# ⚠️ Make sure this is exactly your User ID from Slack (all uppercase in your assignment)
HEAD_OF_IT_ID = "@U071ABCDE" 

# --- CORE EVENTS ---

@app.event("app_mention")
def handle_mainframe_requests(event, say):
    user_id = event.get('user')
    raw_text = event.get('text', '')
    text = raw_text.lower()
    
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

    # FEATURE 3: THE RESTRICTED RELIC REPOSITORY (RBAC LAYER)
    elif "scavenge" in text or "relic" in text:
        if user_id.upper() == HEAD_OF_IT_ID.upper():
            secure_relic = random.choice(FORBIDDEN_RELICS)
            say(
                f"📟 `[OVERRIDE ACCEPTED: HEAD OF IT CLEARANCE RECORDED]`\n"
                f"📂 *Accessing Vault Section 18-F...*\n"
                f"You successfully scavenged a relic from the Deep Down:\n"
                f"> {secure_relic}"
            )
        else:
            say(
                f"❌ **ACCESS DENIED.** <@{user_id}>, you do not possess administrative clearance "
                f"to scavenge the Deep Down. This unauthorized inquiry has been flagged as suspicious behavior."
            )

    # DEFAULT FALLBACK RESPONDER
    else:
        say(
            f"📟 **Silo IT Mainframe Online.**\n"
            f"Greetings citizen <@{user_id}>. Your transmissions are being logged.\n"
            f"Available protocols: Mention me with `status`, `scavenge`, or `outside`."
        )

if __name__ == "__main__":
    # 📡 Create a lightweight HTTP server so Render's Free Tier web-service stays alive
    def run_fake_web_server():
        port = int(os.environ.get("PORT", 8080))
        server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
        print(f"📡 Free Tier Web Port Activator listening on port {port}...")
        server.serve_forever()

    # Start web thread
    threading.Thread(target=run_fake_web_server, daemon=True).start()

    print("⚡️ Silo IT Terminal booting up from the Deep Down...")
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()