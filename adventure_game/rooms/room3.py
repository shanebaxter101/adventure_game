import adventure_game.my_utils as utils

# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
room3_description = '''
    . . . Room 3 . . .  
    You are in a grand room with tall ceilings and cracking marble pillars. There are huge
    oak bookshelves all around the room, yet there are no books in the entire room. You
    see an arched passage to the west and a less palatial passage to the east.'''

room3_inventory = {

}

room3_status = {
    "door_locked": 0
}


def run_room(player_inventory):
    # Let the user know what the room looks like
    print(room3_description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "examine"]
    no_args = ["status", "examine"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        # now deal with the command
        if the_command == 'go':
            go_where = response[1]
            if go_where == "west":
                next_room = 1
                done_with_room = True
            elif go_where == "east":
                next_room = 4
                done_with_room = True
            else:
                print("You cannot go,", go_where)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room3_inventory, take_what)
        elif the_command == "status":
            utils.room_status(room3_inventory)
            utils.player_status(player_inventory)
        elif the_command == "examine":
            print(room3_description)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room3_inventory, drop_what)
        else:
            print("I do not understand", the_command)

            # END of WHILE LOOP
    return next_room

