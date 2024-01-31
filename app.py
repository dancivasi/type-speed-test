import random
import time


class Game:

    @staticmethod
    def choose_language(choice):
        choice = choice.upper()
        if choice == "ENGLISH":
            return f"{choice} Language Selected."
        else:
            return f"{choice} Language Selected."

    @staticmethod
    def get_random_sentence(choice):
        filepath = choice.upper()
        with open(f"{filepath.lower()}_sentences.txt", "r") as file:
            sentences = file.readlines()
        random_sentence = random.choice(sentences)
        random_sentence = random_sentence.strip()
        return random_sentence

    @staticmethod
    def type_speed_test(sentence, user_input ):
        while user_input != sentence:
            user_input = input()




if __name__ == "__main__":
    game = Game()
    choice = input("Choose language of the type-test:(romanian/english)")
    sentence = game.get_random_sentence(choice)
    print("Type the following sentence:")
    print(sentence)
    user_input = ""
    start = time.time()
    game.type_speed_test(sentence, user_input)
    end = time.time()
    elapsed_time = end - start
    print(f"\nTime elapsed: {elapsed_time} seconds")

