import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1312424164195565659/IAc-RjAKIP6dG1jwqmuyQ2cQU1MMnLLcKopNjWSamWqQ3lXMswb2ezuYue2EAAY_bENV"

def main():
    payload = {
        "content": f"# Posted from Github Cron Schedule",
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Successfully posted to Discord.")
    else:
        print(f"Failed to post to Discord: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()
