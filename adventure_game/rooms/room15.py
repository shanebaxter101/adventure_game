import adventure_game.my_utils as utils

#ROOM 15

room15_inventory = {
    "sword": 1
}

room15_description = '''
    . . .Room 15. . .
    You descend further down and enter a room with a small layer of water 
    covering the floor. You see a skeleton lying in the corner of the room 
    with a *sword* still in its bony dead hand. There are odd mushrooms 
    growing all around the room through cracks in the stone floor.
    You see stairs leading up to the north.'''

room15_description_no_sword = '''
    . . .Room 15. . .
    You descend further down and enter a room with a small layer of water 
    covering the floor. You see a skeleton lying in the corner of the room. 
    There are odd mushrooms growing all around the room through cracks 
    in the stone floor.
    You see stairs leading up to the north.'''

def run_room(player_inventory):
    sword_count = room15_inventory["sword"]
    if sword_count < 1:
        print(room15_description_no_sword)
    else:
        print(room15_description)

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
                next_room = 14
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room15_inventory)
        elif the_command == "examine":
            sword_count = room15_inventory["sword"]
            if sword_count < 1:
                print(room15_description_no_sword)
            else:
                print(room15_description)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room15_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room15_inventory, drop_what)
        else:
            print("I do not understand:", the_command)

    return next_room