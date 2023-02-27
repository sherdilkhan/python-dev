
import requests
from bs4 import BeautifulSoup
import openpyxl

excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = 'Top 250 TV Series'


sheet.append(['Rank', 'Title', 'Year of Release', 'IMDB Rating'])

try:
    source = requests.get('https://www.imdb.com/chart/toptv/') # source is HTML content string / response object
    source.raise_for_status() # if above URL is not active

    soup = BeautifulSoup(source.text, 'html.parser')
    tvShows = soup.find('tbody', class_= 'lister-list').find_all('tr')

    for tvShow in tvShows:

        title =   tvShow.find('td', class_='titleColumn').a.text

        rank =   tvShow.find('td', class_='titleColumn').get_text(strip=True).split('.')[0]

        year =   tvShow.find('td', class_='titleColumn').span.text.strip('()')

        rating = tvShow.find('td', class_='ratingColumn imdbRating').strong.text

        print(rank, title, year, rating)
        sheet.append([rank, title, year, rating])


except Exception as e:
    print(e)

excel.save('IMDB Top TV Series.xlsx')