import adventure_game.my_utils as utils

#ROOM 7

room7_inventory = {
    "key": 1
}

room7_status = {
    "door_locked": 0
}

room7_description = '''
    . . .Room 7. . .
    You enter a small, dank room with a wooden bench and a tiny jail cell in the back. 
    Inside the cell is a skeleton sitting atop an upturned bucket with its back against
    the wall. The prisoner must have died decades ago. On a key ring next to the 
    cell is a rusty old *key* with a bone of some sort below it. 
    You see a passage to the north and the west.
    '''
room7_description_no_key = '''
    . . .Room 7. . .
    You enter a small, dank room with a wooden bench and a tiny jail cell in the back. 
    Inside the cell is a skeleton sitting atop an upturned bucket with its back against
    the wall. The prisoner must have died decades ago. You see an empty key ring
     with a bone below it.
    You see a passage to the north and the west.
    '''
def run_room(player_inventory):
    key_count = room7_inventory["key"]
    if key_count < 1:
        print(room7_description_no_key)
    else:
        print(room7_description)

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
                next_room = 8
                done_with_room = True
            elif go_where == "west":
                next_room = 6
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room7_inventory)
        elif the_command == "examine":
            key_count = room7_inventory["key"]
            if key_count < 1:
                print(room7_description_no_key)
            else:
                print(room7_description)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room7_inventory, take_what)
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room7_inventory, drop_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        else:
            print("I do not understand", the_command)

    return next_room