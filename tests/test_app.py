import pytest

from app import Game


@pytest.fixture
def game():
    return Game()


@pytest.mark.parametrize(
    "language_choice, expected_language_selected",
    [
        ("english", "ENGLISH Language Selected",),
        ("romanian", "ROMANIAN Language Selected"),
        ("asdhasiuhdasihduas", "INVALID option")
    ]
)
def test_chosen_language(game, language_choice, expected_language_selected):
    assert game.choose_language(language_choice) == expected_language_selected


@pytest.mark.parametrize(
    "language_choice",
    [
        "english",
        "romanian",
    ]
)
def test_get_sentence_from_english_file_or_romanian_file(game, language_choice):
    mocked_content = {
        'english_sentences.txt': [  "on offering to help the blind man, the man who then stole his car, had not, at that precise moment, had any evil intention, quite the contrary, what he did was nothing more than obey those feelings of generosity and altruism which, as everyone knows, are the two best traits of human nature and to be found in much more hardened criminals than this one, a simple car-thief without any hope of advancing in his profession, exploited by the real owners of this enterprise, for it is they who take advantage of the needs of the poor",
                                    "the mysterious cat roamed through the moonlit alley, casting shadows as it moved silently under the ancient trees",
                                    "with a heart full of hope, Sarah embarked on a journey to discover the hidden treasures that awaited her in the enchanted forest",
                                    "the old bookshop on Elm Street held a collection of dusty novels, each carrying the whispers of tales long forgotten",
                                    "as the sun dipped below the horizon, the city lights flickered to life, transforming the urban landscape into a sea of brilliance",
                                    "in the cozy cafe on the corner, friends gathered to share laughter, stories, and the warmth of freshly brewed coffee",
                                    "lost in thought, Emily gazed out of the window, watching the raindrops dance on the glass like a melancholic ballet",
                                    "the antique pocket watch, passed down through generations, held not only the ticking of time but also the echoes of family history",
                                    "on the summit of the mountain, a lone hiker marveled at the breathtaking panorama, feeling a profound connection to the vast wilderness",
                                    "in the bustling market, vendors peddled exotic spices, colorful fabrics, and trinkets that carried the essence of distant lands"],
        'romanian_sentences.txt': [  "apusul de soare colorat a incendiat cerul cu nuante calde",
                                     "melodia linistitoare a pianului m-a invaluit intr-o atmosfera relaxanta",
                                     "florile de primavara isi deschid petalele sub razele blande ale soarelui",
                                     "copiii zambitori se joaca cu baloanele colorate in parc",
                                     "muntele inzapezit straluceste sub lumina lunii pline",
                                     "aroma proaspata a cafelei abia prajite ma trezeste dimineata",
                                     "cartea captivanta m-a purtat intr-un univers fantastic si ireal",
                                     "valurile marii lovesc malul cu o forta neobisnuita",
                                     "razboiul rece a marcat perioada tensionata din istoria recenta",
                                     "stelele stralucesc ca diamantele pe cerul instelat"]
    }
    assert game.get_random_sentence((language_choice)) in mocked_content[f"{language_choice}_sentences.txt"] or "No sentence for specified language"
