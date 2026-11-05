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


def intro():
    print(
        "have you ever wanted to get away. find an escape into another world, one of fantastic adventure and imagination. One that will sweep the sorrows of tommorow. well look no further and dive into the world of adventure with Dungeons and Dragons. Here your mind can wonder and create in a manner you have never thought. So lets start the adventure with creating a a basic character."
    )
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
        print("stopping here")


if __name__ == "__main__":
    name = intro()
    new_character = Character(name)
    new_character.choose_race()
    new_character.choose_job()
    print("**************")
    print(new_character.__dict__)
    print("**************")
