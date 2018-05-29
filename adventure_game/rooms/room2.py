import adventure_game.my_utils as utils

#Items currently in room

room2_inventory = {
    "coin": 1
}

room2_status = {
    "door_locked": 0
}


# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
#
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory):
    description = '''
    . . .Room 2. . . 
    You carefully walk down the stairs and descend into a cramped room with barrels stacked to 
    the ceiling. Whatever was inside them became rotten years ago and they expel a nearly 
    unbearable odor. Atop a barrel you see a *coin* glistening in the torchlight. You
    see stairs leading up to the north and stairs leading further down to the west.
    '''
    no_coin_description = '''
    . . .Room 2. . . 
    You carefully walk down the stairs and descend into a cramped room with barrels stacked to 
    the ceiling. Whatever was inside them became rotten years ago and they expel a nearly 
    unbearable odor. 
    You see stairs leading up to the north and stairs leading further down to the 
    west.
    '''

    coin_count = room2_inventory["coin"]
    if coin_count < 1:
        print(no_coin_description)
    else:
        print(description)

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
            if direction == 'north':
                next_room = 1
                done_with_room = True
            elif direction == "west":
                next_room = 14
                done_with_room = True
            else:
                print("There is no way to go,", direction)
        elif the_command == 'take':
            take_what = response[1]
            utils.take_item(player_inventory, room2_inventory, take_what)
        elif the_command == "status":
            utils.room_status(room2_inventory)
            utils.player_status(player_inventory)
        elif the_command == "examine":
            coin_count = room2_inventory["coin"]
            if coin_count < 1:
                print(no_coin_description)
            else:
                print(description)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.drop_item(player_inventory, room2_inventory, drop_what)
        else:
            print("I do not understand", the_command)

    # end of main while loop
    return next_room
