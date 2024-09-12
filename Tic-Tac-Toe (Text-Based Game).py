# Tic-Tac-Toe (Text-Based Game)

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def check(player, board):
    combinations = [
        ["top-L", "top-M", "top-R"],
        ['mid-L', 'mid-M', 'mid-R'],
        ['low-L', 'low-M', 'low-R'],
        ['top-L', 'mid-L', 'low-L'],
        ['top-M', 'mid-M', 'low-M'],
        ['top-R', 'mid-R', 'low-R'],
        ['top-L', 'mid-M', 'low-R'],
        ['top-R', 'mid-M', 'low-L']
    ]
    for combo in combinations:
        if all(board[rslt] == player for rslt in combo):
            return True
    return False

def main():
    board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    print("Let's Start the Game Guyz")
    print("============================")
    player_1 = input("Player 1 name: ")
    player_2 = input("Player 2 name: ")
    turn = input(f"Who Goes First, {player_1} or {player_2}: ")
    while turn not in [player_1, player_2]:
        turn = input(f"Enter {player_1} or {player_2}: ")

    symbol = {player_1: 'X', player_2: 'O'}
    print("Symbols for both Players: ", symbol)
    current_player = turn

    while True:
        printBoard(board)

        available_moves = [key for key, value in board.items() if value == ' ']
        print(f"Available moves: {', '.join(available_moves)}")

        print(f"Turn for {current_player}: ", end="")
        move = input()

        if move not in available_moves:
            print("Invalid Move.")
            continue

        board[move] = symbol[current_player]

        if check(symbol[current_player], board):
            print("=============================")
            print(f"Congratulations {current_player} Wins!")
            print("=============================")
            break
        if all(value != " " for value in board.values()):
            printBoard(board)
            print("The game is a draw!")
            break

        current_player = player_1 if current_player == player_2 else player_2
    printBoard(board)

main()
