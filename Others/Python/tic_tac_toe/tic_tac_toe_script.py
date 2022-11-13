def print_board(board):
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")


def turn(n_turn):
    if n_turn % 2 == 0:
        return "X"
    else:
        return "O"


def check_result(board):
    if board[0][0] == board[1][1] == board[2][2] != ' ' or board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    else:
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return True
            for j in range(len(board[i])):
                if board[0][j] == board[1][j] == board[2][j] != ' ':
                    return True
        return False


def play():
    t = 0
    b = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]
    while t < 9:
        player = turn(t)
        print_board(b)
        print("Player " + player + "'s turn.")
        while True:
            l = input("Choose a line (0, 1, 2) : ")
            if l not in {'0', '1', '2'}:
                print("The selected line does not exist!")
                continue
            while True:
                c = input("Choose a column (0, 1, 2) : ")
                if c in {'0', '1', '2'}:
                    break
                print("The selected column does not exist!")
            if b[int(l)][int(c)] == ' ':
                b[int(l)][int(c)] = player
                break
            elif b[int(l)][int(c)] == "X" or b[int(l)][int(c)] == "O":
                print("This location is already taken!")
                print("Please choose another: ")
        if check_result(b):
            print_board(b)
            print("Game over, player " + player + " wins!")
            break
        t += 1
    if t == 9:
        print_board(b)
        print("Game over, draw.")


if __name__ == '__main__':
    play()
