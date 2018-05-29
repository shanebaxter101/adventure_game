import adventure_game.my_utils as utils

#ROOM 8

room8_inventory = {
    "coin": 1
}

room8_description = '''
    . . .Room 8. . .
    You are in a room filled with empty steel cages with thick metal bars. 
    The cages have small tufts of fur and feathers, and some even have
    small spots of caked blood on them, yet they all appear to be vacant.
    There is one that is one cage in the center of the room that is about 
    seven feet tall, with its door ajar, and littered with huge bones.
    Inside the huge cage is a shiny *coin* next to a human hand that is only
    bone.
    You see a passage to the south, east, and west.
    '''

room8_description_no_coin = '''
    . . .Room 8. . .
    You are in a room filled with empty steel cages with thick metal bars. 
    The cages have small tufts of fur and feathers, and some even have
    small spots of caked blood on them, yet they all appear to be vacant.
    There is one that is one cage in the center of the room that is about 
    seven feet tall, with its door ajar, and littered with huge bones.
    You see a passage to the south, east, and west.
    '''

def run_room(player_inventory):
    coin_count = room8_inventory["coin"]
    if coin_count < 1:
        print(room8_description_no_coin)
    else:
        print(room8_description)

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
                next_room = 7
                done_with_room = True
            elif go_where == "west":
                next_room = 5
                done_with_room = True
            elif go_where == "east":
                next_room = 9
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room8_inventory)
        elif the_command == "examine":
            coin_count = room8_inventory["coin"]
            if coin_count < 1:
                print(room8_description_no_coin)
            else:
                print(room8_description)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room8_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room8_inventory, drop_what)
        else:
            print("I do not understand", the_command)

    return next_room