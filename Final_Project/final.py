# Final Project: Text adventure
#
# The introduction to the game is displayed to the player below in main function.
import time
import random

START = 1
QUIT = 2

hiking_shoes = "hiking shoes"
faded_blue_jeans = "faded blue jeans"
white_Tshirt = "white T-shirt"
gray_jacket = "gray jacket"
rifle = "rifle"
rifle_bullet = "rifle bullet"
combat_knife = "combat knife"
food = "food"
water = "water"
# Use len to keep constant numbers for each item and keep them in order so you can add or subtract them later
character_contents = [hiking_shoes, faded_blue_jeans, white_Tshirt, gray_jacket, 
                                rifle, rifle_bullet, rifle_bullet, rifle_bullet]
# The water and food variables will equal their numerical value for which I will recognize them by later, not how much
# the player has in resources.
water = 20
food = 40

def main():
    choice = 0
    while choice != QUIT:
        display_menu()
        try:
            print('')
            choice = int(input('Enter your selection: '))
        except ValueError:
            print('')
            time.sleep(1)
            print('INVALID SELECTION! Enter "1" or "2"')
            print('')
            return main()
        if choice == QUIT:
            print('')
            time.sleep(1)
            print('Quitting game...')
            exit()
# The player is prompted to enter their name which will be held in a variable
# used to display their character's name throughout the game. Needs to be returned for later.
        elif choice == START:
            time.sleep(1)
            print('')
            print('Starting game...')
            time.sleep(0.5)
            return character_name()
        else:
            time.sleep(1)
            print('INVALID SELECTION! Enter "1" or "2"')
            print('')
            return main()
    

def display_menu():
    print('                  ┌------------------------------------------┐')
    print("                  |         THE SURVIVOR'S CHRONICLES        |")
    print('                  └------------------------------------------┘')
    print('┌--------------------------------------------------------------------------------------┐')
    print('|The year is 2054, World War III has ended...                                          |')
    print('|The world you once knew is no more. International governments have fallen...          |')
    print('|and society alike, to a state of anarchy. You have no idea where your family is...    |')
    print('|The winter is quickly approaching and you know that the temperature will soon become  |')
    print('|dangerously cold... What will you do next?                                            |')
    print('|______________________________________________________________________________________|')
    print('|                         **All choices you make matter**                              |')                                                             
    print('└--------------------------------------------------------------------------------------┘')
    print('1) Start Game')
    print('2) Quit Game')
            
user_name = str
def character_name():
    print('')
    user_name = str(input("Enter your name: "))
    last_chance = str
    Y = 'Y'
    N = 'N'
    y = 'y'
    n = 'n'
    while last_chance != N or last_chance != n:
        try:
            print('')
            last_chance = str(input('Are you sure? (y/n): '))
        except ValueError:
            print('')
            print('Invalid Selection! Please enter "y" or "n" ')
            return character_name()
        if last_chance == Y or last_chance == y:
            print('')
            time.sleep(1)
            print('Your name is ',user_name,'!')
            print('')
            time.sleep(2)
            print('The game will begin in a few seconds...')
            print('')
            return chapter_1()
        elif last_chance == N or last_chance == n:
            return character_name()
    return user_name

