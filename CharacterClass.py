import json
from Menus import SkillMenu, AbilityMenu

class Character: 
    def __init__(self, name, abilities=None, skills=None, tradeskills=None):
        if abilities == None:
            self.abilities = {
                "drive": 1,
                "grace": 1,
                "strength": 1,
                "mind": 1,
                "wit": 1
                }
        else:
            self.abilities = abilities
        if skills == None:
            self.skills = {
                "agility": [0, 0],
                "endurance": [0, 0],
                "finesse": [0, 0],
                "might": [0, 0],
                "channeling": [0, 0],
                "perception": [0, 0],
                "rebellion": [0, 0],
                "stealth": [0, 0],
                "boldness": [0, 0],
                "coercion": [0, 0],
                "manipulation": [0, 0],
                "tact": [0, 0],
                "lore": [0, 0],
                "medicine": [0, 0],
                "spirituality": [0, 0],
                "wilderness": [0, 0]
                }
        else:
             self.skills = skills
        if tradeskills == None:
            self.tradeskills = {
                "art": [0, 0],
                "cartography": [0, 0],
                "cooking": [0, 0],
                "herbalism": [0, 0],
                "literature": [0, 0],
                "lockpicking": [0, 0],
                "smithing": [0, 0],
                "tailoring": [0, 0],
                "tinkering": [0, 0]
                }
        else:
            self.tradeskills = tradeskills
        self.name = name # Maybe future add other stats, and other kinds of rolls - set up stuff for standard rolls - basic attack (allow added mods), defense (allow for dodge/defend), etc.
        self.name_modified = name.lower()
    
    def display(self):
        abilities = list(self.abilities.keys())
        print("Character:", self.name)
        for i in abilities:
            print(f"{i}: {self.abilities[i]}")
        skills = list(self.skills.keys())
        for i in skills:
            print(f"{i}: {self.skills[i]}")
        tradeskills = list(self.tradeskills.keys())
        for i in tradeskills:
            print(f"{i}: {self.tradeskills[i]}")

    def GetDicepool(self, ability, skill):
        ability = ability.lower()
        skill = skill.lower()
        if ability not in self.abilities:
            abilVal = 0
        else:
            abilVal = self.abilities[ability]
        if skill in self.skills:
            skillVal = self.skills[skill]
            Dicepool = skillVal[0] * 2 + skillVal[1] + abilVal
        elif skill in self.tradeskills:
            skillVal = self.tradeskills[skill]
            if skillVal[0] == 0:
                Dicepool = abilVal + skillVal[1]
            else:
                Dicepool = abilVal + skillVal[0] * 2 + skillVal[1]
        return Dicepool

    def EditAbilities(self):
        while True:
            value = AbilityMenu(self.name)
            if value == None:
                break
            self.abilities[value[0].lower()] = value[1]

    def EditSkills(self):
        while True:
            selection = SkillMenu(self.name)
            if selection == None:
                break
            selectedskill = selection[0].lower()
            if selectedskill in self.skills:
                self.skills[selectedskill] = [selection[1], selection[2]]
            elif selectedskill in self.tradeskills:
                self.tradeskills[selectedskill] = [selection[1], selection[2]]

    def GetName(self):
        return self.name

    def SaveCharacter(self, filename):
        with open(f'{filename}.txt', 'w') as file:
            data = {
                "name": self.name,
                "abilities": self.abilities,
                "skills": self.skills,
                "trade skills": self.tradeskills,
                "Is a valid sheet": True
                }
            json.dump(data, file)