import random
import json

class Character:
    def __init__(self, name, abilities, skills, tradeskills):
        self.abilities = abilities
        self.abilList = ["Drive", "Grace", "Strength", "Mind", "Wit"]
        self.physSkills = ["Agility", "Endurance", "Finesse", "Might"]
        self.focusSkills = ["Channeling", "Perception", "Rebellion", "Stealth"]
        self.socSkills = ["Boldness", "Coercion", "Manipulation", "Tact"]
        self.knowSkills = ["Lore", "Medicine", "Spirituality", "Wilderness"]
        self.tradeSkills = ["Art", "Cartography", "Cooking", "Herbalism", "Literature", "Lockpicking", "Smithing", "Tailoring", "Tinkering"]
        self.skills = skills
        self.tradeskills = tradeskills
        self.name = name # Maybe future add other stats, and other kinds of rolls - set up stuff for standard rolls - basic attack (allow added mods), defense (allow for dodge/defend), etc.
        self.name_modified = name.lower()
    def GetDicepool(self, ability, skill):
        ability = ability.lower()
        skill = skill.lower()
        AbilVal = self.abilities.get(ability, 0)
        SkillVal = self.skills.get(skill, 0)
        Dicepool = AbilVal + 2 * SkillVal[0] + SkillVal[1] + 1
        return Dicepool
    def EditAttributes(self):
        loop = True
        while loop:
            print(f"Changing the attributes of {self.name}")
            print("Which attribute would you like to change?")
            for i in range(len(self.abilList)):
                print(f"{i + 1}: {self.abilList[i]}")
            selection = TestInt("Enter the number to select, or 0 to end\n", 0, len(self.abilList))
            if selection == 0:
                break
            abilityList = list(self.abilities.keys())
            valprompt = f"Original value is {self.abilities[abilityList[selection]]}. Input new value: "
            value = TestInt(valprompt, 0)
            self.abilities[abilityList[selection]] = value


    def EditSkills(self):
        print("Please select the skill type:")
        print("1. Physical Skills")
        print("2. Focus Skills")
        print("3. Social Skills")
        print("4. Knowledge Skills")
        print("5. Trade Skills")
        selection = TestInt("Enter the number to select, or 0 to end", 0, 5)
        if selection == 0:
            return
        elif 1 <= selection <= 4:
            if selection == 1:
                print("Select the Physical Skill to change: ")
                for i in range(len(self.physSkills)):
                    print(f"{i + 1}: {self.physSkills[i]}")
                SkillSelect = TestInt("Enter the number to select, or 0 to end\n", 0, len(self.physSkills))
            if selection == 2:
                print("Select the Focus Skill to change: ")
                for i in range(len(self.focusSkills)):
                    print(f"{i + 1}: {self.focusSkills[i]}")
                SkillSelect = TestInt("Enter the number to select, or 0 to end\n", 0, len(self.focusSkills))
                SkillSelect += 3
            if selection == 3:
                print("Select the Social Skill to change: ")
                for i in range(len(self.socSkills)):
                    print(f"{i + 1}: {self.socSkills[i]}")
                SkillSelect = TestInt("Enter the number to select, or 0 to end\n", 0, len(self.socSkills))
                SkillSelect += 7
            if selection == 4:
                print("Select the Knowledge Skill to change: ")
                for i in range(len(self.knowSkills)):
                    print(f"{i + 1}: {self.knowSkills[i]}")
                SkillSelect = TestInt("Enter the number to select, or 0 to end\n", 0, len(self.knowSkills))
                SkillSelect += 11
            skillList = list(self.skills.keys())
            selectedSkill = skillList[SkillSelect]
            mprompt = f"Please input the number of marks in {selectedSkill.capitalize}: "
            marks = TestInt(mprompt, 0, 3)
            skillMods = TestInt("Please input any other modifiers: ")
            MarkMod = [marks, skillMods]
            self.skills[selectedSkill] = MarkMod
        elif selection == 5:
            print("Select the Trade Skill to change: ")
            for i in range(len(self.tradeSkills)):
                print(f"{i + 1}: {self.tradeSkills[i]}")
            print("Enter the number to select, or 0 to end")
            SkillSelect = TestInt("Enter the number to select, or 0 to end\n", 0, 4)
            skillList = list(self.tradeskills.keys())
            selectedSkill = skillList[SkillSelect - 1]
            mprompt = f"Please input the number of marks in {selectedSkill.capitalize}: "
            marks = TestInt(mprompt, 0, 3)
            skillMods = TestInt("Please input any other modifiers: ")
            MarkMod = [marks, skillMods]
            self.tradeskills[selectedSkill] = MarkMod
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

