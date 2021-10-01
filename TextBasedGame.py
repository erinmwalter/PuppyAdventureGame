#defining baseline status of starting in foyer and having zero inventory
user_room = 'Foyer'
user_toys = []
valid_directions = ['north', 'south', 'east', 'west']

#dictionary for all rooms in the game and directions user can move in
rooms = {
    'Foyer' : {'east': 'Living Room', 'south':'None', 'west': 'None', 'north': 'None'},
    'Living Room' : {'north': 'Bedroom', 'south': 'Office', 'east':'Kitchen', 'west': 'Foyer'},
    'Bedroom': {'east': 'Bathroom', 'south': 'Living Room', 'north':'None', 'west':'None'},
    'Bathroom': {'west': 'Bedroom', 'east':'None', 'north':'None', 'south': 'None'},
    'Dining Room': {'south': 'Kitchen', 'west': 'None', 'north': 'None', 'east':'None'},
    'Kitchen': {'north':'Dining Room', 'west':'Living Room','south': 'None', 'east':'None'},
    'Office': {'north': 'Living Room', 'east':'Basement', 'south':'None', 'west': 'None'},
    'Basement': {'west':'Office', 'south':'None', 'east': 'None', 'north':'None'}
}

#dictionary for toys and their room locations
toys = {
    'Foyer' : 'None',
    'Living Room': 'cushion',
    'Bedroom' : 'sock',
    'Bathroom' : 'roll',
    'Dining Room': 'shoe',
    'Kitchen' : 'treat',
    'Office' : 'cord',
    'Basement' : 'owner',
}

#function to move between rooms
def move_between_rooms(command):
    for rm, val in rooms.items(): #searches each room in dictionary to find which room you are in
        if rm == user_room:
            new_room = rooms[rm][command] #makes your new room the value matching direction you chose
    if new_room == 'None':
        print("Can't go there!") #if the user picks a selection that is not available vased on the map.
        new_room = user_room
    return new_room

#function to pick up an item in the room
def collect_toy(command):
    if command == toys[user_room]:
        for rm in toys:
            if rm == user_room:
                user_toys.append(toys[user_room])
                toys[user_room] = 'None'
    else:
        print("Can't get {}".format(command))




#welcome message to the game displayed at the start of each game
def welcome_message():
    print("Welcome to Puppy Adventure Game!")
    print("Use the map to navigate between rooms and collect toys")
    print("Use 'go' to change rooms and 'get' to pick up toy")
    print("Rooms: Bedroom, Bathroom, Dining Room, Kitchen, Living Room, Office, Basement")
    print("Toys: Sock, Roll, Cushion, Shoe, Treat, Cord")
    print("Watch out for your owner in the basement!")

#game over message that will display when game is over
def game_over_message():
    if len(user_toys) == 6:
        print('\nToy Inventory: {}'.format(user_toys))
        print("Congratulations! You collected all the toys")
        print('You have won the game!')
    if user_room == 'Basement':
        print('\nCurrent Room: {}'.format(user_room))
        print("Oh no! You found your owner!")
        print("You look very suspicious.")
        print("You Lose!")
        print("Your owner scolds you and puts you \nin your crate for the rest of the night!")
    print("I hope you enjoyed the game. Goodbye.")

#######
#Start of the game play here
######

welcome_message() #display message for user to see
choice = ' '
while choice != 'exit': #the user can choose to end game by typing Exit at any time
    print('--------------------------------')
    #prints the user's current room
    print('You are in the {}.'.format(user_room))
    #this will check for available directions depending on the room
    #so that the user knows their options for where to move
    print('Available directions:', end = " ")
    for rm in rooms.keys():
        if rm == user_room:
            for dir in rooms[rm].keys():
                if rooms[rm][dir] != 'None':
                    print(dir, end = " ")
    print()
    #this will check if there are toys in the room
    #if there are, it will display which toy is available
    #otherwise it will tell the user there is no toy there
    if toys[user_room] != 'None':
        print('You see a {}'.format(toys[user_room]))
    elif toys[user_room] == 'None':
        print("There's nothing in here.")
    elif toys[user_room] == 'Owner':
        break #if owner is in the room breaks the while loop and goes to game over
    #this displays the toy inventory for the user
    print('Toy Inventory: ', user_toys)
    #asks user to input a move and changes it to lower case
    choice = input("Enter command:").lower()
    choice_list = choice.split() #split user choice into a list to search for go vs get command
    if choice_list[0] == 'go':
        if choice_list[1] in valid_directions: #checks to make sure choice is valid direction
            user_room = move_between_rooms(choice_list[1]) #runs through the move function
        else:
            print("Invalid Selection. Please try again.")
    elif choice_list[0] == 'get':
        collect_toy(choice_list[1]) #runs through the get toy function
    elif choice_list[0] == 'exit': #giving user option to end program
        break #stops the loop and exits the program at user's wish
    else:
        print("Invalid Selection!") #any other choice is invalid
    if len(user_toys) == 6 or user_room == 'Basement':
        break
game_over_message()