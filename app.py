import random
import time


class TestTypingSpeed:
    supported_languages = ["ROMANIAN", "ENGLISH"]

    def __init__(self, language=None):
        self.choice = language or self.choose_language()

    def choose_language(self):
        choice = ""
        while choice not in self.supported_languages:
            choice = input("Choose the type test language(English/Romanian): ")
            if choice.upper() in self.supported_languages:
                choice = choice.upper()
                print(f"{choice} Language Selected")
                self.choice = choice
                return self.choice
            else:
                print("INVALID option")

    def start_speed_test(self):
        filepath = self.choice.upper()
        with open(f"{filepath.lower()}_sentences.txt", "r") as file:
            sentences = file.readlines()
        random_sentence = random.choice(sentences)
        random_sentence = random_sentence.strip()
        user_input = ""
        while user_input != random_sentence:
            print("Type the following sentence:")
            print(random_sentence)
            start = time.time()
            user_input = input()
            end = time.time()
            time_elapsed = end - start
            words_in_sentence = len(random_sentence)
            wps = words_in_sentence / time_elapsed
            print(f"\nTime elapsed: {time_elapsed} seconds")
            print(f"Words per second: {wps} WPS")


if __name__ == "__main__":
    game = TestTypingSpeed()
    game.start_speed_test()
