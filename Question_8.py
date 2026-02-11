import requests
from bs4 import BeautifulSoup

#Need to use the headers in order for Wikipedia to allow us to pull the HTML code
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

wikipedia_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text




soup = BeautifulSoup(wikipedia_html, "html5lib")

#Target the main content area
content_div = soup.find("div", id="mw-content-text")

#List of words to exclude
exclude_list = ["References", "External links", "See also", "Notes"]

#Find all <h2> tags inside that div
headings = content_div.find_all("h2")

valid_headings = []

for h2 in headings:
    # Get the text and remove the "[edit]" suffix
    text = h2.get_text().replace("[edit]", "").strip()

    #Check if the heading contains any of the forbidden words
    if not any(word in text for word in exclude_list):
        if text:  # Ensure we don't save empty lines
            valid_headings.append(text)

# 4. Save the headings to a text file
with open("headings.txt", "w") as f:
    for item in valid_headings:
        f.write(item + "\n")

print(f"Extraction complete. {len(valid_headings)} headings saved to headings.txt.")
