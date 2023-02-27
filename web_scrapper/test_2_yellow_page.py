import requests
from bs4 import BeautifulSoup
import csv

# Replace this URL with the URL of the yellow page website you want to scrape
url = "https://www.yellowpages.ca/"

# Replace this person's name with the name you want to search for
person_name = "John Doe"

# Send a GET request to the yellow page website with the person's name as the search query
response = requests.get(url + "/search?search_terms=" + person_name)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the listings in the search results
listings = soup.find_all('div', {'class': 'search-results organic'})

# Create a list to hold the data for each listing
data = []

# Loop through each listing and scrape its data
for listing in listings:
    # Find the name and contact information for this listing
    name = listing.find('a', {'class': 'business-name'}).get_text()
    phone = listing.find('div', {'class': 'phones'}).get_text()

    # Append the data for this listing to the data list
    data.append([name, phone])

# Write the data to a CSV file
with open('yellowpages_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Phone'])
    writer.writerows(data)
