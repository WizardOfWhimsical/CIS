import requests
import json

url="https://api.open5e.com/v2/"
# ARMOR_URL = ""

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def clean_name(name):
    return name.replace("_", " ")

def title(str):
    print("****************")
    print(f"{str}")
    print("****************")

# shows key/values in alphabetic digestible information
def print_information(item):
    sorted_item = sorted(item.keys())
    title(item['name'])
    for key in sorted_item:
        if key != 'document':
            print(f"{clean_name(key)}:\n\t {item[key]}")
# prints whole object
def show_object(obj):
    for item in obj:
        print(item)
# shows single key of nested dict in a list
def show_list_objects(obj,key):
    for item in obj:
        print(item[key])

def fetch(url):
    print("fetching info....")
    response = requests.get(url)

    if response.status_code != 200:
        print("something went wrong in fetch")

    print("successfully recieved.")
    dicts_list = response.json()

    return dicts_list

def print_menu_choices(menu):
    sorted_keys_list = sorted(menu.keys())
    title("MENU CHOICES")
    show_object(sorted_keys_list)
    print()
    choice = input("Please pick an Option on the menu as you see it\n")
    return choice

def get_info(choice):
    sorted_name = sorted(choice['results'], key=lambda item:item["name"])

    # title("ARMOR")
    #
    show_list_objects(sorted_name,'name')
        # for item in obj:
            # print(item[key])
    for item in sorted_name:
        print(item['name'])

    get_armor = input("Please pick an armor choice to investigate\n")

    while get_armor != "q":
        # armor_info ={}

        for item in choice['results']:
            if item['name']==get_armor:
                # only shows keys right now
                # show_object(item)
                print_information(item)
                get_armor = input()




        # jprint(armor_info)
        get_armor = input("what to do next?")
    # print(choice['results'][i][get_armor])


if __name__ == "__main__":

    choice = input("Would you like to get started...")
    while choice != 'q':
        # get menu
        get_menu = fetch(url)
        # orginazies menu alphabetically and puts keys on screen for api choice
        get_choice = print_menu_choices(get_menu)
        # -------------------------------------
        # next api request bease on menu choice
        next_step = fetch(get_menu[get_choice])
        # gets armor keys an places them onscreen/no value returned yet
        get_info(next_step)
        # jprint(menu)
        print("END")
        choice = input()

# response = requests.get("http://api.open-notify.org/astros.json")
# print(menu)
# for person in list_people["people"]:
#     print(f"{person['name']} in on {person['craft']} in space-station")
# print(json.dumps(response.json(),indent=4))
