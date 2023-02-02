import csv
import requests
from bs4 import BeautifulSoup

def scrape_songs():
    # Get the HTML content of the page
    page = requests.get("https://en.wikipedia.org/wiki/List_of_signature_songs")
    soup = BeautifulSoup(page.content, 'html.parser')

    # Find the table containing the song information
    table = soup.find('table', {'class': 'wikitable'})

    # Create a list to store the songs
    songs = []

    # Iterate over the rows of the table
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')

        # Get the song and artist from the table
        song = cols[1].text.strip()
        artist = cols[0].text.strip()

        # Add the song and artist to the list
        songs.append([song, artist])

    # Write the songs to a CSV file
    filename = './scrapping/songs.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Song', 'Artist'])
        writer.writerows(songs)

if __name__ == '__main__':
    scrape_songs()
