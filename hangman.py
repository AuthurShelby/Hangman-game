import random

word = ("JavaScript","Java","Python","SQL","C","Php","HTML","Django","Ruby")
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
    hide = ['_']*len(word)
    return hide


def main():
    print("H A N G M A N")
    WordChoosen = random.choice(word).lower()
    Target = Hidden(WordChoosen)
    wrongs = 0
    max_attempt = 6
   
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
        else:
            wrongs+=1

        if "_" not in Target:
            print(" ".join(Target))
            print("You win!")
            break
        
        if wrongs == max_attempt:
                print("\n------")
                DisplayHangman(wrongs)
                print("------")
                print("You lose!")
                print(f"The word was {WordChoosen}")
                break

    print("________________________________")
    print("Thank you for playing Hangman!")
    print("________________________________")
if __name__ == "__main__":
    main()