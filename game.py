def getScene(gameData, sceneNumber):
    for scene in gameData:
        if(scene['Id'] == sceneNumber):
            return scene

def printScene(scene):
    print(scene["Description"])

    try:
        options = scene["Options"]
    except:
        options = []

    for index in range(1, len(options) + 1):
        print("{} - {}".format(index, options[index - 1]["Text"]))
    return options;

def askUser(options):
    while(True):
        try:
            value = int(input(">>")) - 1
        except:
            print("That's not a valid option")
            continue

        if(value < 0 or value > len(options) - 1):
            print("That's not a valid option")
            continue

        return options[value]



