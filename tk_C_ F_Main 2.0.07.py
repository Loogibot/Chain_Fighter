from tkinter import *
from random import randint

root = Tk()

root.title('CHAIN FIGHTER 2.2:2.0.07 BETA')
root.geometry('575x475')

# Game image resources

start_btnImage = PhotoImage(file='Chain Fighter UI Set/Game_Start.png')
Chain_Fighter_Title = PhotoImage(file='Chain Fighter UI Set/Chain_Fighter_Title.png')

player_moveKick = PhotoImage(file='Chain Fighter UI Set/player_kick.png')
player_movePunch = PhotoImage(file='Chain Fighter UI Set/player_punch.png')
player_moveGrab = PhotoImage(file='Chain Fighter UI Set/player_grab.png')
player_moveDodge = PhotoImage(file='Chain Fighter UI Set/player_dodge.png')
player_moveShield = PhotoImage(file='Chain Fighter UI Set/player_shield.png')

opponent_moveKick = PhotoImage(file='Chain Fighter UI Set/opponent_kick.png')
opponent_movePunch = PhotoImage(file='Chain Fighter UI Set/opponent_punch.png')
opponent_moveGrab = PhotoImage(file='Chain Fighter UI Set/opponent_grab.png')
opponent_moveDodge = PhotoImage(file='Chain Fighter UI Set/opponent_dodge.png')
opponent_moveShield = PhotoImage(file='Chain Fighter UI Set/opponent_shield.png')

kick_btnImage = PhotoImage(file='Chain Fighter UI Set/Player_Public_Option_Kick.png')
shield_btnImage = PhotoImage(file='Chain Fighter UI Set/Player_Public_Option_Shield.png')
dodge_btnImage = PhotoImage(file='Chain Fighter UI Set/Player_Public_Option_Dodge.png')
grab_btnImage = PhotoImage(file='Chain Fighter UI Set/Player_Public_Option_Grab.png')
punch_btnImage = PhotoImage(file='Chain Fighter UI Set/Player_Public_Option_Punch.png')

bG = PhotoImage(file='Chain Fighter UI Set/Main_UI_Field.png')

# Builds the canvas on which everything is 'drawn'

canvas1 = Canvas(root, width=575, height=475)
canvas1.pack(fill='both', expand=True)

# moves and their properties; move name, damage, first and second advantage and button image

moves = [

    ('KICK', '25', 'PUNCH', 'SHIELD', kick_btnImage, player_moveKick, opponent_moveKick),
    ('PUNCH', '15', 'GRAB', 'DODGE', punch_btnImage, player_movePunch, opponent_movePunch),
    ('GRAB', '5', 'KICK', 'SHIELD', grab_btnImage, player_moveGrab, opponent_moveGrab),
    ('DODGE', '0', 'KICK', 'GRAB', dodge_btnImage, player_moveDodge, opponent_moveDodge),
    ('SHIELD', '5', 'PUNCH', 'DODGE', shield_btnImage, player_moveShield, opponent_moveShield),

]


def gameTurn():
    # randomizes the options for the players
    global move_select, move_select1, opponent_choice, btn_Image, btn_Image1, opponent_move, game_turn

    opponent_choice = moves[randint(0, 4)]
    move_select = moves[randint(0, 4)]
    move_select1 = moves[randint(0, 4)]

    btn_Image = move_select[4]
    btn_Image1 = move_select1[4]
    opponent_move = opponent_choice[4]

    # sets HP for both players
    player_HP = 100
    opponent_HP = 90
    player_HPLabel = Label(canvas1, text=player_HP)
    canvas1.create_window(370, 50, window=player_HPLabel)

    opponent_HPLabel = Label(canvas1, text=opponent_HP)
    canvas1.create_window(200, 65, window=opponent_HPLabel)

    game_turn = 0


def gameStart():
    gameTurn()

    global move_button, move_button1
    canvas1.create_image(0, 0, image=bG, anchor='nw')

    move_button = Button(canvas1, image=btn_Image, command=moveChoice)
    move_button_canvas = canvas1.create_window(350, 390, window=move_button)

    move_button1 = Button(canvas1, image=btn_Image1, command=moveChoice1)
    move_button_canvas1 = canvas1.create_window(450, 390, window=move_button1)

    start_game_button.destroy()


def moveChoice():
    global player_move, player_damage, move_advantage

    canvas1.create_image(410, 200, image=move_select[5])

    move_button.config(state=DISABLED)
    move_button1.config(state=DISABLED)

    player_move = move_select[0]
    player_damage = move_select[1]
    move_advantage = move_select[2:4]

    opponentMove()


def moveChoice1():
    global player_move, player_damage, move_advantage

    canvas1.create_image(410, 200, image=move_select1[5])

    move_button.config(state=DISABLED)
    move_button1.config(state=DISABLED)

    player_move = move_select1[0]
    player_damage = move_select1[1]
    move_advantage = move_select1[2:4]

    opponentMove()


def opponentMove():
    global opponent_select, player_damage, opponent_damage, opponent_advantage, game_turn

    canvas1.create_image(160, 265, image=opponent_choice[6])

    game_turn += 1

    opponent_select = opponent_choice[0]
    opponent_damage = opponent_choice[1]
    opponent_advantage = opponent_choice[2:4]

    if opponent_select == player_move:
        print('Moves Cancel!')
        print(opponent_damage, opponent_advantage, opponent_select, player_damage, move_advantage, player_move)

    else:
        print('Different')
        print(opponent_damage, opponent_advantage, opponent_select, player_damage, move_advantage, player_move)
        if player_move in opponent_advantage:
            print('Player takes damage')
        if opponent_select in move_advantage:
            print('Opponent takes damage')


start_game_button = Button(root, image=start_btnImage, command=gameStart)

start_game_canvas = canvas1.create_window(287, 405, window=start_game_button)

cf_Title = canvas1.create_image(287, 237, image=Chain_Fighter_Title)

root.mainloop()