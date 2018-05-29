import adventure_game.my_utils as utils

#ROOM 4


room4_inventory = {
    "coin": 1
}

room4_status = {
    "door_locked": 0
}

def run_room(player_inventory):
    room4_description = '''
    . . . Room 4 . . .
    You enter a smaller well lit room with polished, pristine, wooden walls and a cowled 
    figure sitting at a well kept desk. Before you can get a good look at the figure he 
    runs out of the room to the south at an almost inhuman speed. In its haste the creature forgot one shimmering 
    *coin* on the desk. There is a passage to the south and the west.'''

    room4_description_no_coin = '''
    . . . Room 4 . . .
    You enter a smaller well lit room with polished, pristine, wooden walls and a well 
    kept desk and short stool. There is a passage to the south and the west '''

    coin_count = room4_inventory["coin"]
    if coin_count < 1:
        print(room4_description_no_coin)
    else:
        print(room4_description)

    commands = ["go", "take", "drop", "use", "status", "examine"]
    no_args = ["status", "examine"]

    next_room = -1

    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == "go":
            go_where = response[1]
            if go_where == "south":
                next_room = 5
                done_with_room = True
            elif go_where == "west":
                next_room = 3
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room4_inventory, take_what)
        elif the_command == "status":
            utils.room_status(room4_inventory)
            utils.player_status(player_inventory)
        elif the_command == "examine":
            coin_count = room4_inventory["coin"]
            if coin_count < 1:
                print(room4_description_no_coin)
            else:
                print(room4_description)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room4_inventory, drop_what)
        else:
            print("I do not understand", the_command)

    return next_room
