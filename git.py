import requests
from bs4 import BeautifulSoup

# Make a request to the website
r = requests.get("https://www.example.com")
r.content

# Parse the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Extract all headings
headings = soup.find_all('h1') + soup.find_all('h2') + soup.find_all('h3')

# Print the headings
for heading in headings:
    print(heading.text)