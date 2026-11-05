import random

race = {
    "human": {"strength": 2, "dexterity": 1, "constitution": 1},
    "elf": {"dexterity": 2, "intelligence": 1, "charisma": 1},
    "dwarf": {"strength": 1, "constitution": 2, "wisdom": 1},
}

job = {
    "warrior": {"weapons": 1, "armor": 2, "experience proficiency": "10%"},
    "archer": {"bow": 2, "one-handed weapons": 1, "light armor": 1},
    "mage": {"one-handed weapons": 1, "light armor": 1, "spell proficiency": 2},
}

explainations = {
    "explaination": "With your stats you will make decissions and make a roll of the die to see if you have successfully passed the stat check. This is called your 'savings throw', it is a statistical process inwhich you check numbers aginst your stat to see the out come of a decission. (for more info type 'more' or 'q' to quit)",
    "examples": "Your strenght will effect 'savings throws'that check against things like how much weight carry to how much damage you can do in battle. \nYour intellegence will be used with you abilty to cast spells, \nconstitution is how much life you have and how well you take a hit, \ndexetery is how well you move and hit someone, \nwisdom is how well you learn and percieve things around you, \nand charisma is (believe it or not) how good your character is visually percieved in the game by other players.",
}
dialog = {
    "intro": "Have you ever wanted to get away. find an escape into another world, one of fantastic adventure and imagination. One that will sweep the sorrows of tommorow. well look no further and dive into the world of adventure with Dungeons and Dragons. Here your mind can wonder and create in a manner you have never thought. So lets start the adventure with creating a a basic character.",
    "stat_dialog": "Here we will begin to build you stats that will effect everything for your character. If you would like to know how these stats are used in gameplay, type 'explain'.",
}


def stat_explainations():
    user_choice = input(f"{dialog['stat_dialog']}\n")
    while user_choice != "q":
        if user_choice == "explain":
            user_choice = input(f"{explainations['explaination']}\n")
            if user_choice == "more":
                print(f"{explainations['examples']}\n")
                return
        else:
            return


def intro():
    print(dialog["intro"])
    return input("So choose a name worthy adventurer\n")


def job_choice():
    user_choice = input("Would you like to be a...\nWarrior\nArcher\nMage\n").lower()
    picked = {"job": user_choice, "proficiencies": job.get(user_choice)}
    return picked


def race_choice():
    user_choice = input("Would you like to be a...\nHuman\nElf\nDwarf\n").lower()
    picked = {"race": user_choice, "stat_bonuses": race.get(user_choice)}
    return picked


def stat_dice_roll():
    total = 0
    for i in range(4):
        total += random.randint(1, 6)
    return total


class Character:
    def __init__(self, name):
        self.name = name
        self.race = None
        self.job = None
        self.stats = {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "charisma": 0,
            "wisdom": 0,
        }
        self.proficiencies = {}
        self.equipment = {}

    def choose_job(self):
        completed = job_choice()
        self.job = completed["job"]
        self.proficiencies = completed["proficiencies"]

    def choose_race(self):
        completed = race_choice()
        self.race = completed["race"]
        for stat in completed["stat_bonuses"]:
            if stat in self.stats:
                self.stats[stat] += completed["stat_bonuses"][stat]

    def choose_stats(self):
        stat_explainations()


if __name__ == "__main__":
    name = intro()
    new_character = Character(name)
    new_character.choose_race()
    new_character.choose_job()
    new_character.choose_stats()
    # print("**************")
    # print(new_character.__dict__)
    # print("**************")
