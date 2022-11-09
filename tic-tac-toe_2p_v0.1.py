import random

board = [1,2,3,4,5,6,7,8,9]
counter = 9
# display real board

def display(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")

# define single or 2 players mode
def game_mode():
    mode = int(input('How many players will play? 1 or 2. Enter a digit: '))
    return mode

# user input single mode + update the row
def user_input():
    global counter
    valid = False
    while not valid:
        try:
            turn = int(input('Choose your turn '))
        except:
            print()
            print('Wrong turn ')
            continue
        if 1 <= turn <= 9:
            if (str(board[turn-1]) not in 'XO'):
                board[turn-1] = 'X'
                counter -= 1
                valid = True
            else:
                print('Yoy can not choose this cell')
        else:
            print('Enter digit from 1 to 9')

# AI turn immitation + update the row
def ai_turn():
    global counter
    for _ in range(100):
        i = random.randint(0,8)
        if str(board[i]) not in 'XO':
            board[i] = 'O'
            counter -= 1
            break
        else:
            if counter != 0:
                continue
            else:
                break
            break

# 2 players mode + update the row
def two_players(token):
    global counter
    valid = False
    while not valid:
        try:
            turn = int(input(f'Choose your turn {token}: '))
        except:
            print()
            print('Wrong turn ')
            continue
        if 1 <= turn <= 9:
            if (str(board[turn-1]) not in 'XO'):
                board[turn-1] = token
                counter -= 1
                valid = True
            else:
                print('Yoy can not choose this cell')
        else:
            print('Enter digit from 1 to 9')

# winner check
def the_winner_is(board):
    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]

def main(board):
    global counter
    win = False
    mode = game_mode()
    while not win:
        display(board)
        if mode == 1:
            if counter % 2 != 0:
                user_input()
            else:
                ai_turn()
        elif mode == 2:
            if counter % 2 != 0:
                two_players('X')
            else:
                two_players('O')
        if counter < 5:
            temp = the_winner_is(board)
            if temp == 'X':
                print('X wins!')
                win = True
                break
            elif temp == 'O':
                print('O wins!')
                win = True
                break
        if counter == 0:
            print('DRAW')
            break
    display(board)
main(board)