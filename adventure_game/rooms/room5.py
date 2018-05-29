import adventure_game.my_utils as utils

room5_inventory = {

}

room5_status = {
    "east_locked": 1
}

room5_description = '''
    . . . Room 5. . .
    You see a room with stone brick walls and floor, covered in old growth
    vines that are almost a foot in diameter. As you enter this room you 
    certain memories begin to come back to you. You remember running 
    through a dense jungle, but you can't remember why, and you remember
    tripping over roots that look very similar to the ones in this room. You
    remember falling into dark hole maybe 10 feet wide that seemed to 
    have no end. After that you only remember blackness and then waking 
    up in this maze. 

    You carefully navigate through the room and find passages to the north,
    south, and east. The passage to the east is blocked by vines, you will have to
    burn them down to move east.
    '''

room5_description_no_vines = '''
    . . . Room 5. . .
    You see a room with stone brick walls and floor, covered in old growth
    vines that are almost a foot in diameter. As you enter this room you 
    certain memories begin to come back to you. You remember running 
    through a dense jungle, but you can't remember why, and you remember
    tripping over roots that look very similar to the ones in this room. You
    remember falling into dark hole maybe 10 feet wide that seemed to 
    have no end. After that you only remember blackness and then waking 
    up in this maze. 

    You carefully navigate through the room and find passages to the north,
    south, and east.
    '''

#ROOM 5

def run_room(player_inventory):

    if room5_status["east_locked"] == 1:
        print(room5_description)
    else:
        print(room5_description_no_vines)

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
                next_room = 6
                done_with_room = True
            elif go_where == "north":
                next_room = 4
                done_with_room = True
            elif go_where == "east":
                if room5_status["east_locked"] == 1:
                    print("Vines block your path, try burning them down")
                else:
                    next_room = 8
                    done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room5_inventory)
        elif the_command == "examine":
            if room5_status["east_locked"] == 1:
                print(room5_description)
            else:
                print(room5_description_no_vines)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room5_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "torch":
                utils.use_torch(use_what, player_inventory, room5_status, "east_locked")
            else:
                print("There is no reason to use,", use_what, "here")
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room5_inventory, drop_what)
        else:
            print("I do not understand", the_command)

    return next_room