import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html5lib")

#Locate the main content div
content_div = soup.find("div", id="mw-content-text")

#Find all tables and filter for the first one with >= 3 data rows
target_table = None
for table in content_div.find_all("table"):
    # Count rows that are not headers (contain <td> tags)
    rows = table.find_all("tr")
    data_rows = [row for row in rows if row.find("td")]

    if len(data_rows) >= 3:
        target_table = table
        break

if target_table:
    #Extract Headers
    header_tags = target_table.find_all("th")
    if header_tags:
        headers = [th.get_text(strip=True) for th in header_tags]
    else:
        #If no th peek at the first data row to determine column count
        first_row = target_table.find("tr").find_all(["td", "th"])
        headers = [f"col{i + 1}" for i in range(len(first_row))]

    #Extract Rows and Pad Missing Values
    all_data = []
    num_cols = len(headers)

    #Iterate through all table rows
    for tr in target_table.find_all("tr"):
        cells = tr.find_all(["td", "th"])

        #Skip the header row if we already processed it
        if not cells or (header_tags and all(c in header_tags for c in cells)):
            continue

        row_data = [c.get_text(strip=True) for c in cells]

        #Pad with empty strings if the row is too short
        while len(row_data) < num_cols:
            row_data.append("")

        #Truncate if the row is somehow too long
        row_data = row_data[:num_cols]

        all_data.append(row_data)

    #Save to CSV using pandas
    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv("wiki_table.csv", index=False)
    print("Table successfully saved to wiki_table.csv")
else:
    print("No suitable table found.")