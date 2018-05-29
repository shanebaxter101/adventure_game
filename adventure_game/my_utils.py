# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments = ['status', 'help']):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False;
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result

#has_A: will check whether or not a dictionary has the item specified
#it will check if count is greater that 1

def has_a(player_inventory, item):
    if item in player_inventory.keys():
        count = player_inventory[item]
        if count > 0:
            return True
        else:
            return False
    else:
        return False
def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        current_count = player_inventory[item]
        player_inventory[item] = current_count - 1
        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count + 1
        else:
            room_inventory[item] = 1
        print("you dropped the", item)
    else:
        print("You cannot drop what you do not possess")

#end of drop_item

def take_item(player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        print(item, "was added to your inventory")
        room_count = room_inventory[item]
        room_inventory[item]
        room_inventory[item] = room_count - 1
        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
    else:
        print("you cannot take imaginary things!")

def room_status(room_inventory):
    print("\tIn the room you see:")

    nothing = True

    for key in room_inventory.keys():
        if room_inventory[key] > 0:
            nothing = False
            print("\t\t", key)

    if nothing == True:
        print("\t. . .sadly, nothing.")

def player_status(player_inventory):
    print("\t you currently possess:")
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print("\t\t", key, " : ", player_inventory[key])

def use_gem(gem, player_inventory, room_status):
    if has_a(player_inventory, gem):
        print("The", gem, "locks into place in the pedestal and you hear a series \n"
                          "of clicks within it")
        room_status[gem] = 1
        player_inventory[gem] = 0
    else:
        print("You cannot use what you do not possess")

def use_torch(item, player_inventory, room_status, locked_room):
    if has_a(player_inventory, item):
        if room_status[locked_room] == 1:
            room_status[locked_room] = 0
            print("The path has been opened, thanks to your trusty torch")
        else:
            print("It becomes much easier to see, its pretty gross in here though.")
    else:
        print("Why did you even drop your torch anyways?")

def use_torch1(item, player_inventory):
    if has_a(player_inventory, item):
        print("It becomes much easier to see, its pretty gross in here though.")
    else:
        print("Why did you even drop your torch anyways?")

def use_sword(item, player_inventory, room_status):
    if room_status["cobwebs_up"] == 1:
        if has_a(player_inventory, item):
            print("You chop down the cobwebs with your *sword* and open the passage to the east")
            room_status["cobwebs_up"] = 0
        else:
            print("You cannot use what you do not possess")
    else:
        print("There is no reason to use sword here")