def TestInt(prompt, minimum=None, maximum=None):

    while True:
        value = input(prompt)

        if not value.isdigit():
            print("Please enter a valid integer:")
            continue

        value = int(value)

        if minimum is not None and value < minimum:
            print("Value is too small. Input a valid value.")
            continue

        if maximum is not None and value > maximum:
            print("Value is too large. Input a valid value.")
            continue

        return value

def MainMenu():
    print("To open the character mode, input 1.")
    print("To open the roller mode, input 2.")
    print("To quit, input 0.")
    create = TestInt("", 0, 2)
    if create == 0:
        return False
    elif create == 1:
        CharacterRoller()
    elif create == 2:
        BaseRoller()

def Roll(Dicepool, Modifiers):
    def ParseModifiers(Modifiers):
        Modifiers = Modifiers.lower().replace(",", "")
        ModList = Modifiers.split()

        Mods = {}
        i = 0
        FunctionalMods = ["power", "balance", "chance", "leverage", "reroll", "fudge", "exploding"]
        ValMods = ["leverage", "reroll", "fudge", "exploding"]

        while i < len(ModList):
            Mod = ModList[i]
            if Mod in ValMods:
                if i + 1 > len(ModList):
                    raise ValueError(f"Expected a value for modifier {Mod}.")
                try:
                    Mods[Mod] = int(ModList[i + 1])
                except ValueError:
                    raise ValueError(f"Expected a value for modifier {Mod}.")
                i += 2
            elif Mod in FunctionalMods:
                Mods[Mod] = True
                i += 1
            elif Mod not in FunctionalMods:
                raise ValueError("Valid modifier not found.")

        return Mods
    def RollStart(amount):
        rollresult = []
        for i in range(amount):
            rollresult.append(random.randint(1, 6))
        rollresult.sort(reverse=True)
        return rollresult
    def Explode(roll, val):
        explode = 1
        exploderesult = []
        exploderoll = roll

        while explode:
            explode = 0
            for i in exploderoll:
                if i >= val:
                    explode = explode + 1
            exploderoll = RollStart(explode)
            for i in exploderoll:
                exploderesult.append(i)

        return exploderesult
    def Reroll(Roll, val):
        rerollresult = []
        Roll.sort(reverse=True)
        rerollpool = 0
        for i in Roll:
            if i <= val:
                rerollpool += 1
        rerollresult = RollStart(rerollpool)

        return rerollresult, rerollpool
    def TestSuccess(die, Modifiers):
        successes = 0
        if "chance" in Modifiers:
            if die >= 6:
                    successes = successes + 1
        elif "balance" in Modifiers:
            if die >= 4:
                    successes = successes + 1
        else:
            if die >= 5:
                    successes = successes + 1
        if "power" in Modifiers:
            if die == 6:
                    successes = successes + 1

        return successes
    def Fudge(roll, val, Mods):
        dice = roll[:]
        while val > 0:
            BestEff = -1
            BestIndex = None
            BestCost = 0
            BestTarget = None

            for i, die in enumerate(dice):
                for target in range(die + 1, 7):
                    cost = target - die
                    if cost > val:
                        continue
                    current = TestSuccess(die, Mods)
                    upgraded = TestSuccess(target, Mods)
                    gain = upgraded - current

                    if gain <= 0:
                        continue

                    efficiency = gain/cost

                    if efficiency > BestEff:
                        BestEff = efficiency
                        BestIndex = i
                        BestCost = cost
                        BestTarget = target
            if BestIndex is None:
                break
            dice[BestIndex] = BestTarget
            val -= BestCost
        return dice
    while Dicepool > 36 or Dicepool < 0:
        print("Invalid dicepool.")
        return
    result = RollStart(Dicepool)
    Modifiers = ParseModifiers(Modifiers)
    final = {}
    final["Roll"] = result
    if "reroll" in Modifiers:
        RerVal = Modifiers["reroll"]
        rer, reramt = Reroll(result, RerVal)
        result[-reramt:] = rer
        final["Roll"] = result
    if "exploding" in Modifiers:
        ExpVal = Modifiers["exploding"]
        exp = Explode(result, ExpVal)
        result += exp
        final["Roll"] = result
    result.sort(reverse=True)
    if "fudge" in Modifiers:
        FudVal = Modifiers["fudge"]
        fud = Fudge(result, FudVal, Modifiers)
        final["Fudge"] = fud
        result = fud
    successes = 0
    for i in result:
        successes += TestSuccess(i, Modifiers)
    if successes > 0 and "leverage" in Modifiers:
        val = Modifiers["leverage"]
        successes += val
    final["Successes"] = successes
    return final

def BaseRoller():
    print("This is the Hemlock dice roller. The instructions are simple.")
    print("Input your dicepool as an integer, then list your roll modifiers.")
    print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
    print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
    print("Enter 0 as your dicepool to end.")
    while True:
        prompt = "Please input your dicepool: "
        Dicepool = TestInt(prompt, 0, 36)
        if Dicepool == 0:
            break
        Modifiers = input("Please list your modifiers: ")
        try:
            result = Roll(Dicepool, Modifiers)
        except ValueError:
            print("Input not accepted. Try again")
            continue
        rollresult = result["Roll"]
        print("Roll result:", rollresult)
        if "Fudge" in result:
            print("Fudge adjusted values:", result["Fudge"])
        print("Number of Successes:", result["Successes"])
