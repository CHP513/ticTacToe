

#Dictionary for Spaces in Tic Tac Toe
tic_tac_toe = {
    "ul":"  UL   ",
    "um":"  UM   ",
    "ur":"  UR   ",
    "ml":"  ML   ",
    "mm":"  MM   ",
    "mr":"  MR   ",
    "ll":"  LL   ",
    "lm":"  LM   ",
    "lr":"  LR   ",
}

# Create copy for replays
gametic_tac_toe = tic_tac_toe

# Keep track if the game ended
gameOver = False

# Keep track of turn order (Player1/Player2)
turn = "Player1"

# Keep track of turn number.  If 9, game over
turnNumber = 0

# Show rules and how to play
print(f"Welcome to Tic Tac Toe")
print(f"Rules: This is a two player game, Player 1 is X and Player 2 is O.")
print(f"Player 1 goes first, type in the letters below to place your symbol, then it is the other player's turn")
print(f"  UL  |  UM  |  UR  ")
print(f"____________________")
print(f"  ML  |  MM  |  MR  ")
print(f"____________________")
print(f"  LL  |  LM  |  LR  ")
print(f"If one of the players gets three symbols in a row, they win.  If all spaces are filled, the game is a tie.")

print(f"Let the game begin")

while not gameOver:
    #Keep track of player and their symbols
    if turn == "Player1":
        symbol = "  X  "
    else:
        symbol = "  O  "

    place = input("Where to put symbol: ")
    if place not in gametic_tac_toe:
        print("Not a valid space, try again")
        turnNumber = turnNumber - 1
    else:
        gametic_tac_toe[place] = symbol

    print(f"{gametic_tac_toe['ul']}|{gametic_tac_toe['um']}|{gametic_tac_toe['ur']}")
    print(f"{gametic_tac_toe['ml']}|{gametic_tac_toe['mm']}|{gametic_tac_toe['mr']}")
    print(f"{gametic_tac_toe['ll']}|{gametic_tac_toe['lm']}|{gametic_tac_toe['lr']}")
    turnNumber = turnNumber + 1

    if turnNumber == 9:
        gameOver = True

 # Check if a player won
    if (gametic_tac_toe['ul'] == gametic_tac_toe['um'] == gametic_tac_toe['ur'] or
            gametic_tac_toe['ml'] == gametic_tac_toe['mm'] == gametic_tac_toe['mr'] or
            gametic_tac_toe['ll'] == gametic_tac_toe['lm'] == gametic_tac_toe['lr'] or
            gametic_tac_toe['ul'] == gametic_tac_toe['ml'] == gametic_tac_toe['ll'] or
            gametic_tac_toe['um'] == gametic_tac_toe['mm'] == gametic_tac_toe['lm'] or
            gametic_tac_toe['ur'] == gametic_tac_toe['mr'] == gametic_tac_toe['lr'] or
            gametic_tac_toe['ul'] == gametic_tac_toe['mm'] == gametic_tac_toe['lr'] or
            gametic_tac_toe['ll'] == gametic_tac_toe['mm'] == gametic_tac_toe['ur']):

        gameOver = True

    if turn == "Player1":
        turn = "Player2"
    else:
        turn = "Player1"

    if gameOver == True:
        playAgain = input("Game Over, Play Again? Y/N: ")

        if playAgain == 'Y':
            gametic_tac_toe = tic_tac_toe
            gameOver = False

