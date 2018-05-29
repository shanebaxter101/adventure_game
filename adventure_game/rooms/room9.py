import adventure_game.my_utils as utils

#ROOM 9

room9_description = '''
    . . .Room 9. . .
    You enter a long skinny room that is well lit with lanterns hanging 
    the ceiling. There are only two exits in this room and you feel drawn
    to the other side of this massive hall. There is a cobweb covered 
    purple carpet going down the middle of the wooden floor and statues
    of old men with unreadable plaques line line each side of the room.
    There is a passage to the east and the west.'''

room9_inventory = {

}

def run_room(player_inventory):
    print(room9_description)

    commands = ["go", "take", "drop", "use", "status", "examine"]
    no_args = ["status", "examine"]

    next_room = -1

    done_with_room = False
    while not done_with_room:
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == "go":
            go_where = response[1]
            if go_where == "west":
                next_room = 8
                done_with_room = True
            elif go_where == "east":
                next_room = 10
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room9_inventory)
        elif the_command == "examine":
            print(room9_description)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room9_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room9_inventory, drop_what)
        else:
            print("I do not understand:", the_command)

    return next_room