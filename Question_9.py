import csv
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Machine_learning"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, features="html.parser")

content_div = soup.find("div", id="mw-content-text")

#Find first table with at least 3 data rows
target_table = None

for table in content_div.find_all("table"):
    rows = table.find_all("tr")
    data_row_count = 0

    for r in rows:
        if r.find_all(["td", "th"]):
            data_row_count += 1

    if data_row_count >= 3:
        target_table = table
        break

if not target_table:
    print("No table with at least 3 rows found")
    exit(1)

rows = target_table.find_all("tr")

#Find row with th tags to use as header
header_row_index = -1
headers = None

for i, r in enumerate(rows):
    th_cells = r.find_all("th")
    if th_cells:
        headers = [h.get_text(" ", strip=True) for h in th_cells]
        header_row_index = i
        break

#If no th found, create col x headers
if headers is None:
    max_cols = 0
    for r in rows:
        cols = r.find_all(["td", "th"])
        max_cols = max(max_cols, len(cols))
    headers = [f"col{i + 1}" for i in range(max_cols)]

#Determine max columns
max_cols = len(headers)


data = []

for i, r in enumerate(rows):
    if i == header_row_index:
        continue

    cells = r.find_all(["th", "td"])
    if not cells:
        continue

    row_text = [c.get_text(" ", strip=True) for c in cells]

    #Pad missing columns with empty strings
    if len(row_text) < max_cols:
        row_text += [""] * (max_cols - len(row_text))
    elif len(row_text) > max_cols:
        row_text = row_text[:max_cols]

    data.append(row_text)

#Write to csv
with open("wiki_table.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(data)

print("Saved table to wiki_table.csv")
print(f"Rows saved: {len(data)}")
