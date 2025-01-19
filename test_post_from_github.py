import requests
import os
from dotenv import load_dotenv

def main():
    payload = {
        "content": f"# Posted from Github Cron Schedule",
    }

    load_dotenv()
    WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_TEST_HOOK")

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Successfully posted to Discord.")
    else:
        print(f"Failed to post to Discord: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()
