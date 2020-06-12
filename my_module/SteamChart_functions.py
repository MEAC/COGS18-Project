"""A collection of function for doing my project."""
# Took many of the basic functions and comments from A3 Chatbot
import requests
import string
import random
import numpy as np
import webbrowser

from bs4 import BeautifulSoup
from time import sleep

class web_scrape:
    """
    The process in how we web scrape information from the website we want
    """
    # Create empty lists for all the data we are storing from webpage
    top_games_names = []
    top_games_current_players = []
    top_games_peak_players = []
    top_games_hours_played_30days = []

    # Needed to loop through pages 1 to 40
    # Code taken from and inspired by https://bit.ly/30uch6O
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


        # Parse through and get information we want from the 
        # HTML markup language
        for games in top_games_table.find_all('tbody'):
            rows = games.find_all('tr')
            for row in rows:
                top_games_names.append(row.find('td', 
                class_ = 'game-name left').text.strip())

                top_games_current_players.append(row.find('td', 
                class_ = 'num').text)

                top_games_peak_players.append(row.find('td', 
                class_ = 'num period-col peak-concurrent').text)

                top_games_hours_played_30days.append(row.find('td', 
                class_ = 'num period-col player-hours').text)    

def is_question(input_string):
    """
    Function to determine if the input contains '?'
    Function taken from A3

    Inputs: 
        string
    Outputs: 
        string
    """
    if '?' in input_string:
        output = True
        return output
    else:
        output = False
        return output

def is_greeting(input_string):
    """
    Function to determine if the input includes a greeting from the
    GREETINGS_IN list
    Inspired from A3

    Inputs: 
        string
    Outputs: 
        string
    """
    for i in input_string:
        if i in GREETINGS_IN:
            output = selector(input_string, GREETINGS_IN, GREETINGS_OUT)
        else:
            output = None
    return output
    
def is_non_steam_platform(input_string):
    """
    Function to determine if the input includes a platform that is in the
    PLATFORMS_THAT_ARE_NOT_STEAM_IN list
    Inspired from A3

    Inputs: 
        string
    Outputs: 
        string
    """
    for i in input_string:
        if i in PLATFORMS_THAT_ARE_NOT_STEAM_IN:
            output = selector(input_string, PLATFORMS_THAT_ARE_NOT_STEAM_IN,
                              PLATFORMS_THAT_ARE_NOT_STEAM_OUT)
        else:
            output = None
    return output

def remove_punctuation(input_string):
    """
    Function to remove punctuation once we know it is a question
    Function taken from A3

    Inputs: 
        string
    Outputs: 
        string
    """
    out_string = ''
    for i in input_string:
        if i not in string.punctuation:
            out_string += i
    return out_string

def prepare_text(input_string):
    """
    Function to split string into list
    Function taken from A3

    Inputs: 
        string
    Outputs: 
        list of strings
    """
    temp_string = input_string
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list

def selector(input_list, check_list, return_list):
    """
    Function to randomly choose from a list
    Function taken from A3

    Inputs: 
        string, string, string
    Outputs: 
        string
    """
    output = None
    for i in input_list:
        if i in check_list:
            output = random.choice(return_list)
            break
    return output

def string_concatenator(string1, string2, separator):
    """
    Function to concatenate two strings
    Function taken from A3

    Inputs: 
        list, list, list
    Outputs: 
        string
    """
    output = string1 + separator + string2
    return output

def list_to_string(input_list, separator):
    """
    Function to turn a list of strings into a concatenated string
    Function taken from A3

    Inputs: 
        list of strings, string
    Outputs: 
        string
    """
    output = input_list[0]
    for i in input_list[1:]:
        output = string_concatenator(output, i, separator)
    return output

def end_chat(input_string):
    """
    Takes user input and checks if equal to 'quit' or 'exit'
    Function taken from A3

    Input: string
    Output: boolean
    """
    for i in input_string:
        if i == 'quit' or i == 'exit':
            return True
        else:
            return False

def is_in_list(list_one, list_two):
    """
    Function to check if an element in list_one is in list_two
    Function taken from A3

    Inputs: 
        list, list
    Outputs: 
        boolean
    """
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """
    Function to find an element from list_one that is in list_two 
    and returns it. Returns None if nothing is found.
    Function taken from A3

    Inputs: 
        list, list
    Outputs: 
        string or None
    """
    
    for element in list_one:
        if element in list_two:
            return element
    return None

def is_link(input_string):
    """
    Takes user input and checks if equal to 'games'

    Input: string
    Output: boolean
    """
    if input_string == 'games':
        return True
    else:
        return False

# Topics inspired by A3
GREETINGS_IN = ['hello', 'hi', 'hey', 'greetings']
GREETINGS_OUT = ['Hello, got any games you want information on?',
                 "Let's talk about some games!"]

