from tkinter import *
from random import randint
from tkinter.ttk import *

root = Tk()

root.title('CHAIN FIGHTER 2.2:2.1.04 BETA')
root.geometry('575x475')

from CFMOVES import *

# Game image resources from CFMOVES. Needs to run AFTER Tk,
# otherwise the images from PhotoImage() will be called too early.
# Also imports 'moves'. See CFMOVES.py for more details

# Builds the canvas on which everything is 'drawn'

canvas1 = Canvas(root, width=575, height=475)
canvas1.pack(fill='both', expand=True)


def gameTurn():
    # randomizes the options for the players
    global move_select, move_select1, opponent_choice, btn_Image, btn_Image1, \
        opponent_move, game_turn, move_button, move_button1, move_button_canvas, move_button_canvas1

    opponent_choice = moves[randint(0, 4)]
    move_select = moves[randint(0, 4)]
    move_select1 = moves[randint(0, 4)]

    btn_Image = move_select[4]
    btn_Image1 = move_select1[4]
    opponent_move = opponent_choice[4]

    # sets move buttons for the player

    move_button = Button(canvas1, image=btn_Image, command=moveChoice)
    move_button_canvas = canvas1.create_window(350, 390, window=move_button)

    move_button1 = Button(canvas1, image=btn_Image1, command=moveChoice1)
    move_button_canvas1 = canvas1.create_window(450, 390, window=move_button1)

    game_turn = True


def gameStart():
    gameTurn()

    global player_HPBar, opponent_HPBar

    player_HPBar = Progressbar(canvas1, orient=HORIZONTAL, length=100, mode='determinate')
    canvas1.create_window(370, 55, window=player_HPBar)

    opponent_HPBar = Progressbar(canvas1, orient=HORIZONTAL, length=100, mode='determinate')
    canvas1.create_window(200, 55, window=opponent_HPBar)

    player_HPBar['value'] = 100
    opponent_HPBar['value'] = 100


    canvas1.create_image(0, 0, image=bG, anchor='nw')

    start_game_button.destroy()


def moveChoice():
    global player_move, player_damage, move_advantage, plyrmoveUI

    plyrmoveUI = canvas1.create_image(410, 200, image=move_select[5])

    player_move = move_select[0]
    player_damage = move_select[1]
    move_advantage = move_select[2:4]

    opponentMove()


def moveChoice1():
    global player_move, player_damage, move_advantage, plyrmoveUI

    plyrmoveUI = canvas1.create_image(410, 201, image=move_select1[5])

    player_move = move_select1[0]
    player_damage = move_select1[1]
    move_advantage = move_select1[2:4]

    opponentMove()


def opponentMove():
    global opponent_select, player_damage, opponent_damage, opponent_advantage, game_turn, moveUI

    moveUI = canvas1.create_image(160, 265, image=opponent_choice[6])
    canvas1.delete(move_button_canvas, move_button_canvas1)

    opponent_select = opponent_choice[0]
    opponent_damage = opponent_choice[1]
    opponent_advantage = opponent_choice[2:4]

    if opponent_select == player_move:
        print('Moves Cancel!')
        print(opponent_select, player_move)
        game_turn = False

    else:
        print('Moves Hit!')
        print(opponent_damage, opponent_select, player_damage, player_move)
        game_turn = False

        if player_move in opponent_advantage:
            print('Player takes {} damage'.format(opponent_damage))
            player_HPBar['value'] = player_HPBar['value'] - opponent_damage

        if opponent_select in move_advantage:
            print('Opponent takes {} damage'.format(player_damage))
            opponent_HPBar['value'] = opponent_HPBar['value'] - player_damage

    if game_turn == False:
        canvas1.after(1200, clearGameUI)
        canvas1.after(500, gameTurn)


def clearGameUI():
    canvas1.delete(moveUI, plyrmoveUI)



start_game_button = Button(root, image=start_btnImage, command=gameStart)

start_game_canvas = canvas1.create_window(287, 405, window=start_game_button)

cf_Title = canvas1.create_image(287, 237, image=Chain_Fighter_Title)

root.mainloop()
