print("--------------------")
print("Welcome to the game!")


def create_tic_tac_toe(values):
    print("\n")
    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")

    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")

    print("\t     |     |     ")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |     ")
    print("\n")


def check_win(player_position, current_player):

    soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    for x in soln:
        if all(y in player_position[current_player] for y in x):
            return True
    return False


def check_draw(player_position):
    if len(player_position['X']) + len(player_position['O']) == 9:
        return True
    return False


def single_game(current_player):
    values = [' ' for x in range(9)]
    player_position = {'X':[], 'O':[]}

    while True:
        create_tic_tac_toe(values)

        try:
            print("Player ", current_player, " turn. Which box: ", end="")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try again")
            continue

        if values[move-1] != ' ':
            print("Place already filled. Try again!")
            continue

        values[move-1] = current_player

        player_position[current_player].append(move)

        if check_win(player_position, current_player):
            create_tic_tac_toe(values)
            print("Player ", current_player, " has won the game!")
            print("\n")
            return current_player

        if check_draw(player_position):
            create_tic_tac_toe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


while True:
    single_game('X')

    play_again = input("Would you like to play again? (Y for yes or N for No): ").lower()
    if play_again != "y":
        break
print("Bye, see you next time.")
