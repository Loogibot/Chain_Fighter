# Chain Fighter - by Loogibot

# makes a new move with properties, sets move advantages, name and name

class moveBuild:

    def __init__(self, moveName, moveDam, moveAdv, moveAdv2):
        self.move = moveName
        self.damage = moveDam
        self.advantage = (moveAdv, moveAdv2)

Kick = moveBuild('Kick', 25, 'Punch', 'Shield')
Punch = moveBuild('Punch', 15, 'Grab', 'Dodge')
Grab = moveBuild('Grab', 5, 'Kick', 'Shield')
Dodge = moveBuild('Dodge', 0, 'Kick', 'Grab')
Shield = moveBuild('Shield', 5, 'Punch', 'Dodge')

move_entry = input('Enter a move: ')

