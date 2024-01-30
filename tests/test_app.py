import pytest
from app import Game
def test_user_can_choose_between_english_or_romanian():
    game = Game()
    choice = "english"
    assert game.choose_language(choice) == "ENGLISH Language Selected."

def test_a_sentence_is_shown_in_console():
    game = Game()
    choice = "english"
    assert game.get_random_sentence(choice) == "As the sun dipped below the horizon, the city lights flickered to life, transforming the urban landscape into a sea of brilliance."