import random
import time


class Game:

    @staticmethod
    def choose_language(choice):
        choice = choice.upper()
        if choice != "ENGLISH" and choice != "ROMANIAN":
            return "INVALID option"
        if choice == "ENGLISH":
            return f"{choice} Language Selected"
        else:
            return f"{choice} Language Selected"

    @staticmethod
    def get_random_sentence(choice):
        filepath = choice.upper()
        if filepath != "ENGLISH" and filepath != "ROMANIAN":
            return "No sentence for specified language"
        with open(f"{filepath.lower()}_sentences.txt", "r") as file:
            sentences = file.readlines()
        random_sentence = random.choice(sentences)
        random_sentence = random_sentence.strip()
        return random_sentence

    @staticmethod
    def type_speed_test(sentence):
        user_input = ""
        while user_input != sentence:
            print("Type the following sentence:")
            print(sentence)
            start = time.time()
            user_input = input()
            end = time.time()
            time_elapsed = end - start
            words_in_sentence = len(sentence)
            wps = words_in_sentence / time_elapsed
            print(f"\nTime elapsed: {time_elapsed} seconds")
            print(f"Words per second: {wps} WPS")


if __name__ == "__main__":
    game = Game()
    choice = input("Alege limba pentru type test(Romanian/English):")
    print(game.choose_language(choice))
    sentence = (game.get_random_sentence(choice))
    game.type_speed_test(sentence)
