# The words parameter is a list of strings.
def build_dictionary(words):
    my_dict = {}
    for word in words:
        if my_dict.get(word, False):
            my_dict[word]+=1
        else:
            my_dict[word]=1
    return my_dict


# words =["hey", "hi", "Mark", "hi", "mark"]


# The following code asks for input, splits the input into a word list,
# calls build_dictionary(), and displays the contents sorted by key.
# if __name__ == "__main__":
#     words = input().split()
#     your_dictionary = build_dictionary(words)
#     sorted_keys = sorted(your_dictionary.keys())
#     for key in sorted_keys:
#         print(f"{ key } - { str(your_dictionary[key]) }")




# music = {
#     "Pink Floyd": {
#         "The Dark Side of the Moon": {
#             "songs": ["Speak to Me", "Breathe", "On the Run", "Money"],
#             "year": 1973,
#             "platinum": True,
#         },
#         "The Wall": {
#             "songs": ["Another Brick in the Wall", "Mother", "Hey you"],
#             "year": 1979,
#             "platinum": True,
#         },
#     },
#     "Justin Bieber": {
#         "My World": {
#             "songs": ["One Time", "Bigger", "Love Me"],
#             "year": 2010,
#             "platinum": True,
#         }
#     },
# }
#
# # Get user input
# print("Lets add to your library")
#
# artist = input("Artist name: ")
# album = input("Album name: ")
#
#
# if music.get(artist, False):
#     if music[artist].get(album,False):
#         songs = input("Would you like to add a song: \n\n\t type exit to leave")
#         while songs != "exit":
#             if music[artist][album]["songs"].get(songs,False):
#                 print("song is in album")
#                 songs = input("Would you like to add a song: \n\n\t type exit to leave")
#             else:
#                 music[artist][album]["songs"].append(songs)
#     else:
#         songs = input("Would you like to add a song: \n\n\t type exit to leave")
#         while songs != "exit":
#             if music[artist][album]["songs"].get(songs,False):
#                 print("song is in album")
#                 songs = input("Would you like to add a song: \n\n\t type exit to leave")
#             else:
#                 music[artist][album]["songs"].append(songs)
#         music[artist].update({album:{"songs":songs}})
# else:
#     songs = input("Add some songs: ").split()
#     music.update({artist:{album:{"songs":songs}}})
#
# print("This is the library:")
# print(music)




# students = {"Stephen":{"Grade":"B-"}}
# students["Jose"] = {"Grade":"A+"}
# print("Jose:")
# print(students)
# print("extra")
