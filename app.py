import random
import time


class TestTypingSpeed:
    supported_languages = ["ROMANIAN", "ENGLISH"]

    def choose_language(self):
        choice = ""
        while choice not in self.supported_languages:
            choice = input("Choose the type test language(English/Romanian): ")
            if choice.upper() in self.supported_languages:
                choice = choice.upper()
                print(f"{choice} Language Selected")
                self.choice = choice
                return f"{choice} Language Selected"
            else:
                print("INVALID option")

    def get_random_sentence(self):
        filepath = self.choice.upper()
        if filepath != "ENGLISH" and filepath != "ROMANIAN":
            return "No sentence for specified language"
        else:
            with open(f"{filepath.lower()}_sentences.txt", "r") as file:
                sentences = file.readlines()
            random_sentence = random.choice(sentences)
            random_sentence = random_sentence.strip()
            self.random_sentence = random_sentence
            return random_sentence

    def start_speed_test(self):
        user_input = ""
        while user_input != self.random_sentence:
            print("Type the following sentence:")
            print(self.random_sentence)
            start = time.time()
            user_input = input()
            end = time.time()
            time_elapsed = end - start
            words_in_sentence = len(self.random_sentence)
            wps = words_in_sentence / time_elapsed
            print(f"\nTime elapsed: {time_elapsed} seconds")
            print(f"Words per second: {wps} WPS")


if __name__ == "__main__":
    game = TestTypingSpeed()
    game.choose_language()
    game.get_random_sentence()
    game.start_speed_test()
