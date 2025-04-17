import random
import os

print("Welcome to legends of monopoly")

# Define game constants
INITIAL_BALANCE = 1500
START_POSITION = 1

bank = {"bal": 1000000}
players = {
    1: {"name": "Soham   ", "bal": INITIAL_BALANCE, "pos": START_POSITION, "property": [], "ST.": 0, "WR.": 0},
    2: {"name": "Shubham ", "bal": INITIAL_BALANCE, "pos": START_POSITION, "property": [], "ST.": 0, "WR.": 0},
    3: {"name": "Medhansh", "bal": INITIAL_BALANCE, "pos": START_POSITION, "property": [], "ST.": 0, "WR.": 0},
    4: {"name": "Soham J.", "bal": INITIAL_BALANCE, "pos": START_POSITION, "property": [], "ST.": 0, "WR.": 0},
}

# Define board properties
board = {
         1:  ["Shrine of Ressurection(GO)", "0", False],
         2:  ["Temple of Time", "60", True],
         3:  ["Boko Chest", "0", False],
         4:  ["Forest of Spirits", "60", True],
         5:  ["Got insulted by aunty.", "200", False],
         6:  ["Divine Beast VAH MEDOH", "200", True],
         7:  ["Lurelin Village", "100", True],
         8:  ["Chance 1", "0", False],
         9:  ["Rito Village", "100", True],
         10: ["Zora's Domain", "120", True],
         11: ["Lockup(Jail)", "0", False],
         12: ["Goron City", "140", True],
         13: ["HATENO TECH LAB", "150", True],
         14: ["Gerudo Town", "140", True],
         15: ["Korok Forest", "160", True],
         16: ["Divine Beast VAH RUTA", "200", True],
         17: ["Eventide Island", "180", True],
         18: ["Metal Chest", "0", False],
         19: ["Yiga Clan Hideout", "180", True],
         20: ["Satori Mountain", "200", True],
         21: ["Stable(Rest)", "0", False],
         22: ["Spring of Wisdom", "220", True],
         23: ["Chance 2", "0", False],
         24: ["Spring of Power", "220", True],
         25: ["Spring of Courage", "240", True],
         26: ["Divine Beast VAH RUDANIA", "200", True],
         27: ["South Lomei Labyrinth", "260", True],
         28: ["North Lomei Labyrinth", "260", True],
         29: ["AKKALA TECH LAB", "150", True],
         30: ["Lomei Labyrinth", "280", True],
         31: ["Go To LOCKUP", "0", False],
         32: ["Kakariko Village", "300", True],
         33: ["Hateno Village", "300", True],
         34: ["Sheikah Chest", "0", False],
         35: ["Tarrey Town", "320", True],
         36: ["Divine Beast VAH NABORIS", "200", True],
         37: ["Chance 3", "0", False],
         38: ["Forgotten Temple", "350", True],
         39: ["stepped on branch(fall damage).", "100", False],
         0:  ["Hyrule Castle", "400", True]
}

chest = [
    ['Bank error in your favor. Collect $200', 200],
    ['Doctor’s fee. Pay $50', -50],
    ['From sale of stock you get $50', 50],
    ['Holiday fund matures. Receive $100', 100],
    ['Pay hospital fees of $100', -100]
]
chance = [
    ['Bank pays you dividend of $50', 50],
    ['You have won second prize in a beauty contest. Collect $10', 10],
    ['Speeding fine $15', -15],
    ['Your building loan matures. Collect $150', 150],
    ['You lose $100', -100]
]
properties = {
              2:  {"rent": 2, "rent_h": 10, "rent_2h": 30, "rent_3h": 90,  "rent_4h": 160, "rent_5ht":	250},
              4:  {"rent": 4, "rent_h": 20, "rent_2h": 60, "rent_3h": 180, "rent_4h": 320, "rent_5ht": 450},
              7:  {"rent": 6, "rent_h": 30, "rent_2h": 90, "rent_3h": 270, "rent_4h": 400, "rent_5ht": 550},
              9:  {"rent": 6, "rent_h": 30, "rent_2h": 90, "rent_3h": 270, "rent_4h": 400, "rent_5ht": 550},
              10: {"rent": 8, "rent_h": 40, "rent_2h": 100,"rent_3h": 300, "rent_4h": 450, "rent_ht":	600},
              12: {"rent": 10,"rent_h": 50, "rent_2h": 150,"rent_3h": 450, "rent_4h": 625, "rent_ht": 750},
              14: {"rent": 10,"rent_h": 50, "rent_2h": 150,"rent_3h": 450, "rent_4h": 625, "rent_ht": 750},
              15: {"rent": 12,"rent_h": 60, "rent_2h": 180,"rent_3h": 500, "rent_4h": 700, "rent_ht": 900},
              17: {"rent": 14,"rent_h": 70, "rent_2h": 200,"rent_3h": 550, "rent_4h": 750, "rent_ht": 950},
              19: {"rent": 14,"rent_h": 70, "rent_2h": 200,"rent_3h": 550, "rent_4h": 750, "rent_ht": 950},
              20: {"rent": 16,"rent_h": 80, "rent_2h": 220,"rent_3h": 600, "rent_4h": 800, "rent_ht": 1000},
              22: {"rent": 18,"rent_h": 90, "rent_2h": 250,"rent_3h": 700, "rent_4h": 875, "rent_ht": 1050},
              24: {"rent": 18,"rent_h": 90, "rent_2h": 250,"rent_3h": 700, "rent_4h": 875, "rent_ht": 1050},
              25: {"rent": 20,"rent_h": 100,"rent_2h": 300,"rent_3h": 750, "rent_4h": 925, "rent_ht": 1100},
              27: {"rent": 22,"rent_h": 110,"rent_2h": 330,"rent_3h": 800, "rent_4h": 975, "rent_ht":	1150},
              28: {"rent": 22,"rent_h": 110,"rent_2h": 330,"rent_3h": 800, "rent_4h": 975, "rent_ht":	1150},
              30: {"rent": 24,"rent_h": 120,"rent_2h": 360,"rent_3h": 850, "rent_4h": 1025,"rent_ht": 1200},
              32: {"rent": 26,"rent_h": 130,"rent_2h": 390,"rent_3h": 900, "rent_4h": 1100,"rent_ht": 1275},
              33: {"rent": 26,"rent_h": 130,"rent_2h": 390,"rent_3h": 900, "rent_4h": 1100,"rent_ht": 1275},
              35: {"rent": 28,"rent_h": 150,"rent_2h": 450,"rent_3h": 1000,"rent_4h":	1200,"rent_ht":	1400},
              38: {"rent": 35,"rent_h": 175,"rent_2h": 500,"rent_3h": 1100,"rent_4h":	1300,"rent_ht":	1500},
              0:  {"rent": 50,"rent_h": 200,"rent_2h": 600,"rent_3h": 1400,"rent_4h":	1700,"rent_ht":	2000},

              6:  {"rent": 25,"rent_2": 50,"rent_3": 100,"rent_4": 200},
              16: {"rent": 25,"rent_h": 50,"rent_3": 100,"rent_4": 200},
              26: {"rent": 25,"rent_h": 50,"rent_3": 100,"rent_4": 200},
              36: {"rent": 25,"rent_h": 50,"rent_3": 100,"rent_4": 200},

              13: {"rent": 4,"rent_2": 10},
              29: {"rent": 4,"rent_h": 10},
}



