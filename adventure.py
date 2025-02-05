import time
import random

def bag():
    bag = ["Bottlecap", "Peanuts", "Piece of String"]

def print_paws(message):
    print(message)
    time.sleep(1.5)

def random_item():
    item = random.choice(bag)
    bag.remove(item)

def nutkin():
    print_paws("You see your reflection looking back at you, \nbright-eyed"
               " and bushy-tailed.")

def jay():
    print_paws("A clever Jay greets you with a raucous squawk, \n"
               "a mischevious glint in his eye.\n"
               "When you glace away, he picks the knot on your bag\n"
               "and steals an item!\n")
    random_item()

def dirty_rat():
    print_paws("The Dirty Rat glares at you from his hate-filled \n"
               "beady eyes...the stench of stolen Food on his breath.\n"
               "You have found him!  The one who starves the Little Ones.\n"
               "You have one chance to defeat him - or face defeat yourself!\n")

def bunnykin():
    print_paws("A soft brown Bunnykin looks at you with peace in her eyes.\n"
               "She shyly hands you a Chocolate Chip Cookie.\n"
               "I made them myself! she sqeaks.\n")
    bag.append("Chocolate Chip Cookie")

def raven():
    print_paws("A black Raven swoops majestically down in front of you, wisdom in her eyes.\n"
               "She croaks a greeting in her ancient tongue and gives you a Glass Marble.\n")
    bag.append("Glass Marble")

def kind_boy():
    print_paws("A Kind Boy walks by, trying not to step on you.  You bumble across\n"
               "his shoe with a squeak.\n"
               "Starled, he cries out!  When he sees it's his friend Nutkin,\n"
               "he smiles and hands you a warm slice of bread!\n")
    bag.append("Warm Slice of Bread")

def guard_cat():
    print_paws("The old Guard Cat watches you lazily, swishing her fuzzy tail.\n"
               "She fishes out with a paw, trapping you until you give her\n"
               "something from your bag.\n")
random_item()

def yard():
    print_paws("You dash into the Yard, scattering leaves as you go.\n")

def house():
    print_paws("You sneak in to the House through a crack beside the chimney.\n")

def under_deck():
    print_paws("You scurry under the Deck, trying not to trip on all the cut wood.\n")

def swift_creek():
    print_paws("You carefully creep to the edge of the Swift Creek.\n")

def trees():
    print_paws("You deftly take to the Trees, your home and native land.\n")

def areas():
    print("1. The Trees\n2. Under the Deck\n3. The House\n4. The Swift Creek"
               "\n5. the Yard\n")


def intro():
    print_paws("You are a fearless squirrel, Defender of the Realm of the Trees.")
    print_paws("Nutkin is your name...the seventh of the Nutkin line.")
    print_paws("A breeze rustles the leaves which adorn the grassy patch.")
    print_paws("The Good Lady sends Food down from above, and you must collect it.")
    print_paws("But there are Others after the Food...")
    print_paws("Your mission is to search the Drinkwater Grounds, ")
    print_paws("find, and destroy,")
    print_paws("the Dirty Rat, Usurper of the Food.")
    print_paws("Begin your search...")

def choose_area():
    areas()
    area_choice = input("Where will you go next, brave Nutkin?\n"
                        "Enter a number from 1 to 5...\n\n")
    if area_choice == "1":
        trees()
    elif area_choice == "2":
        under_deck()
    elif area_choice == "3":
        house()
    elif area_choice == "4":
        swift_creek()
    elif area_choice == "5":
        yard()             

def encountered():
    characters = [jay, bunnykin, raven, kind_boy, guard_cat, dirty_rat]
    character = random.choice(characters)
    if character == jay:
        jay()
    if character == bunnykin:
        bunnykin()
    if character == raven:
        raven()
    if character == kind_boy:
        kind_boy()
    if character == guard_cat:
        guard_cat()
    if character == dirty_rat:
        dirty_rat()

def game_play():
    intro()
    choose_area()
    encountered()

while True:
    game_play()
    again = input("Do you want to play again?   Y/N\n\n").lower()
    if again == "n":
        break
