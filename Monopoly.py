import random
import os
from typing import List, Dict, Union

players: Dict[int, Union[Dict[str, Union[str, int, List[str]]], Dict[str, int]]] = {
    1: {"name": "", "bal": 1500, "pos": 1, "property": []}, #player1: Dict[str, Union[str, int, List[str]]] = {"name": "", "bal": 1500, "pos": 1, "property": []}
    2: {"name": "", "bal": 1500, "pos": 1, "property": []}, #player2: Dict[str, Union[str, int, List[str]]] = {"name": "", "bal": 1500, "pos": 1, "property": []}
    3: {"name": "", "bal": 1500, "pos": 1, "property": []}, #player3: Dict[str, Union[str, int, List[str]]] = {"name": "", "bal": 1500, "pos": 1, "property": []}
    4: {"name": "", "bal": 1500, "pos": 1, "property": []}, #player4: Dict[str, Union[str, int, List[str]]] = {"name": "", "bal": 1500, "pos": 1, "property": []}
    5: {"bal": 10000}                                       #bank: Dict[str, int] = {"bal": 10000}
}

board: Dict[int, List[Union[str, bool]]] = {
    1: ["Shrine of Ressurection(GO)", "0", False],
    2: ["Temple of Time", "60", True],
    3: ["Boko Chest", "0", False],
    4: ["Forest of Spirits", "60", True],
    5: ["Got insulted by aunty.", "200", False],
    6: ["Divine Beast VAH MEDOH", "200", True],
    7: ["Lurelin Village", "100", True],
    8: ["Chance 1", "0", False],
    9: ["Rito Village", "100", True],
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
    0: ["Hyrule Castle", "400", True]
}

chest: Dict[int, List[Union[str, int]]] = {
    1: ["Bank error in your favor. Collect $200", 200],
    2: ["Doctorâ€™s fee. Pay $50", -50],
    3: ["From sale of stock you get $50", 50],
    4: ["Holiday fund matures. Receive $100", 100],
    5: ["Pay hospital fees of $100", -100]
}

chance: Dict[int, List[Union[str, int]]] = {
    1: ["Bank pays you dividend of $50", 50],
    2: ["You have won second prize in a beauty contest. Collect $10", 10],
    3: ["Speeding fine $15", -15],
    4: ["Your building loan matures. Collect $150", 150],
    5: ["You lose $100", -100]
}

properties: Dict[int, Dict[str, Union[int, List[int]]]] = {
    2: {"rent": 2, "rent_h": 1},
    4: {"rent": 4, "rent_h": 20},
    6: {"rent": 25, "rent_2": 50, "rent_3": 100, "rent_4": 200},
    7: {"rent": 6, "rent_h": 30},
    9: {"rent": 6, "rent_h": 30},
    10: {"rent": 8, "rent_h": 40},
    12: {"rent": 10, "rent_h": 50},
    13: {"rent": 4, "rent_2": 10},
    14: {"rent": 10, "rent_h": 50},
    15: {"rent": 12, "rent_h": 60},
    16: {"rent": 25, "rent_2": 50, "rent_3": 100, "rent_4": 200},
    17: {"rent": 14, "rent_h": 70},
    19: {"rent": 14, "rent_h": 70},
    20: {"rent": 16, "rent_h": 80},
    22: {"rent": 18, "rent_h": 90},
    24: {"rent": 18, "rent_h": 90}
}

print("Welcome to legends of monopoly" + "\n")

for l in range(1, 5): players[l]["name"] = input(f"What is the name of player {l} ? ")

def clearConsole() -> None:
    os.system('cls' if os.name=='nt' else 'clear')

def rollDice() -> int:
    return random.randint(1,6)+random.randint(1,6)

def display(m: int) -> None:
    print("\n" + "Name:", players[m]["name"], "| Balance:", players[m]["bal"], "| Place:", board[players[m]["pos"]][0], "| Properties:", players[m]["property"], "\n")

def transfer(player_from: int, player_to: int, amt: int) -> None:
    players[player_from]["bal"] -= amt
    players[player_to]["bal"] += amt

def checkIfPlayersAreBankrupt() -> None:
    cont: List[bool] = []
    [cont.extend(True if players[x]["bal"] > 0 else False for x in range(1, 5))]
    if cont.count(False) >= 3: exit()

def game(pos: int, pl: int) -> None:
    if board[pos][2] == True:
        print('''\n1. Buy the place\n2. Display player status\n3. Do nothing''')
        print("\nEnter the option number you want to do. ", end="" + "\n")
        choice: int = int(input())
        while (choice != 1 and choice != 2 and choice != 3 and choice != 4):
            choice = input("invalid input, enter again: ")
        if choice == 1:
            players[pl]["property"].append(board[pos][0])
            print("Congrats, you bought", board[pos][0])
            board[pos][2] = False
            transfer(pl, 5, int(board[pos][1]))
        elif choice == 2:
            display(pl)
            game(pos, pl)
        elif choice == 3:
            pass
        else:
            display(pl)
            mortgage_property = input("Which property do you want to mortgage?")
            if players[pl]["property"] == mortgage_property: print("You mortgaged the property")
    elif pos == 5:
        transfer(pl, 5, 200)
        print("You paid 200 to do a therapy lol.")
    elif pos == 39:
        transfer(pl, 5, 100)
        print("You paid 100 to visit the doctor, such a failure.")
    else:
        for s in range(1, 5):
            if board[pos][0] in players[s]["property"]:
                print("This has been bought already, you have to pay.")
                transfer(pl, s, properties[current_pos]["rent"])
    display(pl)

while True:
    checkIfPlayersAreBankrupt()
    for i in range(1, len(players)):
        clearConsole()
        before_pos = players[i]["pos"]
        print(players[i]["name"], ", it is your turn.")
        start_var = input("Press enter to roll the dice. ")
        while start_var != "":
            start_var = input("You have to press enter to roll the dice. ")
        else:
            dice_val = rollDice()
            current_pos = before_pos + dice_val
            players[i]["pos"] = current_pos
            if before_pos < 40 and current_pos >= 40:
                players[i]["bal"] += 200
            current_pos = current_pos % 40
            print("\nYou rolled a", dice_val)
            print("and you landed on >>", board[current_pos][0])
            if players[i]["pos"] == 11:
                print("\nYou landed at Jail so you can not do anything")
                con = input("Type enter to pass the turn. ")
                while con != "":
                    con = input("You have to type enter. ")
                else:
                    continue
            if players[i]["pos"] == 8 or players[i]["pos"] == 23 or players[i]["pos"] == 37:
                chancething = random.choice(list(chance.values()))
                players[i]["bal"] += chancething[1]
                print("\n" + chancething[0])
                display(i)
                con = input("Type enter to pass the turn. ")
                while con != "":
                    con = input("You have to type enter. ")
                else:
                    continue
            if players[i]["pos"] == 3 or players[i]["pos"] == 18 or players[i]["pos"] == 34:
                chestthing = random.choice(list(chest.values()))
                players[i]["bal"] += chestthing[1]
                print("\n" + chestthing[0])
                display(i)
                con = input("Type enter to pass the turn. ")
                while con != "":
                    con = input("You have to type enter. ")
                else:
                    continue
            else:
                game(current_pos, i)
            con = input("Type enter to pass the turn. ")
            while con != "":
                con = input("You have to type enter. ")
            else:
                continue
