from HangmanWords import words
import random


hangman = {
    0:("     ",
       "     ",
       "     "),
    1:("  O  ",
       "     ",
       "     "),
    2:("  O  ",
       "  |  ",
       "     "),
    3:("  O  ",
       "  | \\",
       "     "),
    4:("  O  ",
       "/ | \\",
       "     "),
    5:("  O  ",
       "/ | \\",
       " /   "),
    6:("  O  ",
       "/ | \\",
       " / \\"),
}
def DisplayHangman(wrongs):
    for i in hangman[wrongs]:
        print(i)

def Hidden(word):
    return ['_']*len(word)


def main():
    print("H A N G M A N")
    WordChoosen = random.choice(words).lower()
    Target = Hidden(WordChoosen)
    wrongs = 0
    max_attempt = 6
    guessed = []

    while True:
        print("\n------")
        DisplayHangman(wrongs)
        print("------")

        print("\n"," ".join(Target))
        guess = input("\nGuess a letter: ").lower()
       
        if len(guess)!=1 or not guess.isalpha():
            print("Invalid!")
            continue

        if guess in WordChoosen:
            for i in range(len(WordChoosen)):
                if guess == WordChoosen[i]:
                    Target[i] = guess
                    guessed.append(guess)
        else:
            wrongs+=1
        
        if guess in guessed:
            print("You already guessed this letter!")
            continue
        
        if "_" not in Target:
            print(" ".join(Target))
            print("You win!")
            break
        
        if wrongs == max_attempt:
                print("\n------")
                DisplayHangman(wrongs)
                print("------")
                print("....................")
                print("\nYou lose!")
                print(f"The word was {WordChoosen.title()}")
                print("....................")
                break

    print("________________________________")
    print("Thank you for playing Hangman!")
    print("________________________________")
if __name__ == "__main__":
    main()
