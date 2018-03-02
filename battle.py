import dice
import character
import time

def Resolve(player, enemy):
    enemy = character.Character(enemy["Name"], enemy["Skill"], enemy["HP"])
    while(player.HP > 0 and enemy.HP > 0):
        (dice1, dice2) = dice.Roll();
        playerTotal = player.Skill + dice1 + dice2;
        print("player total = {} + {} + {} = {}".format(dice1, dice2, player.Skill, playerTotal));
        (dice1, dice2) = dice.Roll();
        enemyTotal = enemy.Skill + dice1 + dice2;
        print("{} total = {} + {} + {} = {}".format(enemy.Name, dice1, dice2, enemy.Skill, enemyTotal));
        if(playerTotal >= enemyTotal):
            print('You have hit {} ({} hp)'.format(enemy.Name, enemy.HP - 1))
            enemy.HP -= 1
        else:
            print('{} hits you ({} hp)'.format(enemy.Name, player.HP - 1))
            player.HP -= 1

        time.sleep(2);