USER_INPUTED_GAMES_IN = ['games']
USER_INPUTED_GAMES_OUT = ['Have fun looking at the list of Steam games.']

USER_INPUTED_STEAM_IN = ['steam', 'Steam']
USER_INPUTED_STEAM_OUT = ['Steam is a video game digital distrubtion ' +
                          'service by the company Valve where users ' +
                          'can buy and play video games']

PLATFORMS_THAT_ARE_NOT_STEAM_IN = ['Battle.net', 'Discord', 'Origin', 'Uplay',
                                   'GOG', 'Green Man Gaming', 'Humble Store', 
                                   'EPIC']
PLATFORMS_THAT_ARE_NOT_STEAM_OUT = ['This bot only works with Steam', 
                                    'Why are you mentioning other platforms',
                                    "Please don't input other platforms"]

PEOPLE_IN = ['Newell', 'Kojima', 'Howard', 'Persson']
PEOPLE_OUT = ['is a video game developer', 'knows how to create amazing games']
PEOPLE_NAMES = {'Newell': 'Gabe', 'Kojima': 'Hideo', 'Howard': 'Todd',
                'Persson': 'Markus'}

UNKNOWN = ["Umm... That's not a game on Steam.", 
          'Do you know what a Steam game is?', 
          "That games doesn't look like it's in our charts at the moment...",
          "You know you can type 'games' for a list of games on Steam if " + 
          "you're lost..."]

QUESTION = "I can't answer every question. Ask me about a game!"


        
def have_a_chat():
    """
    Main function used to run our chatbot.
    Partially used code and comments from A3.
    """
    greeting_msg = '''Welcome to the Steam charts bot! 
I love to track the data on all of the
top games people are playing right now on Steam!!!
Input a video game that is avaliable on Steam.\n'''
    print(greeting_msg)

    open_games_webpage = '''If you would like to load
a list of all Steam games please type 'games'\n'''
    print(open_games_webpage)

    please_wait_msg = '''
Please give me 50 seconds to grab a list of the current
top games on Steam!\n'''
    print(please_wait_msg)

    # Call the web_scrape class and create the object
    # website
    website = web_scrape()

    # Number of times user has inputed into bot
    times_through_chat = 0

    chat = True
    
    while chat:
        # Get a message from the user
        msg = input('INPUT :\t')
        out_msg = None

        times_through_chat += 1

        # Check if user input is identical to 'games' and if so opens up 
        # website in current browser
        if is_link(msg):
            webbrowser.open('https://steamcharts.com/top')
            
        
        # Check if user input is in our games list
        # If user input is in list then output information
        if msg in website.top_games_names:
            index_of_game = website.top_games_names.index(msg)
            print('OUTPUT:', 'Looks like', msg, 
                  'is in the top 1000 charts right now!')
                  
            print('OUTPUT:', 'There are also',
                  website.top_games_current_players[index_of_game], 
                  'players playing currently')
                  
            print('OUTPUT:', 'The peak amount of players logged on today is',
                  website.top_games_peak_players[index_of_game])
                  
            print('OUTPUT:', 'In the past 30 days people have played for',
                  website.top_games_hours_played_30days[index_of_game], 
                  'hours \n')

            is_link(msg) == True
        
        # Checks to see if user has inputed to the bot 2 times
        if times_through_chat == 2:
            print("***NOTICE*** If you would like to exit the chat " +
                  "type 'exit'\n")

        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check if message is 'exit' or 'quit'. Exectues if True.
        if end_chat(msg):
            out_msg = 'Come back soon!!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        # Here, we will check for a series of topics that we have designed to 
        # answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output 
            # if so
            outs.append(is_greeting(msg))

            # Check if the input is a platform other than Steam, add a message 
            # saying to only discuss about Steam
            outs.append(is_non_steam_platform(msg))

            # Check if the input is 'games'. Outputs a kind message if so
            outs.append(selector(msg, USER_INPUTED_GAMES_IN,
                                 USER_INPUTED_GAMES_OUT))

            # Check if the input is 'steam'. Outputs a message describing what 
            # steam is
            outs.append(selector(msg, USER_INPUTED_STEAM_IN,
                                 USER_INPUTED_STEAM_OUT))
            
            # Check if the input mentions a person that is specified, add a 
            # person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name],
                                            name.capitalize(),
                                            selector(msg, PEOPLE_IN,
                                            PEOPLE_OUT)], ' '))

            # We could have selected multiple outputs from the topic search 
            # above (if multiple return possible outputs).
            # We also might have appended None in some cases, meaning we don't 
            # have a reply.
            # To deal with this, we are going to randomly select an output 
            # from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return 
        # msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)

        print('OUTPUT:', out_msg)