# Chapter 1 will be the function that will include the first real in-game choice that will be offered
# to the player and depending on whether they go right=1 or left=2, will determine the outcomes of later
# events in the next chapters. 
def chapter_1():
    time.sleep(2)
    print('')
    print('                  ┌------------------------------------------┐')
    print("                  |              THE BEGINNING               |")
    print('                  └------------------------------------------┘')
    print('┌-----------------------------------------------------------------------------------------------------┐')
    print('|You have just awoken from a long sleep...                                                            |')
    print('|The last thing you remember is being with your                                                       |') 
    print('|family in your bomb shelter under your house.                                                        |')
    print('|Then there was a sudden flash along with a gigantic                                                  |')
    print('|explosion. The next thing you know, you have awoken.                                                 |')
    print('|You look around and see nothing but ashe covering your once                                          |')
    print('|beautiful home. You have no clue where your family is...                                             |')
    print('|You begin looking around for any sign of life in the area but                                        |')
    print('|find nothing. All you have with you currently is some old hiking                                     |')
    print('|shoes, faded blue jeans, a white t-shirt, and a gray jacket along with                               |')
    print("|your father's rifle with 3 bullets, which you had hidden away in your shelter.                       |")
    print('|Your stomach is rumbling violently and you are quite thirsty.                                        |')
    print('|You look to your right and see a storm coming but what looks like a                                  |')
    print('|enclosed shelter off in the distance. To the left, you see a forest with clear skies surrounding it. |')
    print('|Where will you go?                                                                                   |')
    print('└-----------------------------------------------------------------------------------------------------┘')
    print('1) Go right towards the shelter in the arising storm')
    print('2) Go left towards the forest')
    print('3) Quit game (your progress will NOT be saved)')
    try:
        print('')
        right_left_choice = int(input('Enter your choice: '))
    except ValueError:
        print('')
        print("You didn't make a correct selection! Please enter an one of the displayed integers...")
        return right_left_choice
    if right_left_choice == 1:
        print('')
        print('You chose to go to the right towards the shelter admist the rising storm')
        return right_choice_path()
    if right_left_choice == 2:
        print('')
        print('You chose to go to the left towards the bright forest')
        return left_choice_path()
    if right_left_choice == 3:
        print('')
        print('You chose number 3 to quit the game...')
        print('')
        time.sleep(1.5)
        print('Quitting game...')
        exit()
    else:
        print('')
        print("You didn't make a correct selection! Please enter an one of the displayed integers...")
        return right_left_choice


# The right choice path will develop into a completely different area and offer at least one other significant choice
# that will impact the player's experience based on their choice of where to go next.
# If they choose to go to the bridge, they will end up encoutering a zombie who has a 1/3 chance of killing them.
# If they choose to continue on to the shelter, they will find food/water and gain rest. 
def right_choice_path():
    time.sleep(2)
    print('')
    print('                  ┌------------------------------------------------┐')
    print("                  |              CHOOSING TO GO RIGHT              |")
    print('                  └------------------------------------------------┘')
    print('┌-----------------------------------------------------------------------------------------------------┐')
    print('|You begin to head towards the right, hoping to get to the shelter off in the distance                |')
    print('|before the storm hits. Besides the distant thunder, everything around you is desolate                |')
    print('|and quiet. There are no animals in sight or other people. You know that you must find food and water |')
    print('|fast. After walking towards the shelter for about an hour, you feel a cold droplet of rain fall on   |')
    print('|your head. Then a downpour of colder droplets along with a very close boom. You see an old stone     |')
    print('|bridge close by. If you continue to the shelter you were headed for, you could risk getting hurt from|')
    print('|the storm, but you are starving and need food soon.                                                  |')
    print('|What will you do next?                                                                               |')
    print('└-----------------------------------------------------------------------------------------------------┘')
    print('1) Continue heading to the shelter')
    print('2) Go underneath the bridge to wait out the storm')
    print('3) Quit game (your progress will NOT be saved)')
    try:
        print('')
        shelter_or_bridge_choice = int(input("Enter your choice: "))
    except ValueError:
        print('')
        time.sleep(1)
        print('Invalid Selection! Please enter an one of the displayed integers...')
        right_choice_path()
    if shelter_or_bridge_choice == 1:
        print('')
        print("You chose to continue to head to the shelter")
        return heading_to_shelter_choice()
    if shelter_or_bridge_choice == 2:
        print('')
        print("You chose to go underneath the bridge to wait out the storm")

    if shelter_or_bridge_choice == 3:
        print('')
        time.sleep(1.5)
        print('Quitting game...')
        exit()
    else:
        print('')
        time.sleep(1)
        print('Invalid Selection! Please enter an one of the displayed integers...')
        return right_choice_path()
       