# Function to display player info
def display_info(player):
    print("Name:", player["name"], "| Balance:", player["bal"], "| Place:", player["pos"], "| Properties:", player["property"])
def transfer(player_from, player_to, amount):
    player_from["bal"] -= amount
    player_to["bal"] += amount
def buy_property(player, property):
    player["property"].append(property[0])
    property[2] = False
    transfer(player, bank, int(property[1]))
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
            command = 'cls'
    os.system(command)
def choose(player, current_pos):
    print("1. Buy the place")
    print("2. Display player status")
    print("3. Do nothing")
    choice = int(input("Enter the option number you want to do: "))
    if choice == 1:
        buy_property(player, board[current_pos])
        if current_pos in [6, 16, 26, 36]:
            player["St."] += 1
        elif current_pos in [13, 29]:
            player["WR."] += 1
    elif choice == 2:
        display_info(player)
        choose(player, current_pos)

def play_turn(player):
    clearConsole()
    dice_val = random.randint(1, 6) + random.randint(1, 6)
    before_pos = player["pos"]
    player["pos"] = current_pos = before_pos + dice_val
    # Check for passing GO
    if before_pos < 40 and current_pos >= 40:
        player["bal"] += 200
        current_pos -= 40

    print(f"{player['name']}, you rolled a {dice_val} and landed on {board[current_pos][0]}")

    if current_pos == 11:
        print("You landed at Jail, you can't do anything.")
        return

    if current_pos in [8, 23, 37]:
        chancething = random.choice(chance)
        player["bal"] += chancething[1]
        print(chancething[0])

    if current_pos in [3, 18, 34]:
        chestthing = random.choice(chest)
        player["bal"] += chestthing[1]
        print(chestthing[0])

    if current_pos in [5, 39]:
        if current_pos == 5:
            print("You got insulted by auntie, pay 200.")
            player["bal"] -= 200
        else:
            print("You fell 2cm(fall damage). Pay 100")
            player["bal"] -= 100

    if board[current_pos][2]:
        choose(player,current_pos)
    else:
        for p in players:
            player = players[p]
            if board[current_pos][0] in player["property"]:
                property_owner = player["name"]
                rent_amount = properties[current_pos]["rent"]
                if current_pos in [13, 29]:
                    if player["WR."] == 1:
                        rent_amount = 4*dice_val
                    elif player["WR."] == 2:
                        rent_amount = 10*dice_val
                if current_pos in [6, 16, 26, 36]:
                    rent_amount = 25*player["ST."]
                if player != player:
                    print("")
                    print("This property is owned by", property_owner)
                    print("You have to pay rent of $", rent_amount, "to", property_owner)
                    transfer(player, player, rent_amount)
                    display_info(player)
                else:
                    print("This property belongs to you.")
    display_info(player)
    input("Press enter to pass the turn. ")

# Main game loop
while True:
    for i in range(1, len(players) + 1):
        clearConsole()
        player = players[i]
        print(f"{player['name']}, it is your turn.")
        input("Press enter to roll the dice. ")
        play_turn(player)
