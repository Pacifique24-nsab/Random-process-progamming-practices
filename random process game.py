# import the random process so that our game will be able to run into a library that enable the program to use random processes
import random

flag = True

# ask the user for the name
while flag:
    name = input("What is your name user?\n").strip()

    # ensure the name entered is valid for the norms indicated
    if not name.isalpha():
        print("You have entered an invalid name, please try again")
        continue
    else:
        # greet the user and start our guessing game
        
        print("Hello " + name + ", we are excited to help and assist you in the Pacifique program and we wish you good luck!!")
        break

# create a list of words that the player will guess in
words_list = ['Python', 'HTML', 'CSS', 'Java', 'C++', 'JavaScript', 'SQL', 'Swift', 'PHP', 'Perl', 'Sqala', 'Ruby', 'C#', 'TypeScript', 'Kotlin', 'Go', 'Fortran', 'MathLab', 'Scratch', 'Scheme']

# choose a random word from the list
word = random.choice(words_list)

# ask the user to guess a character between the characters provided
print(name + ", please, take a guess of any character \n")
num_turns = 20 

# loop through the number of turns allowed and check if the guess is correct
while num_turns > 0:
    guess = input("Please take a guess of a character\n")
    if not guess.isalpha() or len(guess) != 1:
        print("You have entered an invalid character, please try again")
        continue
    if guess in word:
        print("Good guess!")
    else:
        num_turns -= 1
        print("Wrong guess!")
        print("You have", num_turns, "more guesses left.")
    if set(word).issubset(set(guess)):
        # player wins if they guess all the letters in the word
        print("Congratulations, you won!")
        break
    elif num_turns == 0:
        # player loses if they run out of guesses between the possible choices provided
        print("Sorry, you lost!")
        print("The word was:", word)
        break
