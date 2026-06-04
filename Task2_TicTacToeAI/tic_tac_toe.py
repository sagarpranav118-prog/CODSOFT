def print_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


def print_positions():
    print("\nBoard Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print()


def human_move(board):
    while True:

        try:
            position = int(input("Enter your move (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("This position is already occupied.")
                continue

            board[position - 1] = "X"
            break

        except ValueError:
            print("Invalid input. Please enter a number.")


def check_winner(board, player):

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:

        if (board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player):
            return True

    return False


def is_draw(board):
    return " " not in board


def minimax(board, is_maximizing):

    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_draw(board):
        return 0

    if is_maximizing:

        best_score = -1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(board, False)

                board[i] = " "

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = 1000

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(board, True)

                board[i] = " "

                best_score = min(score, best_score)

        return best_score


def ai_move(board):

    best_score = -1000
    best_move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


def main():

    print("=" * 50)
    print("        TIC-TAC-TOE AI")
    print("      Human (X) vs AI (O)")
    print("=" * 50)

    print_positions()

    board = [" " for _ in range(9)]

    while True:

        print_board(board)

        # Human Turn
        human_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 Congratulations! You Win!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a Draw!")
            break

        print("\nAI is thinking...\n")

        # AI Turn
        ai_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("🤖 AI Wins!")
            break

        if is_draw(board):
            print_board(board)
            print("🤝 It's a Draw!")
            break


if __name__ == "__main__":
    main()