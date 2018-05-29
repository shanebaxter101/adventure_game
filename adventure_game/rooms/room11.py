import adventure_game.my_utils as utils

#ROOM 11

room11_inventory = {
    "ruby": 1
}

room11_status = {
    "dragon alive": 1
}

room11_description = """
    . . .Room 11. . .
    You enter a room bigger than any other you have seen in this place, in 
    the back a massive green dragon, at least 15 feet long, with spikes running
    down its back, sleeps in the back corner atop a pile of bones. You can see
    a glimmering *ruby* next to the dragon, but it would be very foolish to 
    try and grab the ruby without a weapon of some kind. You could probably
    get out without awaking the dragon too.
    You see a passage to the south."""

room11_description_no_dragon_no_ruby = """
    . . .Room 11. . .
    You enter a room bigger than any other you have seen in this place, in 
    the back is a pile of bones and skulls.
    You see a passage to the south."""

room11_description_no_dragon = """
    . . .Room 11. . .
    You enter a room bigger than any other you have seen in this place, in 
    the back is a pile of bones and skulls. You see a *ruby* next to the pile.
    You see a passage to the south."""


def run_room(player_inventory):
    if room11_status["dragon alive"] == 0 and room11_inventory["ruby"] == 0:
        print(room11_description_no_dragon_no_ruby)
    elif room11_status["dragon alive"] == 0 and room11_inventory["ruby"] == 1:
        print(room11_description_no_dragon)
    else:
        print(room11_description)

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
                next_room = 10
                done_with_room = True
            else:
                print("You cannot go", go_where)
        elif the_command == "status":
            utils.player_status(player_inventory)
            utils.room_status(room11_inventory)
        elif the_command == "examine":
            if room11_status["dragon alive"] == 0 and room11_inventory["ruby"] == 0:
                print(room11_description_no_dragon_no_ruby)
            elif room11_status["dragon alive"] == 0 and room11_inventory["ruby"] == 1:
                print(room11_description_no_dragon)
            else:
                print(room11_description)
        elif the_command == "drop":
            drop_what = response[1]
            utils.drop_item(player_inventory, room11_inventory, drop_what)
        elif the_command == "take":
            take_what = response[1]
            if take_what == "ruby":
                if room11_status["dragon alive"] == 0:
                    utils.take_item(player_inventory, room11_inventory, "ruby")
                else:
                    print("Maybe try doing something about that dragon before\n"
                          "taking the *ruby*")
            else:
                utils.take_item(player_inventory, room11_inventory, take_what)
        elif the_command == "use":
            use_what = response[1]
            if use_what == "sword":
                if utils.has_a(player_inventory, "sword"):
                    room11_status["dragon alive"] = 0
                    print("You walk up yo the sleeping dragon very stealthily, as\n"
                          "you approach it you can feel its hot breath as it snores\n"
                          "peacefully. You take your sword and stab straight down\n"
                          "into a crack between its scales near its torso. The\n"
                          "dragon makes a terrible roar and lets loose a jet of\n"
                          "flame straight up into the air through its nostrils. The\n"
                          "dragon then falls lifeless to the ground and you feel it\n"
                          "is much safer now to take the *ruby*.")
                else:
                    print("You cannot use what you do not possess.")
            elif use_what == "torch":
                utils.use_torch1(use_what, player_inventory)
            else:
                print("There is no reason to use", use_what, "here")
        else:
            print("I do not understand", the_command)


    return next_room