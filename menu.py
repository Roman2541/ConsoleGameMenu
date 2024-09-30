import os  # Both used solely for file I/O
import csv #
from character import *

def addCharacter(): 
    character = Character(userName(), userRole(), userWealth(), userRace(), userSkill()) # Instantiating a character based on user input
    if character.getRole() == "warrior":
        character = Warrior(character, userWeapon(), userArmour()) # 
    elif character.getRole() == "mage":                            # Based on role of character converts them to the correct subclass using Inheritance
        character = Mage(character, userSpell(), userMana())       #
    characters.append(character) # Adds new character to global array

def listCharacters():
    count = 0
    for character in characters: # Iterating through global array
        count += 1
        print(str(count) + ". " + character.getName()) # e.g. "1. Name"
    if count == 0:
        print("No Characters found.")

def searchCharacterByName():
    searchTerm = "" # Defining variable in outer scope for use later on
    while True:
        searchTerm = input("Please Enter an alphanumerical username with 16 or less characters: ")
        if searchTerm.isalnum() and len(searchTerm) <= 16: 
            break
    for character in characters:
        if character.getName() == searchTerm:
             character.printDetails() # Details are printed when a name matching the search term is found
             return
    print("Character does not Exist.")

def displayTotalWealth():
    totalWealth = 0
    for character in characters:
        totalWealth += int(character.getWealth())
    print("Total Wealth:", totalWealth)

def saveToFile():
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'w', newline = '') as csvfile: # Opens file from absolute path with write permissions and is assigned to csvfile
        writer = csv.writer(csvfile, delimiter = ',') # Initates csv.writer
        for character in characters:
            writer.writerow([character.getName()]   + 
                            [character.getRole()]   + 
                            [character.getWealth()] + 
                            [character.getRace()]   + 
                            [character.getSkill()]  + 
                            [character.getExtra1()] + # Dynamically gets extra members based on whether role is warrior or mage
                            [character.getExtra2()])  #

def loadFromFile():
    newCharacters = [] 
    with open(os.path.join(os.path.dirname(__file__), "characters.csv"), 'r', newline = '') as csvfile: # Opens the file with read permissions instead of write
        reader = csv.reader(csvfile, delimiter = ',') # Initates csv.reader
        for row in reader:
            character = Character(row[0], row[1], row[2], row[3], row[4]) # Instantiating character based on the attributes stored in the csvfile
            if character.getRole() == "warrior":                         
                newCharacters.append(Warrior(character, row[5], row[6])) # 
            elif character.getRole() == "mage":                          # Converting character to the correct subclass and assigning the additional class specific attributes
                newCharacters.append(Mage(character, row[5], row[6]))    #
    characters.clear()
    for character in newCharacters: # After clearing characters array repopulates it with the characters from the file
        characters.append(character)
        
def mainMenu():
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
        case 1: addCharacter()
        case 2: listCharacters() 
        case 3: searchCharacterByName() 
        case 4: displayTotalWealth()
        case 5: saveToFile()
        case 6: loadFromFile()
        case _: exit() # If somehow no other cases are hit exit is the default action