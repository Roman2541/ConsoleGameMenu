import os  # Both used solely for file I/O
import csv #
from character import *

def add_character(): 
    character = Character(user_name(), user_role(), user_wealth(), user_race(), user_skill()) # Instantiating a character based on user input
    if character.get_role() == "warrior":
        character = Warrior(character, user_weapon(), user_armour()) # 
    elif character.get_role() == "mage":                             # Based on role of character converts them to the correct subclass using Inheritance
        character = Mage(character, user_spell(), user_mana())       #
    characters.append(character) # Adds new character to global array

def list_characters():
    count = 0
    for character in characters: # Iterating through global array
        count += 1
        print(str(count) + ". " + character.get_name()) # e.g. "1. Name"
    if count == 0:
        print("No Characters found.")

def search_character_by_name():
    search_term = "" # Defining variable in outer scope for use later on
    while True:
        search_term = input("Please Enter an alphanumerical username with 16 or less characters: ").lower()
        if search_term.isalnum() and len(search_term) <= 16: 
            break
    for character in characters:
        if character.get_name() == search_term:
             character.print_details() # Details are printed when a name matching the search term is found
             return
    print("Character does not Exist.")

def display_total_wealth():
    total_wealth = 0
    for character in characters:
        total_wealth += int(character.get_wealth())
    print("Total Wealth:", total_wealth)

def save_to_file():
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'w', newline = '') as csvfile: # Opens file from absolute path with write permissions and is assigned to csvfile
        writer = csv.writer(csvfile, delimiter = ',') # Initates csv.writer
        for character in characters:
            writer.writerow([character.get_name()]   + 
                            [character.get_role()]   + 
                            [character.get_wealth()] + 
                            [character.get_race()]   + 
                            [character.get_skill()]  + 
                            [character.get_extra1()] + # Dynamically gets extra members based on whether role is warrior or mage
                            [character.get_extra2()])  #

def load_from_file():
    characters.clear()
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'r', newline = '') as csvfile: # Opens the file with read permissions instead of write
        reader = csv.reader(csvfile, delimiter = ',') # Initates csv.reader
        for row in reader:
            character = Character(row[0], row[1], row[2], row[3], row[4]) # Instantiating character based on the attributes stored in the csvfile
            if character.get_role() == "warrior":                         
                characters.append(Warrior(character, row[5], row[6])) # 
            elif character.get_role() == "mage":                       # Converting character to the correct subclass and assigning the additional class specific attributes
                characters.append(Mage(character, row[5], row[6]))    #
        
def main_menu():
    choice = 0
    while True:
        try:
            choice = int(input("\n1 - Add a Character\n" +
                               "2 - List all Characters\n" +
                               "3 - Search for Characters by Name\n" +
                               "4 - Total Wealth of all the Characters\n" +
                               "5 - Save Characters to a File\n" +
                               "6 - Load Characters from a File\n" +
                               "0 - Exit Application\n" +
                               "Please Enter Your Choice: "))
            if choice >= 0 and choice <= 6:
                break
        except:
            pass

    match choice:
        case 0: exit()
        case 1: add_character()
        case 2: list_characters() 
        case 3: search_character_by_name() 
        case 4: display_total_wealth()
        case 5: save_to_file()
        case 6: load_from_file()
        case _: exit() # If somehow no other cases are hit exit is the default action