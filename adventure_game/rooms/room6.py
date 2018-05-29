import adventure_game.my_utils as utils

#ROOM 6

room6_inventory = {
    "coin": 1
}

room6_status = {
    "door_locked": 0
}



def run_room(player_inventory):

    room6_description = ''' 
    . . .Room 6. . .
    You enter a room filled with wooden crates stacked three high, 
    they all have some odd characters inscribed on their sides that you 
    are unable to read. There are empty flasks, small empty bags with the 
    names of herbs written on them, and in the corner of the room you see
    one, lone, shimmering, *coin*.
    You see a passage to the north, and east'''

    room6_descripton_no_coin =  ''' 
    . . .Room 6. . .
    You enter a room filled with wooden crates stacked three high, 
    they all have some odd characters inscribed on their sides that you 
    are unable to read. There are empty flasks and small empty bags with the 
     names of herbs written on them.
     You see a passage to the north, and east'''
    coin_count = room6_inventory["coin"]
    if coin_count < 1:
        print(room6_descripton_no_coin)
    else:
        print(room6_description)

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
                next_room = 5
                done_with_room = True
            elif go_where == "east":
                next_room = 7
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room6_inventory)
        elif the_command == "examine":
            coin_count = room6_inventory["coin"]
            if coin_count < 1:
                print(room6_descripton_no_coin)
            else:
                print(room6_description)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room6_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room6_inventory, drop_what)
        else:
            print("I do not understand", the_command)

    return next_room