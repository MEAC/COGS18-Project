"""Test for my functions in SteamChart_functions."""
from my_module.SteamChart_functions import *

def test_is_question():
    """Function does some tests to the is_question function"""
    assert isinstance(is_question('lol'), bool)
    assert is_question('test?') == True
    assert callable(is_question)

def test_is_greeting():
    """Function does some tests to the is_greeting function"""
    test1 = 'Hello, got any games you want information on?'
    test2 = "Let's talk about some games!"
    assert isinstance(is_greeting(['hi']), str)
    assert is_greeting(['hi']) == test1 or test2
    assert callable(is_greeting)

def test_is_non_steam_platform():
    """Function does some tests to the is_non_steam_platform function"""
    test1 = 'This bot only works with Steam'
    test2 = 'Why are you mentioning other platforms'
    test3 = "Please don't input other platforms"
    assert isinstance(is_non_steam_platform(['Origin']), str)
    assert is_non_steam_platform(['Origin']) == test1 or test2 or test3
    assert callable(is_non_steam_platform)

def test_remove_punctuation():
    """Function does some tests to the remove_punctuation function"""
    assert isinstance(remove_punctuation('test'), str)
    assert remove_punctuation('h!ello there') == 'hello there'
    assert callable(remove_punctuation)

def test_prepare_text():
    """Function does some tests to the prepare_text function"""
    assert isinstance(prepare_text('a test'), list)
    assert prepare_text('a test') == ['a', 'test']
    assert callable(prepare_text)

def test_selector():
    """Function does some tests to the selector function"""
    assert selector(['a', 'test'], ['lol'], ['cool']) == None
    assert selector(['a', 'test'], ['test'], ['cool']) == 'cool'
    assert callable(selector)

def test_string_concatenator():
    """Function does some tests to the string_concatenator function"""
    assert isinstance(string_concatenator('a', 'test', ' '), str)
    assert string_concatenator('a', 'test', ' ') == 'a test'
    assert callable(string_concatenator)

def test_list_to_string():
    """Function does some tests to the list_to_string function"""
    assert isinstance(list_to_string(['a', 'test'], ' '), str)
    assert list_to_string(['a', 'test'], ' ') == 'a test'
    assert callable(list_to_string)

def test_end_chat():
    """Function does some tests to the end_chat function"""
    assert isinstance(end_chat('a test'), bool)
    assert end_chat(['a test']) == False
    assert end_chat(['quit']) == True
    assert callable(end_chat)

def test_is_in_list():
    """Function does some tests to the is_in_list function"""
    assert isinstance(is_in_list(['a test'], ['a test']), bool)
    assert is_in_list(['a test'], ['a test']) == True
    assert callable(is_in_list)

def test_find_in_list():
    """Function does some tests to the find_in_list function"""
    assert isinstance(find_in_list(['a test'], ['a test']), str)
    assert find_in_list(['a test'], ['a test']) == 'a test'
    assert callable(find_in_list)

def test_is_link():
    """Function does some tests to the is_link function"""
    assert isinstance(is_link('games'), bool)
    assert is_link('games') == True
    assert callable(is_link)

def run_all_tests():
    """Function that runs all of the test functions"""
    test_is_question()
    test_is_greeting()
    test_is_non_steam_platform()
    test_remove_punctuation()
    test_prepare_text()
    test_selector()
    test_string_concatenator()
    test_list_to_string()
    test_end_chat()
    test_is_in_list()
    test_find_in_list()
    test_is_link()
