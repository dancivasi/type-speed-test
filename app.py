import random

class Game():

    def choose_language(self, choice):
        choice = choice.upper()
        if choice == "ENGLISH":
            return f"{choice} Language Selected."
        else:
            return f"{choice} Language Selected."

    def get_random_sentence(self, choice):
        filepath = choice.upper()
        with open(f"{filepath.lower()}_sentences.txt", "r") as file:
            sentences = file.readlines()
        random_sentence = random.choice(sentences)
        random_sentence = random_sentence.strip()
        return random_sentence

    