def heading_to_shelter_choice():
    time.sleep(2)
    print('')
    print('                  ┌------------------------------------------------┐')
    print("                  |              CONTINUING TO SHELTER             |")
    print('                  └------------------------------------------------┘')
    print('┌-----------------------------------------------------------------------------------------------------┐')
    print('|You headed for the shelter running the enitre way, through the violent freezing rain and colder wind.|')
    print('|When you arrived at the shelter you run towards the door and begin knocking violently. When no one   |')
    print('|comes to answer, you grab for the handle and turn it, only to discover its locked. You head towards  |')
    print('|the small window and break it swiftly. Then you climb through it and find yourself in a small room   |')
    print('|with a running fireplace, a couch, and a medium sized fridge. You quickly make your way towards the  |')
    print('|fridge and open it, uncovering multiple bottles of water, and some food. You make haste and grab some|')
    print('|water and food and once you feel fully refreshed, you go over to the sofa and close your eyes...     |')
    print('|When you wake up, you see a hooded figure standing near you looking straight at you. How will you    |')
    print('|react? What will you do next?                                                                        |')
    print('└-----------------------------------------------------------------------------------------------------┘')
    print('1) Pull out your rifle and shoot the figure')
    print('2) Ask them who they are and what they want')
    print('3) Make a run for it')
    print('4) Do nothing')
    print('5) Quit game (your progress will NOT be saved)')
    try:
        print('')
        reaction_to_figure = int(input('Enter your choice: '))
    except ValueError:
        print('')
        time.sleep(1)
        print('Invalid selection! Please enter an one of the displayed integers...')
        return heading_to_shelter_choice()
# Option 1 is pulling out rifle and shooting figure
# Create function to process the possible failure of the gun and different outcomes as a result of failure
    if reaction_to_figure == 1:
        print('')
        print('You chose to try and shoot the figure')
        return shooting_figure()
# Option 2 is asking them who they are and what they want
    if reaction_to_figure == 2:
        print('')
        print('You chose to ask the figure who they are and what they want')
        print('')
        print('You ask the figure who they are and what they want. Then they respond that you had no right to')
        print('come into their home and take their resources. Based on the voice, you deduce it is a middle aged man.')
        print('Will you apologize?')
        print('')
        print('1) Sure')
        print('2) No!')
        try:
            print('')
            possible_apology = int(input('Enter your choice: '))
        except ValueError:
            print('')
            time.sleep(1)
            print('Type "1" or "2"! Not whatever you just typed...')
            return possible_apology
        if possible_apology == 1:
            print('')
            print('You chose to apologize...')
            print('')
            time.sleep(2)
            print('')
            print('You apologized to the man and he accepts it.')
            print('Then you have a long conversation with him about wanting to find your family.')
            print('The man says that there is rumored to be a safegaurded city that is free from all of the worldly')
            print('chaos... The city known as Incibo. The man offers to come with you on the journey to the city and you')
            print('graciously accept. You pack some water and food and leave the shelter with the man.')
            for x in range(7):
                character_contents.append(water)
                character_contents.append(food)
            print('')
            time.sleep(2)
            print("You have gained 6 water bottles and 6 food items")
            time.sleep(1)
            print('You currently have these items: ',', '.join(str(character_contents)))

        if possible_apology == 2:
            print('')
            print('You chose to not apologize...')
            print('')
            time.sleep(2)
            print('')
            print('I was starving and you had the resources I needed. I have no regrets...')
            print('Then the figure showed his face which you made out to be a middle aged man.')
            print('He then angrily charged at you with a knife and you lifted your rifle and shot him.')
            print('You looked in his pockets to see if he had anything useful and you found a map to a city')
            print('referred to as "Incibo". You did not have much of a plan anyways, so what the heck, you thought.')
            print('You grabbed the mans knife, and some food and water, then left the shelter to head to the city ')
            print('known as Incibo.')
            for x in range(5):
                character_contents.append(water)
                character_contents.append(food)
            character_contents.remove(rifle_bullet)
            character_contents.append(combat_knife)
            print('')
            time.sleep(2)
            print("You have gained 4 water bottles and 4 food items and Bill's knife, but lost 1 of your 3 bullets")
            time.sleep(1)
            print('You currently have these items: ',', '.join(str(character_contents)))
        else:
            print('')
            time.sleep(1)
            print('Type "1" or "2"! Not whatever you just typed...')
            return possible_apology

