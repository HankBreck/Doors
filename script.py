import random
import pandas as pd

savedData = pd.read_csv("save.csv")

def run():
    global totalTreasure
    adjectives = {"heavy":0.13,"wooden":0.06,"metal":0.09,"chained":0.23,"eerie":0.18,"white":0.01,"black":0.09,"striped":0.05,"shiny":0.14,"dull":0.19,"bloody":0.3,"worn down":0.16,"charred":0.21,"broken":0.25,}
    alive = True

    # Let the games begin
    print("Welcome to doors. The place where you make choices and fucking die.")
    input("Press enter to continue...")
    name = input("What is your name?\n").lower()


    # Cute little thing for Miss Lele
    if (name == "elle"):
        name = "miss ellemer"

    for i in range(len(savedData.index)):
        if name == savedData.iloc[i]['name']:
            totalTreasure = savedData.iloc[i]['total']
            idx = i
        else:
            print('Name is not %s' % (savedData.iloc[i]['name']))


    print("\nHello, %s" % name.capitalize())

    print("\nThe rules of this game are simple. Three doors on each level appear. A short description of each door will appear. You must select one of the doors to pass through. If the Scuvasz is on the other side of the door, you die.")
    print("\nThere is also a treasure system. Treasure currently has no use, but eventually you will be able to buy things. The scarier the door, the more treasure will be behind the door!")

    score = 0

    # Game logic
    while (alive == True):
        # Publishing the score each level
        print("\nYour score is: %d\nYour treasure count is: %d" % (score, totalTreasure))

        # Increasing score after each level
        score += 1

        # Resetting the description and threat levels each level
        door_adj = ["blank","blank","blank"]
        door_threat = [0,0,0]
        treasure = [0,0,0]

        # Randomly selecting the adjectives to use for each door & defining the threat based off of this
        for i in range(3):
            door_adj[i] = [random.choice(list(adjectives)),random.choice(list(adjectives))]
            door_threat[i] = adjectives[door_adj[i][0]] + adjectives[door_adj[i][1]]
            treasure[i] = ((adjectives[door_adj[i][0]] + adjectives[door_adj[i][1]]) * 35) * random.random()

        # Printing the door description to the user
        print("Door 1 is %s and %s" % (door_adj[0][0],door_adj[0][1]))
        print("Door 2 is %s and %s" % (door_adj[1][0],door_adj[1][1]))
        print("Door 3 is %s and %s" % (door_adj[2][0],door_adj[2][1]))

        # User selects the door they wish to pass through
        choice = int(input("Which door are you going through? [1,2,3]\n"))

        # Using threat to determine whether the user lives or dies
        alive = random.random() > door_threat[choice-1]

        # If the Scuvasz is behind the door, end the game
        if (alive == False):
            print("\nYou were mauled to death by the floofiest Scuvasz! Good boy!")
        else:
            totalTreasure += treasure[choice-1]

        savedData.iloc[idx, savedData.columns.get_loc('total')] = totalTreasure
    savedData.to_csv(r'save.csv')
