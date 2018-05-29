import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")

# room imports
import adventure_game.rooms.room1 as r1
import adventure_game.rooms.room2 as r2
import adventure_game.rooms.room3 as r3
import adventure_game.rooms.room4 as r4
import adventure_game.rooms.room5 as r5
import adventure_game.rooms.room6 as r6
import adventure_game.rooms.room7 as r7
import adventure_game.rooms.room8 as r8
import adventure_game.rooms.room9 as r9
import adventure_game.rooms.room10 as r10
import adventure_game.rooms.room11 as r11
import adventure_game.rooms.room12 as r12
import adventure_game.rooms.room13 as r13
import adventure_game.rooms.room14 as r14
import adventure_game.rooms.room15 as r15

from colorama import init
init()

print("\n\nyou awake in a dimly lit room with cracking stone walls that seem to be ages old.\n"
      "The only sources of light are a torch on the wall and a small beam of light\n"
      "coming through a hole directly above the spot where you woke up. Your\n"
      "head is caked in dried blood and your brain feels like it is pounding against\n"
      "the sides of your skull. You need to find a way out of this place, but you do \n"
      "remember exactly why. You take the torch from its place on the wall and\n"
      "begin your quest to escape this foul place.\n"
      " * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n")

print("""

. . .How to Play. . .
-type 'status' to see what items you currently have in your inventory and 
  the items that are available in the room you are currently in
-type ' examine to see the room description again
-type 'go' followed by 'north', 'south', 'east', or 'west' to move from 
  room to room in the maze
-all items that can be interacted with have asterisks next to them, like a 
  *sword*
-type 'take' followed by an item in the room to add it to your inventory
-type 'drop' followed by an item in your inventory to drop it in a room you 
  are currently in
-type 'use' followed by an item in your inventory to use that item, but items
  can only be used in specific rooms
-Try to escape the maze!""")

# Default the player to the first room
room_number = 1

# Player Inventory
player_inventory = {
    'torch': 1
}

should_continue = True
while should_continue:
    if room_number == 1:
        room_number = r1.run_room(player_inventory)
    elif room_number == 2:
        room_number = r2.run_room(player_inventory)
    elif room_number == 3:
        room_number = r3.run_room(player_inventory)
    elif room_number == 4:
        room_number = r4.run_room(player_inventory)
    elif room_number == 5:
        room_number = r5.run_room(player_inventory)
    elif room_number == 6:
        room_number = r6.run_room(player_inventory)
    elif room_number == 7:
        room_number = r7.run_room(player_inventory)
    elif room_number == 8:
        room_number = r8.run_room(player_inventory)
    elif room_number == 9:
        room_number = r9.run_room(player_inventory)
    elif room_number == 10:
        room_number = r10.run_room(player_inventory)
    elif room_number == 11:
        room_number = r11.run_room(player_inventory)
    elif room_number == 12:
        room_number = r12.run_room(player_inventory)
    elif room_number == 13:
        room_number = r13.run_room(player_inventory)
    elif room_number == 14:
        room_number = r14.run_room(player_inventory)
    elif room_number == 15:
        room_number = r15.run_room(player_inventory)
    elif room_number == 42:
        should_continue = False

    else:
        print("Ack I don't know room number:", room_number)
        break

#

print("The game has ended...")
