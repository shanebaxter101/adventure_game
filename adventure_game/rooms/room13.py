import adventure_game.my_utils as utils

#ROOM 13

room13_inventory = {

}

room13_status = {
    "ruby": 0,
    "emerald": 0,
    "sapphire": 0
}
room13_description = """
    . . .Room 13. . .
    You walk into a grand room with marble walls and floors and gem encrusted
    lanterns hanging from the walls. There is a high glass ceiling and  
    the brilliant light of the sun shines down and burns your eyes. There is 
    a pedestal in the center of the room with three different shaped sockets. There 
    is an ancient inscription on the front of the pedestal reading: 
    'Place three gems here and you will may get out of here. Your quest 
    will come to its end as these great doors ascend.'
    This room marks the end of your great adventure, all you need is the 
    three gems mentioned, hopefully they are nearby.
    You see a passage to the west."""

end_game = """
    . . .The End. . .
    The walls in front of you begin to rise, as if by magic. The light of the sun
    pierces through and blinds you. As your eyes adjust to the light you see that 
    there is a forest in front of you and a trail leading ot from the room. You 
    may have escaped the dungeon, but your journey has just begun."""

def run_room(player_inventory):
    print(room13_description)

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
                next_room = 10
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "take":
            take_what = response[1]
            utils.take_item(player_inventory, room13_inventory, take_what)
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room13_inventory, drop_what)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room13_inventory)
        elif the_command == "examine":
            print(room13_description)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "ruby":
                utils.use_gem("ruby", player_inventory, room13_status)
                if room13_status["ruby"] == 1 and room13_status["sapphire"] == 1 and room13_status["emerald"] == 1:
                    print(end_game)
                    next_room = 42
                    done_with_room = True
            elif use_what == "sapphire":
                utils.use_gem("sapphire", player_inventory, room13_status)
                if room13_status["ruby"] == 1 and room13_status["sapphire"] == 1 and room13_status["emerald"] == 1:
                    print(end_game)
                    next_room = 42
                    done_with_room = True
            elif use_what == "emerald":
                utils.use_gem("emerald", player_inventory, room13_status)
                if room13_status["ruby"] == 1 and room13_status["sapphire"] == 1 and room13_status["emerald"] == 1:
                    print(end_game)
                    next_room = 42
                    done_with_room = True
            elif use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use,", use_what, "here")

        else:
            print("I do not understand:", the_command)

    return next_room