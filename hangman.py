#------------------------------------------------------------------------------
#Project Name:     hangman
#Description:      A simple version of hangman coded in Python
#------------------------------------------------------------------------------
#Author:           laazyLlama
#Date Created:     26/04/2021
#Last Changes:     26/04/2021
#------------------------------------------------------------------------------

word = "Test"
known = "...."

while known.find('.') != -1:
    print(known)
    guess = input("Have a guess: ").lower()
    for i in word:
        if i == guess or i == guess.upper():
            known = known[:(word.find(i))] + word[word.find(i)] + known[(word.find(i) + 1):]

print(known + " was the hidden word!")