def CharacterRoller():
    def CharRoll(Selected):
        print("Rolling: ")
        ability = input("Please enter your ability: ")
        skill = input("Please enter your skill: ")
        Dicepool = Selected.GetDicepool(ability, skill)
        prompt = "Please enter the amount of additional dice: "
        plus = TestInt(prompt)
        Dicepool += plus
        if Dicepool > 36:
            Dicepool = 36
        Modifiers = input("Please enter your modifiers: ")
        try:
            result = Roll(Dicepool, Modifiers)
        except ValueError:
            print("Input not accepted.")
            return
        print("Roll result:", result["Roll"])
        if "Fudge" in result:
            print("Fudge adjusted values:", result["Fudge"])
        print("Number of Successes:", result["Successes"])
    def CharSelect():
        print("Current Characters: ")
        CharacterIndex = list(Characters.keys())
        CharacterList = []
        if len(CharacterIndex) == 0:
            print("No characters in Index.")
            return
        for i in CharacterIndex:
            CharacterList.append(Characters[i].GetName())
        for i in range(len(CharacterList)):
            print(f"{i + 1}: {CharacterList[i]}")
        print("Input a number to select the corresponding character. Input 0 to quit")
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                return None
            elif choice > len(CharacterList):
                print("Invalid selection.")
                return None
            else:
                selectedchar = CharacterIndex[choice - 1]
                return Characters[selectedchar]
        else:
            print("Invalid selection.")
            return None
    def LoadChar():
        print("Input the filename of your character file: ")
        print("Do not include the filetype")
        filename = input()
        with open(f'{filename}.txt', 'r') as file:
            Retrieved = json.load(file)
        if Retrieved["Is a valid sheet"]:
            name = Retrieved["name"]
            abilities = Retrieved["abilities"]
            skills = Retrieved ["skills"]
            tradeskills = Retrieved["trade skills"]
            PlayerCharacter = Character(name, abilities, skills, tradeskills)
            NumChar = len(list(Characters.keys()))
            Characters[NumChar] = PlayerCharacter
        else:
            print("Selected file is not a valid character.")
    def CreateChar():
        print("Please create your character.")
        name = input("Please input your character's name: ")
        abilList = ["Drive", "Grace", "Strength", "Mind", "Wit"]
        abilities = {}
        for i in range(len(abilList)):
            j = abilList[i]
            k = j.lower()
            prompt = f"Input your character's {j}: "
            val = TestInt(prompt, 0)
            abilities[k] = val
        marks = {
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
        tradeskills = {
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
        PlayerCharacter = Character(name, abilities, marks, tradeskills)
        NumChar = len(list(Characters.keys()))
        Characters[NumChar] = PlayerCharacter
        print("Ensure you edit the charater's abilities and skills before use.")
        return
    def SaveChar(Selected):
        print("Ensure you have a character selected and input your desired filename")
        charname = Selected.GetName()
        print(f"Your selected character is {charname}.")
        filename = input("Input your desired filename: ")
        Selected.SaveCharacter(filename)
        print("Character successfuly saved!")
    def Menu():
        Selected = None
        while True:
            print("Select one of the following:")
            print("1. Roll")
            print("2. Select Character")
            print("3. Edit Character")
            print("4. Load Character")
            print("5. Create Character")
            print("6. Save Character to Device")
            print("Enter a number to select. Enter 0 to quit")
            print("Ensure you have a character selected before choosing \"Roll\"")
            selection = TestInt("", 0, 6)
            if selection == 0:
                break
            elif selection == 1 and Selected != None:
                CharRoll(Selected)
            elif selection == 2:
                Selected = CharSelect()
            elif selection == 3 and Selected != None:
                print("Input 1 to edit your selected character's abilities, and input 2 to edit their skills. Input 0 to cancel.")
                print("Ensure you have a character selected.")
                choice = TestInt("", 0, 2)
                if choice == 0:
                    continue
                elif choice == 1:
                    Selected.EditAttributes()
                elif choice == 2:
                    Selected.EditSkills()
                continue
            elif selection == 4:
                LoadChar()
            elif selection == 5:
                CreateChar()
            elif selection == 6 and Selected != None:
                SaveChar(Selected)

    print("Welcome to the Character Roller.")
    print("Simply input the ability, skill, bonuses, and modifiers to roll with.")
    print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
    print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
    Menu()
Characters = {}
print("Welcome to the Hemlock Roller.")
_exit = True
while _exit:
    _exit = MainMenu()
