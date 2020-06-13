# COGS 18 - Final Project

## Description
This is a chat bot uses many of the basic functions from A3 Chatbot. Although it uses lots of functions we wrote in A3 it behaves differently from the one we made. What makes this chat bot different from the one in assignment 3 is how it web scrapes information from the website 'https://steamcharts.com/ '. This website has information about all the top played games on Steam. 

Steam is a video game digital distribution service by the company Valve where users can buy and play video games in the Steam library. Steam collects data on how many users are playing games on their service. The website that I web scraped is a website that is not affiliated with Steam, but neatly shows information about every game on Steam. The point of this chat bot is to know information about how popular specific games on the Steam platform are doing.

When asked to input a game name the program will output a good amount of information including:
- Current players playing at the given moment
- Peak amount of players throughout the current day
- Total number of hours Steam users in total played the game in 30 days

## Examples:
Here are some of the more popular games avaliable on Steam if you want to check out the statistics on them:

- Counter-Strike: Global Offensive
- Dota 2
- PLAYERUNKNOWN'S BATTLEGROUNDS
- Destiny 2

## Notes to consider:
- **When you run (from my_module.SteamChart_functions import *) and the pytest, it will take a couple seconds before you can run the have_a_chat function to run due to parsing through 20 web pages.**
    - **Please be patient and give the code time to run.**

- **Please note that the user MUST input the exact name of the game title from Steam.**

- **If the data that the bot outputs doesn't correlate with the steamcharts website then restart your notebook and try again.**

- **This project requires 'requests' and 'numpy'**