# Option 3 is making a run for it
    if reaction_to_figure == 3:
        time.sleep(2)
        print('')
        print('You sprint off the couch and make a run for the window.')
        print('Unfortunately, you failed... As you began to climb out the window you felt')
        print('the hand of the figure grab for your leg and pull you down to the floor')
        print('of the cabin...')
        possible_death = random.randint(1,500)
        if possible_death >= 400:
            print('The man stabbed your multiple times...')
            print('')
            time.sleep(0.5)
            print('┌--------------------------┐')
            print('|         YOU DIED         |') 
            print('└--------------------------┘')
            time.sleep(1)
            print('')
            print('Would you like to play again?')
            print('1) Yes, I want to play again!')
            print('2) No, get me out of this game!!!')
            try:
                print('')
                quit_option = int(input('Enter your choice: '))
            except ValueError:
                print('')
                time.sleep(1)
                print('Invalid selection! Please enter one of the select integers...(1 or 2)')
                return quit_option
        if quit_option == 1:
            return main()
        elif quit_option == 2:
            print('')
            time.sleep(1.5)
            print('Quitting game...')
            exit()
        else:
            print("You successfully escaped the shelter and kept running until you couldn't see the man chasing")
            print("you anymore. You then decide to head to a dam off in the distance with the hope that you can")
            print("find some supplies that could be useful...")
            print('')

# Option 4 is do nothing
    if reaction_to_figure == 4:
        print('Many moments passed and nothing happened. Then the figure, said, "I do not have time for this..."')
        print('You recognized the figures voice to be that of an older man. Then the man began to walk towards you...')
        possible_death_1 = random.randint(1,100)
        if possible_death_1 == 23 or possible_death_1 == 96:
            print('The man pulled about a combat knife and stabbed you multiple times...')
            print('')
            time.sleep(0.5)
            print('┌--------------------------┐')
            print('|         YOU DIED         |') 
            print('└--------------------------┘')
            time.sleep(1)
            print('')
            print('Would you like to play again?')
            print('1) Yes, I want to play again!')
            print('2) No, get me out of this game!!!')
            try:
                print('')
                quit_option = int(input('Enter your choice: '))
            except ValueError:
                print('')
                time.sleep(1)
                print('Invalid selection! Please enter one of the select integers...(1 or 2)')
                return quit_option
        if quit_option == 1:
            return main()
        elif quit_option == 2:
            print('')
            time.sleep(1.5)
            print('Quitting game...')
            exit()
        else:
            print('The man then said that he is desperate for supplies and knows of a nearby dam with supplies that')
            print('could prove helpful for himself and you. He then asked you if you could help him and you agreed to help.')
            print('The man said that his name was Bill. You and Bill set off for the dam about an hour later...')

# Option 5 is quit game
    elif reaction_to_figure == 5:
        print('')
        time.sleep(1)
        print('Quitting game...')
        exit()
    else:
        time.sleep(1)
        print('')
        print('You did not make a correct selection...')
        return heading_to_shelter_choice()
        
            
