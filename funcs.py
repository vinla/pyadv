def IncreaseStat(player, stat, amount):
    currentValue = getattr(player, stat)
    newValue = currentValue + amount
    setattr(player, stat, newValue)
    print("Your {} has increased by {} and is now {}".format(stat, amount, newValue))

def AddItem(player, item):
    print("You have acquired {}".format(item))

def Hurt(player, amount):
    print("You are hit for {}".format(amount))
    player.HP -= amount;