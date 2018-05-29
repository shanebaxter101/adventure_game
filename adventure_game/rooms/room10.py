import adventure_game.my_utils as utils

#ROOM 10

room10_inventory = {
    "emerald": 1
}

room10_description = """
    . . .Room 10. . .
    You walk into a small room with a large square room with a small booth of 
    some sort in a corner. There is a small man with lots of jewelry at the booth.
    He seems to be a merchant of some sort, but he has nothing on display in his
    booth. As you get closer the man yells out to you. 
    'Oh great, its another one of you pesky adventurers acting like you own 
    this whole place', says the man in an aggressive tone.  
    'All you idiots do is steal all of my supplies, gold, and rare animals and run 
    off with the stuff without paying me squat!'
    'The last brainhead that came through here released my rare greenspike
    dragon and tried to fight it without a sword!'
    He continues by saying, 'maybe you could prove to me you aren't like those 
    other dunces by buying my last *emerald* for only 4 gold *coins*'.
    You see a passage to the north, south, eas, and west. ."""

room10_description_no_emerald = """
    . . .Room 10. . .
     You walk into a small room with a large square room with a small booth of 
    some sort in a corner. There is a small man with lots of jewelry at the booth.
    He seems to be a merchant of some sort, but he has nothing on display in his
    booth. As you get closer the man yells out to you.
    'Hey good luck on getting out of here buddy, I know you can do it!', he says.
    You see a passage to the north, south, east and west. There is a locked door to 
    the south.
    """

def run_room(player_inventory):
    emerald_count = room10_inventory["emerald"]
    if emerald_count < 1:
        print(room10_description_no_emerald)
    else:
        print(room10_description)

    commands = ["go", "take", "drop", "use", "status", "examine"]
    no_args = ["status", "examine"]

    next_room = -1

    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == "go":
            go_where = response[1]
            if go_where == "north":
                next_room = 11
                done_with_room = True
            elif go_where == "west":
                next_room = 9
                done_with_room = True
            elif go_where == "east":
                next_room = 13
                done_with_room = True
            elif go_where == "south":
                next_room = 12
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room10_inventory)
        elif the_command == "examine":
            emerald_count = room10_inventory["emerald"]
            if emerald_count < 1:
                print(room10_description_no_emerald)
            else:
                print(room10_description)
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room10_inventory, drop_what)
        elif the_command == "take":
            take_what = response[1]
            coin_count = player_inventory["coin"]
            if take_what == "emerald" and coin_count > 0:
                print("Hey, stealing is not very nice!")
            else:
                utils.take_item(player_inventory, room10_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "coin" or use_what == "coins":
                current_coin_count = player_inventory["coin"]
                if current_coin_count == 4:
                    utils.take_item(player_inventory, room10_inventory, "emerald")
                    player_inventory["coin"] = 0
                    print("Wow, maybe you are better than those other adventurers,\n"
                          "thanks for your purchase!")
                else:
                    print("You are gonna need more money than that! I said 4 coins\n "
                          "and I ain't budgin'")
            elif use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use", use_what, "here")
        else:
            print("I do not understand", the_command)

    return next_room