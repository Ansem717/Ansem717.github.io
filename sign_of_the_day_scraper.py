import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

WEBSITE_URL = "https://www.signingsavvy.com/signoftheday" 

def fetch_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        video = soup.find('link', {'as': 'video'})['href']

        title_section = soup.find('div', {'class': 'signing_header'})
        title = title_section.find('h2').get_text()
        context = title_section.find('h3')
        if context is not None:
            context = context.get_text()

        return video, title, context
    except Exception as e:
        print(f"Error fetching webpage content: {e}")
        return None


def post_to_discord(video, title, context):

    header = "# Sign Of The Day \n"
    title_content = f"## {title}"
    if context is None:
        with_context = ""
    else:
        with_context = f"\n*{context}*\n"
    signature = f"\n-# [-]({video}) [From SigningSavvy.com](<{WEBSITE_URL}>)"

    final = header + title_content + with_context + signature

    payload = {
        "content": final
    }

    load_dotenv()
    WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_SIGN_OF_THE_DAY")
    # WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_TEST_HOOK")

    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Successfully posted to Discord.")
    else:
        print(f"Failed to post to Discord: {response.status_code}, {response.text}")


def main():
    video, title, context = fetch_webpage_content(WEBSITE_URL)
    if video and title:
        post_to_discord(video, title, context)


if __name__ == "__main__":
    main()
