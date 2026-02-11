import requests
from bs4 import BeautifulSoup

#Need to use the headers in order for Wikipedia to allow us to pull the HTML code
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

wikipedia_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text

parsed_html_wikipedia_page = BeautifulSoup(wikipedia_html, "html5lib")

#Extract and print the page title
page_title = parsed_html_wikipedia_page.title.string
print(f"Page Title: {page_title}")

#Extract the first paragraph from mw-content-text
#We look for the main content div, then find paragraphs inside it
content_div = parsed_html_wikipedia_page.find(id="mw-content-text")

#Look for all p tags inside that div
paragraphs = content_div.find_all('p')

#Find the first paragraph that meets the 50-character requirement
first_valid_paragraph = ""

for p in paragraphs:
    #Get the text and strip extra whitespace
    text = p.get_text().strip()

    #Checking if length of paragraph is at least characters
    if len(text) >= 50:
        first_valid_paragraph = text
        break # Stop once we find the first one

#Print the result
if first_valid_paragraph:
    print("First Paragraph Found:")
    print(first_valid_paragraph)
else:
    print("No paragraph of 50 or more characters was found.")