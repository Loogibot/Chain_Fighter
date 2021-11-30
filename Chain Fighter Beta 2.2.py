# Chain Fighter - by Loogibot

# makes a new move with properties, sets move advantages, name and name

class moveBuild:

    def __init__(self, moveName, moveDam, moveAdv, moveAdv2):
        self.moveName = moveName
        self.moveDam = moveDam
        self.moveAdv = moveAdv
        self.moveAdv2 = moveAdv2

    def validMove(self, ):
        return self.moveName

Kick = moveBuild('Kick', 25, 'Punch', 'Shield')
Punch = moveBuild('Punch', 15, 'Grab', 'Dodge')
Grab = moveBuild('Grab', 5, 'Kick', 'Shield')
Dodge = moveBuild('Dodge', 0, 'Kick', 'Grab')
Shield = moveBuild('Shield', 5, 'Punch', 'Dodge')




def player_Move():
    move_select = input("Enter a move: ").lower()
    valid_input = moveBuild(moveName=move_select)
    if move_select not in valid_input:
        return False
    else:
        print(valid_input)

player_Move()