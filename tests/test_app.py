import pytest
from app import Game


def test_user_can_choose_between_english_or_romanian():
    game = Game()
    choice = "english"
    assert game.choose_language(choice) == "ENGLISH Language Selected."

def test_an_english_sentence_is_shown_in_console():
    game = Game()
    choice = "english"
    with open("english_sentences.txt", "r") as file:
        content = file.readlines()
        content = [phrase.strip() for phrase in content]
    assert game.get_random_sentence(choice) in content

def test_an_romanian_sentence_is_shown_in_console():
    game = Game()
    choice = "romanian"
    with open("romanian_sentences.txt", "r") as file:
        content = file.readlines()
        content = [phrase.strip() for phrase in content]
    assert game.get_random_sentence(choice) in content

