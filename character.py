characters = []

class Character:
    def __init__(self, name, role, wealth, race, skill): # Constructor for Character class
        self.name = name
        self.role = role
        self.wealth = wealth
        self.race = race
        self.skill = skill

    def getName(self):
        return self.name
    def getRole(self):
        return self.role
    def getWealth(self):
        return self.wealth
    def getRace(self):
        return self.race
    def getSkill(self):
        return self.skill
    def getExtra1(self): 
        return
    def getExtra2(self):
        return
    
    def setName(self, name): 
        self.name = name
    def setRole(self, role): 
        self.role = role
    def setWealth(self, wealth): 
        self.wealth = wealth
    def setRace(self, race): 
        self.race = race
    def setSkill(self, skill): 
        self.skill = skill
    def getExtra1(self, extra1):
        pass
    def getExtra2(self, extra2):
        pass

    def printDetails(self): 
        print("Character Name: " + self.name)
        print("Character Role: " + self.role)
        print("Character Wealth: " + self.wealth)
        print("Character Race: " + self.race)
        print("Character Skill: " + self.skill)

class Warrior(Character): # Inherits from class Character
    def __init__(self, character, weapon, armour):
        super().__init__(character.name, character.role, character.wealth, character.race, character.skill) # Calls Character constructor first gg
        self.weapon = weapon
        self.armour = armour

    def getExtra1(self):
        return self.weapon
    def getExtra2(self):
        return self.armour
    
    def setExtra1(self, weapon): 
        self.weapon = weapon
    def setExtra2(self, armour): 
        self.armour = armour

    def printDetails(self):
        super().printDetails() # Calls print details function of parent class
        print("Character Weapon: " + self.weapon)
        print("Character Armour: " + self.armour)

class Mage(Character):
    def __init__(self, character, spell, mana):
        super().__init__(character.name, character.role, character.wealth, character.race, character.skill)
        self.spell = spell
        self.mana = mana

    def getExtra1(self):
        return self.spell
    def getExtra2(self):
        return self.mana
    
    def setExtra1(self, spell): 
        self.spell = spell
    def setExtra2(self, mana): 
        self.mana = mana

    def printDetails(self): 
        super().printDetails()
        print("Character Spell: " + self.spell)
        print("Character Mana: " + self.mana)

#Shared attribute functions
def userName():
    while True:
        name = input("Please Enter an alphanumerical username with 16 or less characters: ")
        isDuplicate = False
        for character in characters: # Iteration through the array is necessary to ensure no duplicates
            if character.getName() == name:
                isDuplicate = True
        if name.isalnum() and len(name) <= 16 and not isDuplicate: 
            return name
def userRole():
    while True:
        role = input("Please Enter your Role (Warrior / Mage): ").lower()
        if role == "warrior" or role == "mage":
            return role
def userWealth():
    while True:
        try:
            wealth = int(input("Please Enter a Wealth greater than or equal to 0: "))
            if wealth >= 0:
                return str(wealth) # Converting the return to a string so it can be used more easily to print
        except:
            pass
def userRace():
    while True:
        race = input("Please Enter your Race (Human / Dwarf / Elf): ").lower()
        if race == "human" or race == "dwarf" or race == "elf":
            return race
def userSkill():
    while True:
        try:
            skill = int(input("Please Enter your Skill Level (1 - 5): "))
            if skill > 0 and skill < 6:
                return str(skill)
        except:
            pass

# Role based functions 
def userWeapon():
    while True:
        weapon = input("Please Select your Weapon (Sword / Axe) ").lower()
        if weapon == "sword" or weapon == "axe":
            return weapon
def userArmour():
    while True:
        armour = input("Please Select your Weapon (Chainmail / Plate) ").lower()
        if armour == "chainmail" or armour == "plate":
            return armour
def userSpell():
    while True:
        spell = input("Please Select your Weapon (Fireball / Lightning) ").lower()
        if spell == "fireball" or spell == "lightning":
            return spell
def userMana():
    while True:
        try:
            mana = int(input("Please Enter your Mana Points (0 - 100): "))
            if mana >= 0 and mana <= 100:
                return str(mana)
        except:
            pass