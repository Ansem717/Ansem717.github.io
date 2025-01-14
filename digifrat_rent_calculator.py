import requests
import math

WEBHOOK_URL = "https://discord.com/api/webhooks/1323772589515997265/GywJ3jLw4LK98Swd3KeIrJsL4HdEz_r2ZcK29C9jnWDs0lpcziwNiLkCgUTxZnjzbv0J"
# WEBHOOK_URL = "https://discord.com/api/webhooks/1312424164195565659/IAc-RjAKIP6dG1jwqmuyQ2cQU1MMnLLcKopNjWSamWqQ3lXMswb2ezuYue2EAAY_bENV"

def main():

    print("\n\n#\n# Digifrat Rent Calculator\n#\n")
    months = [
        "1: January",
        "2: February",
        "3: March",
        "4: April",
        "5: May",
        "6: June",
        "7: July",
        "8: August",
        "9: September",
        "10: October",
        "11: November",
        "12: December",
    ]

    # Print the list of months
    print("Select a month by its number:")
    for month in months:
        print(month)

    # Get user input
    user_input = int(input("Enter the number of the month (1-12): "))

    # Validate input and get the month name
    selected_month = months[user_input - 1].split(": ")[1]
    print(f"You selected: {selected_month}")

    u = float(input("Utilities Total (do not divide by 6 people) > "))
    e = float(input("Electric Total > "))
    utilPerPerson = math.ceil((u/6) * 100) / 100
    elecPerPerson = math.ceil((e/6) * 100) / 100

    texts = [
        f"# Payment for {selected_month} 1st @everyone", 
        f"### Utilities: ${utilPerPerson:.2f} per person",
        f"### Electric: ${elecPerPerson:.2f} per person",
        f"",
        f"## Equal Payments for 6 people",
        f"- Everyone will pay the same amount:",
        f"  - __$3.60__ will go directly to Ethan for insurance",
        f"  - __${elecPerPerson:.2f}__ will go directly to Ethan for Electric",
        f"  - __$16__ will go directly to Andy for Wifi",
        f"  - __${(550 + utilPerPerson):.2f}__ will be paid to Redmond Place for **Rent** ($550) + **Utilities** (${utilPerPerson:.2f})",
        f"- *Total Cost for posterity: ${(3.6 + elecPerPerson + 16 + 550 + utilPerPerson):.2f}*",
    ]

    final = "\n".join(texts)

    payload = {
        "content": final
    }
    response = requests.post(WEBHOOK_URL, json=payload)
    if response.status_code == 204:
        print("Successfully posted to Discord.")
    else:
        print(f"Failed to post to Discord: {response.status_code}, {response.text}")

if __name__ == "__main__":
    main()
