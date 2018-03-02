import json
import game
import character
import battle
import funcs

data = ''
with open('game.json') as game_file:
    data = game_file.read()

playerName = input('Name your character >')
player = character.Character(playerName, 10, 10)

game_data = json.loads(data)
scene_index = '001'

while(True):
    scene = game.getScene(game_data, scene_index)
    options = game.printScene(scene)
    if(len(options) == 0):
        break
    user_option = game.askUser(options)

    #Check for an enemy
    if("Enemy" in user_option):
        enemy = user_option["Enemy"]
        battle.Resolve(player, enemy)
        if(player.HP > 0):
            scene_index = user_option["GotoOnWin"]
        elif("GotoOnLose" in user_option):
            scene_index = user_option["GotoOnLose"]
        else:
            break;
    else:
        scene_index = user_option["Goto"]

print('Game over')


