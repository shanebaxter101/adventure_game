import adventure_game.my_utils as utils

room1_inventory = {

}

room1_status = {
    "door_locked": 0,
    "cobwebs_up": 1
}

description = '''
    . . . Starting Room. . . 
    You are in the room where you awoke, you see an arched passage to the east
    that is blocked by huge cobwebs and a staircase going down to the south.
     '''

description_no_web = '''
    . . . Starting Room. . . 
    You are in the room where you awoke, you see an arched passage to the east
    and a staircase going down to the south.
    '''

def run_room(inventory):

    if room1_status["cobwebs_up"] == 1:
        print(description)
    else:
        print(description_no_web)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "examine"]
    no_args = ["status", "examine"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                next_room = 2
                done_with_room = True
            elif direction == 'east':
                if room1_status["cobwebs_up"] == 1:
                    print("you will have to chop down the cobwebs in order to proceed")
                else:
                    next_room = 3
                    done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(inventory, room1_inventory, take_what)
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(inventory, room1_inventory, drop_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, inventory)
            elif use_what == "sword":
                utils.use_sword(use_what, inventory, room1_status)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "status":
            utils.room_status(room1_inventory)
            utils.player_status(inventory)
        elif the_command == "examine":
            if room1_status["cobwebs_up"] == 1:
                print(description)
            else:
                print(description_no_web)





    # end of while loop
    return next_room
