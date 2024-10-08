characters = []

class Character:
    def __init__(self, name, role, wealth, race, skill): # Constructor for Character class
        self.name = name
        self.role = role
        self.wealth = wealth
        self.race = race
        self.skill = skill

    def get_name(self):
        return self.name
    def get_role(self):
        return self.role
    def get_wealth(self):
        return self.wealth
    def get_race(self):
        return self.race
    def get_skill(self):
        return self.skill
    def get_extra1(self): 
        return
    def get_extra2(self):
        return
    
    def set_name(self, name): 
        self.name = name
    def set_role(self, role): 
        self.role = role
    def set_wealth(self, wealth): 
        self.wealth = wealth
    def set_race(self, race): 
        self.race = race
    def set_skill(self, skill): 
        self.skill = skill
    def get_extra1(self, extra1):
        pass
    def get_extra2(self, extra2):
        pass

    def print_details(self): 
        print("Character Name: " + self.name)
        print("Character Role: " + self.role)
        print("Character Wealth: " + self.wealth)
        print("Character Race: " + self.race)
        print("Character Skill: " + self.skill)

class Warrior(Character): # Inherits from class Character
    def __init__(self, character, weapon, armour):
        super().__init__(character.name, character.role, character.wealth, character.race, character.skill) # Calls Character constructor first
        self.weapon = weapon
        self.armour = armour

    def get_extra1(self):
        return self.weapon
    def get_extra2(self):
        return self.armour
    
    def set_extra1(self, weapon): 
        self.weapon = weapon
    def set_extra2(self, armour): 
        self.armour = armour

    def print_details(self):
        super().print_details() # Calls print details function of parent class
        print("Character Weapon: " + self.weapon)
        print("Character Armour: " + self.armour)

class Mage(Character):
    def __init__(self, character, spell, mana):
        super().__init__(character.name, character.role, character.wealth, character.race, character.skill)
        self.spell = spell
        self.mana = mana

    def get_extra1(self):
        return self.spell
    def get_extra2(self):
        return self.mana
    
    def set_extra1(self, spell): 
        self.spell = spell
    def set_extra2(self, mana): 
        self.mana = mana

    def print_details(self): 
        super().print_details()
        print("Character Spell: " + self.spell)
        print("Character Mana: " + self.mana)

#Shared attribute functions
def user_name():
    while True:
        name = input("Please Enter an alphanumerical username with 16 or less characters: ")
        is_duplicate = False
        for character in characters: # Iteration through the array is necessary to ensure no duplicates
            if character.get_name() == name:
                is_duplicate = True
        if name.isalnum() and len(name) <= 16 and not is_duplicate: 
            return name
def user_role():
    while True:
        role = input("Please Enter your Role (Warrior / Mage): ").lower()
        if role == "warrior" or role == "mage":
            return role
def user_wealth():
    while True:
        try:
            wealth = int(input("Please Enter a Wealth greater than or equal to 0: "))
            if wealth >= 0:
                return str(wealth) # Converting the return to a string so it can be used more easily to print
        except:
            pass
def user_race():
    while True:
        race = input("Please Enter your Race (Human / Dwarf / Elf): ").lower()
        if race == "human" or race == "dwarf" or race == "elf":
            return race
def user_skill():
    while True:
        try:
            skill = int(input("Please Enter your Skill Level (1 - 5): "))
            if skill > 0 and skill < 6:
                return str(skill)
        except:
            pass

# Role based functions 
def user_weapon():
    while True:
        weapon = input("Please Select your Weapon (Sword / Axe) ").lower()
        if weapon == "sword" or weapon == "axe":
            return weapon
def user_armour():
    while True:
        armour = input("Please Select your Weapon (Chainmail / Plate) ").lower()
        if armour == "chainmail" or armour == "plate":
            return armour
def user_spell():
    while True:
        spell = input("Please Select your Weapon (Fireball / Lightning) ").lower()
        if spell == "fireball" or spell == "lightning":
            return spell
def user_mana():
    while True:
        try:
            mana = int(input("Please Enter your Mana Points (0 - 100): "))
            if mana >= 0 and mana <= 100:
                return str(mana)
        except:
            pass