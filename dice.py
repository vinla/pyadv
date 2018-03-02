import random

def Roll():
    firstDice = random.randint(1, 6)
    secondDice = random.randint(1, 6)
    return (firstDice, secondDice)