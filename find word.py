import random
from uzwords import words
def find_word(word):
    while len(word) != 5:
        word = random.choice(words)
    hidden_word = '-' * len(word)

    print("Let's start the word-finding game! words are in the Russian alphabet.")
    print(hidden_word)
    counter = 0
    guess_later_counter = ""
    while '-' in hidden_word:
        counter += 1
        guess = input(f"{counter} - attempt: letter you entered ({guess_later_counter})  enter a letter: ")
        guess_later_counter += guess
        for i in range(len(word)):
            if word[i] == guess: 
                hidden_word = hidden_word[:i] + guess + hidden_word[i + 1:]
        print(hidden_word)
    print(f"Congratulations, you found the word {hidden_word} in {counter} moves!")
word = random.choice(words)
find_word(word)
