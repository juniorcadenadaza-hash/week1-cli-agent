import os
from datetime import date
from urllib.parse import quote

import requests


BASE_ID = os.getenv("AIRTABLE_BASE_ID")
TOKEN = os.getenv("AIRTABLE_TOKEN")
TABLE_NAME = "Ideas Backlog"


def create_idea():
    if not BASE_ID or not TOKEN:
        print("Missing Airtable environment variables.")
        print("Please set AIRTABLE_BASE_ID and AIRTABLE_TOKEN.")
        return

    encoded_table_name = quote(TABLE_NAME)
    url = f"https://api.airtable.com/v0/{BASE_ID}/{encoded_table_name}"

    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "records": [
            {
                "fields": {
                    "Title": "First API idea",
                    "Topic": "Python automation",
                    "Status": "New",
                    "Created": date.today().isoformat(),
                }
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    print(f"Status code: {response.status_code}")
    print(response.json())


create_idea()