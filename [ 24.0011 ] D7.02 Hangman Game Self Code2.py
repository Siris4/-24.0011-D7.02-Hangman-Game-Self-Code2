import random

# Step 1
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
print(f"Btw, the secret word is: {chosen_word} ")

# Ask the user to guess a letter and convert it to lowercase (input already in the while loop below)


# Deconstruct the chosen word into a list of characters.
deconstructed_chosen_word = list(chosen_word)

# Initialize the board with underscores.
l = len(chosen_word)
#you can use display instead of board if you want
board = ["_"] * l
#print(f"The current board: {board}")

# Display the current state of the board.
#print(' '.join(board))

# Step 2

counter = 0

while counter < l:
    guess = input("Please make a guess of a letter you think may be inside the word! : \n").lower()
    counter += 1

# Update the board based on the new guess.
    for position_on_board in range(l):
        # Display the updated state of the board.

        if guess == deconstructed_chosen_word[position_on_board]:
            board[position_on_board] = guess
    print(' '.join(board))
    if guess in deconstructed_chosen_word:
        print(f"Nice work! You guessed a correct letter! You chose '{guess}'")
    else:
         print(f"Sorry, but '{guess}' was not in this index place. +1 Penalty!\n")

else:
    print("Guess that's all of it. You did not guess in time. Sorry, you lose! Try again!")

# Display the updated state of the board.
print(' '.join(board))

#User_Wins
if "_" not in board:
    print("You won!!!!!")