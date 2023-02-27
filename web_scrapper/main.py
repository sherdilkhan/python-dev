
# to scrape a website, there is two ways:
# 1. Use API (if given)
# 2. Use HTML Web Scrapping using tools like bs4 (beautiful Soup Python)


import requests

from bs4 import BeautifulSoup

# Step 1: lets create a URL varaible
url = 'https://codewithharry.com'
# Step 2: get the conent of above URL
r = requests.get(url)
htmlContent = r.content
# Step 3: parse the HTML conent
soup = BeautifulSoup(htmlContent, 'html.parser')
# Step 4: HTML Tree traversal

title = soup.title

paras = soup.find('p')

print(title)
print(paras)
