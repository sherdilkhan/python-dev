import requests
from bs4 import BeautifulSoup
import csv

# Replace this list with the URLs of the websites you want to scrape
urls = ["https://codewithharry.com"]

# Create a list to hold the data for each website
data = []

# Loop through each URL and scrape its data
for url in urls:
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the title tag in the HTML content and get its text
    title = soup.find('title').get_text()

    # Find all the paragraphs in the HTML content and join their text
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    content = " ".join(paragraphs)

    # Append the data for this website to the data list
    data.append([url, title, content])

# Write the data to a CSV file
with open('website_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['URL', 'Title', 'Content'])
    writer.writerows(data)