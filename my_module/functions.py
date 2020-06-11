"""A collection of function for doing my project."""
import requests
import string
import random
import numpy as np
#import sys

from bs4 import BeautifulSoup
from time import sleep

# Create empty lists for all the data we are storing from webpage
class WebScrape:
    top_games_names = []
    top_games_current_players = []
    top_games_peak_players = []
    top_games_hours_played_30days = []

    # Needed to loop through pages 1 to 40
    pages = np.arange(1, 10)

    for page in pages:

        # Get the url we are scraping from including the page
        url = 'https://steamcharts.com/top/p.' + str(page)
        response = requests.get(url)

        # HTML parsing
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the table we want to get information from
        top_games_table = soup.find('table', class_ = 'common-table')

        # Wait 1 second after scraping from one page in order to avoid
        # asking the server for multiple requests in too short of a time
        # to avoid getting our IP address in trouble.
        #sleep(1)


        # Parse through and get information we want from the HTML markup language
        for games in top_games_table.find_all('tbody'):
            rows = games.find_all('tr')
            for row in rows:
                top_games_names.append(row.find('td', class_ = 'game-name left').text.strip())
                top_games_current_players.append(row.find('td', class_ = 'num').text)
                top_games_peak_players.append(row.find('td', class_ = 'num period-col peak-concurrent').text)
                top_games_hours_played_30days.append(row.find('td', class_ = 'num period-col player-hours').text)
