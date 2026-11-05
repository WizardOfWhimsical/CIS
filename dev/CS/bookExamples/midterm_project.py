def create_roster():
    player = {}
    for i in range(1,6):
        jersey_num = int(input(f"Enter player {i}'s jersey number:\n"))
        rating_num = int(input(f"Enter player {i}'s rating:\n"))
        print()
        while 1 >rating_num or rating_num >= 11:
            rating_num = int(input("please enter a number between 1-10 for rating:"))
        player[i] = {"jersey":jersey_num,"rating":rating_num}
    return player

def add_player(players_dict):
    dict_list = sorted(players_dict.keys())
    jersey_num = int(input("Enter a new players jersey number:"))
    rating_num = int(input("Enter a new players rating: "))
    while 1 >rating_num or rating_num >= 11:
        rating_num = int(input("please enter a number between 1-10 for rating:"))
    players_dict[dict_list[-1]+1] = {"jersey":jersey_num,"rating":rating_num}
    return players_dict

def menu():
    print("MENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit")
    print()
    choice = input("Choose an option:")
    while choice not in ["a","d","u","r","o","q"]:
        print("Please pick one of the options available here\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit")
        print()
        choice = input("Choose an option:")
    return choice

def roster_output(players_dict):

    def sort_jersey(player):
        return players_dict[player]["jersey"]

    sorted_dict = sorted(players_dict,key=sort_jersey)
    print("ROSTER")
    for player in sorted_dict:
        print(f"Jersey number: {players_dict[player]['jersey']}, Rating: {players_dict[player]['rating']}")
    print()

def delete_player(players_dict):
    player_jersey_delete = int(input("Enter a jersey number to delete:"))
    to_delete = 0
    for player in players_dict:
        if players_dict[player]["jersey"] == player_jersey_delete:
            to_delete = player

    if to_delete == 0:
        print("Failed to find player")
        return delete_player(players_dict)
    # can not delete while iterating
    del players_dict[to_delete]
    return players_dict

def update_player_rating(players_dict):
    player_rating_update = int(input("Enter a jersey number to update rating:"))
    new_rating = int(input("Enter a new rating for the player: "))

    while 1 >new_rating or new_rating >= 11:
        new_rating = int(input("please enter a number between 1-10 for rating:"))

    to_update = 0
    for player in players_dict:
        if players_dict[player]["jersey"] == player_rating_update:
            to_update = player

    if to_update == 0:
        print("Failed to find player")
        return update_player_rating(players_dict)

    players_dict[to_update]["rating"] = new_rating
    return players_dict

def rated_players(players_dict):
    rating = int(input("Enter a rating:\n"))
    above_rating = {}

    for player in players_dict:
        if players_dict[player]["rating"]>rating:
            above_rating[player] = players_dict[player]

    def sort_jersey(player):
        return players_dict[player]["jersey"]

    sorted_dict = sorted(above_rating,key=sort_jersey)
    print(f"ABOVE {rating}")
    for player in sorted_dict:
        print(f"Jersey number: {players_dict[player]['jersey']}, Rating: {players_dict[player]['rating']}")
    print()

if __name__ == "__main__":
    players_roster = create_roster()
    roster_output(players_roster)
    menu_choice = menu()
    print()
    while menu_choice != 'q':
        if menu_choice == "a":
            players_roster = add_player(players_roster)
        elif menu_choice == "d":
            players_roster = delete_player(players_roster)
        elif menu_choice == "u":
            players_roster = update_player_rating(players_roster)
        elif menu_choice == "r":
            rated_players(players_roster)
        elif menu_choice == "o":
            roster_output(players_roster)

        menu_choice = menu()