def shooting_figure():
    for x in range(1):
        chance_to_hit = random.randint(1,3)
    if chance_to_hit == 1:
        print('')
        time.sleep(1)
        print('You missed your shot! The figure came at you with a knife and stabbed')
        print('you multiple times...')
        print('')
        time.sleep(0.5)
        print('┌--------------------------┐')
        print('|         YOU DIED         |') 
        print('└--------------------------┘')
        time.sleep(1)
        print('')
        print('Would you like to play again?')
        print('1) Yes, I want to play again!')
        print('2) No, get me out of this game!!!')
        try:
            print('')
            quit_option = int(input('Enter your choice: '))
        except ValueError:
            print('')
            time.sleep(1)
            print('Invalid selection! Please enter one of the select integers...(1 or 2)')
            return quit_option
    if quit_option == 1:
        main()
    elif quit_option == 2:
        print('')
        time.sleep(1.5)
        print('Quitting game...')
        exit()
    elif chance_to_hit == 2:
        print('You hit your shot and the figure fell over. When you got closer to investigate')
        print('the damage, it appeared that you killed a middle aged man whom had a silver combat')
        print('knife. You soon realized that you may have invaded his shelter and there could')
        print('be others, so you must leave. You grab all the food and water you can then leave the shelter.')
        for x in range(4):
            character_contents.append(water)
            character_contents.append(food)
        character_contents.remove(rifle_bullet)
        print('')
        time.sleep(2)
        print('You have gained 3 water bottles and 3 food items, but lost 1 of your 3 bullets')
        time.sleep(1)
        print('You currently have these items: ',', '.join(str(character_contents)))

    elif chance_to_hit == 3:
        print('Your gun jammed and then the figure began to laugh. It was the laugh of a man...')
        print('He then asks you why you are in his home. ')
        print('-----------------------------------------------------------------------------------')
        print('1) Tell him that you were seeking shelter from the storm')
        print('2) Apologize and tell him you will leave immediately')
        print('3) Tell him a reason yourself')
        print('4) Quit game (your progress will NOT be saved)')
        try:
            print('')
            explanation = int(input('Enter your choice: '))
        except ValueError:
            time.sleep(1)
            print('')
            print('Invalid selection! Please enter an one of the displayed integers...')
            return shooting_figure()
        if explanation == 1:
            print('The figure accepted your explanation and responded that his name was Bill.')
            print('Bill: "What is your name?"')
            print('You: "My name is ',user_name,'".')
            print('Bill: "Its nice to meet you',user_name,' even though you took some of my food..."')
            print('Bill: "These lands are harsh. I do not blame you for what you did."')
            print('Bill: "But... I am afraid I cannot trust you. I am truly sorry for what comes next."')
            print('Then Bill lunged at you with a knife and you quickly lifted your rifle up and shot him, your heart racing...')
            print('You gather your things and as much food and water as you can store and leave the shelter.')
            for x in range(4):
                character_contents.append(water)
                character_contents.append(food)
            character_contents.remove(rifle_bullet)
            print('')
            time.sleep(2)
            print('You have gained 3 water bottles and 3 food items, but lost 1 of your 3 bullets')
            time.sleep(1)
            print('You currently have these items: ',', '.join(str(character_contents)))

        if explanation == 2:
            print('You apologized but the figure did not move a muscle. Then you heard it mumble something lightly.')
            print('It was the voice of an older man. He then much louder, replied "I understand your desperation to')
            print('take my food. But that is an unfortunate debt you must repay with your life..." Then the man came')
            print('at you with a silver combat knife. Fortunately, you had your rifle ready and quickly shot the man')
            print('before he could even reach you. You then gathered as much food and water as you could carry and')
            print('left the shelter as quickly as you could...')
            for x in range(4):
                character_contents.append(water)
                character_contents.append(food)
            character_contents.remove(rifle_bullet)
            print('')
            time.sleep(2)
            print('You have gained 3 water bottles and 3 food items, but lost 1 of your 3 bullets')
            time.sleep(1)
            print('You currently have these items: ',', '.join(str(character_contents)))

        if explanation == 3:
            print('')
            user_reason = str(input('Enter your reason: '))
            print('The figure responded quickly with a very aggressive tone. "I could give two shits what your reason was."')
            print('"You stole from me and now you must pay for it..."')
            print('Then the figure ran at you with a knife. Luckily, you had your rifle ready and you shot the figure')
            print('before it could even touch you. When you looked down at the body, you saw the face of an older middle')
            print('aged man. You then gathered your things, and as much food and water as you could carry and left')
            print('the shelter immediately...')
            for x in range(4):
                character_contents.append(water)
                character_contents.append(food)
            character_contents.remove(rifle_bullet)
            print('')
            time.sleep(2)
            print('You have gained 3 water bottles and 3 food items, but lost 1 of your 3 bullets')
            time.sleep(1)
            print('You currently have these items: ',', '.join(str(character_contents)))

        if explanation == 4:
            print('')
            time.sleep(1.5)
            print('Quitting game...')
            exit()
        else:
            time.sleep(1)
            print('')
            print('You did not make a correct selection...')
            return shooting_figure()

# Scratch.py goes right here (entire thing)
def left_choice_path():
    print('')
    print('                      ┌------------------------------------------------┐')
    print("                      |                CHOOSING TO GO LEFT             |")
    print('                      └------------------------------------------------┘')
    print('┌-----------------------------------------------------------------------------------------------------┐')
    print('| You go left towards the              |')
    print('|             |')
    print('||')
    print('|  |')
    print('|   |')
    print('||')
    print('|                                                |')
    print('|                                                                             |')
    print('└-----------------------------------------------------------------------------------------------------┘')
    print('1) Continue heading to the shelter')
    print('2) Go underneath the bridge to wait out the storm')
    print('3) Quit game (your progress will NOT be saved)')
    
main()