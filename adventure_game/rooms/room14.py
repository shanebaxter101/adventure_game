import adventure_game.my_utils as utils

#ROOM 14

room14_description = '''
    . . . Room 14. . .
    You descend farther down the stairs and enter a room with moss and algae 
    covering every inch of the walls. The room looks like a rainbow due to the variety
    of organisms growing, there are greens, reds, purples, and blues all across the 
    walls. Moss has grown all over a passage to the south, maybe you could burn
    the moss down.
    There are stairs leading further down to the south and stairs leading up to the east.'''

room14_description_no_moss = '''
    . . . Room 14. . .
    You descend farther down the stairs and enter a room with moss and algae 
    covering every inch of the walls. The room looks like a rainbow due to the variety
    of organisms growing, there are greens, reds, purples, and blues all across the 
    walls. 
    There are stairs leading further down to the south and stairs leading up to the east.'''



room14_inventory = {

}

room14_status = {
    "south_locked": 1
}

def run_room(player_inventory):
    if room14_status["south_locked"] == 1:
        print(room14_description)
    else:
        print(room14_description_no_moss)

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
                if room14_status["south_locked"] == 1:
                    print("You need to get rid of the moss in order to proceed to the south")
                else:
                    next_room = 15
                    done_with_room = True
            elif go_where == "east":
                next_room = 2
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room14_inventory)
        elif the_command == "examine":
            if room14_status["south_locked"] == 1:
                print(room14_description)
            else:
                print(room14_description_no_moss)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room14_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch(use_what, player_inventory, room14_status, "south_locked")
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room14_inventory, drop_what)
        else:
            print("I do not understand:", the_command)

    return next_room