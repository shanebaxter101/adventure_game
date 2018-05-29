import adventure_game.my_utils as utils

#ROOM 12

room12_inventory = {
    "sapphire": 1
}

room12_status = {
    "chest locked": 1
}

room12_description = """
    . . .Room 12. . .
    You walk into a tiny room with nothing but a chest directly in the middle of 
    the room. When you get closer you see the chest is quite old and is made of
    cracking wood, yet it is still sturdy and the golden padlock is still spotless 
    and simmering.  You are going to need a *key* to open this thing.
    You see a passage to the north."""

room12_description_chest_unlocked_sapphire_inside = """
    . . .Room 12. . .
    You walk into a tiny room with nothing but a chest directly in the middle of 
    the room. When you get closer you see the chest is quite old and is made of
    cracking wood, yet it is still sturdy and the golden padlock is still spotless 
    and simmering.  The chest is wide open and there is a beautiful *sapphire*
    lying inside.
    You see a passage to the north."""

room12_description_chest_unlocked_no_sapphire = """
    . . .Room 12. . .
    you walk into a tiny room with nothing but a chest directly in the middle of 
    the room. When you get closer you see the chest is quite old and is made of
    cracking wood, yet it is still sturdy and the golden padlock is still spotless 
    and simmering.  The chest is wide open but there is nothing inside. 
    You see a passage to the north."""


def run_room(player_inventory):
    if room12_status["chest locked"] == 1:
        print(room12_description)
    elif room12_status["chest locked"] == 0 and room12_inventory["sapphire"] == 1:
        print(room12_description_chest_unlocked_sapphire_inside)
    else:
        print(room12_description_chest_unlocked_no_sapphire)

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
                next_room = 10
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room12_inventory)
        elif the_command == "examine":
            if room12_status["chest locked"] == 1:
                print(room12_description)
            elif room12_status["chest locked"] == 0 and room12_inventory["sapphire"] == 1:
                print(room12_description_chest_unlocked_sapphire_inside)
            else:
                print(room12_description_chest_unlocked_no_sapphire)
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room12_inventory, drop_what)
        elif the_command == "take":
            take_what = response[1]
            if take_what == "sapphire":
                if room12_status["chest locked"] == 0:
                    utils.take_item(player_inventory, room12_inventory, "sapphire")
                else:
                    print("You cannot take the sapphire while the chest is locked")
            else:
                utils.take_item(player_inventory, room12_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "key":
                if player_inventory["key"] > 0:
                    player_inventory["key"] = 0
                    room12_status["chest locked"] = 0
                    print("You unlock the chest with your *key* and see a \n"
                          "massive shining blue *sapphire*")
                else:
                    print("You cannot use what you do not possess")
            elif use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use", use_what, "here")
        else:
            print("I do not understand:", the_command)

    return next_room
