from tkinter import *

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


# moves and their properties; move name, damage, first and second advantage and button image

moves = [

    ('KICK', 25, 'PUNCH', 'SHIELD', kick_btnImage, player_moveKick, opponent_moveKick),
    ('PUNCH', 15, 'GRAB', 'DODGE', punch_btnImage, player_movePunch, opponent_movePunch),
    ('GRAB', 5, 'KICK', 'SHIELD', grab_btnImage, player_moveGrab, opponent_moveGrab),
    ('DODGE', 0, 'KICK', 'GRAB', dodge_btnImage, player_moveDodge, opponent_moveDodge),
    ('SHIELD', 5, 'PUNCH', 'DODGE', shield_btnImage, player_moveShield, opponent_moveShield),

]
