import random
import json
def Main():
    class Character: # Next update ideas: Add something to increase abilities, skills, etc. Also maybe sort the skills into social, physical, focus, knowledge, trade.
        def __init__(self, name, abilities, skills, tradeskills):
            self.abilities = abilities
            self.skills = skills # Future, add a way to edit the character. Maybe a basic main menu thing that is 'character roll, base roll, edit character, create character'
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
            print(f"Changing the attributes of {self.name}")
            print("Which attribute would you like to change?")
            print("1. Drive")
            print("2. Grace")
            print("3. Strength")
            print("4. Mind")
            print("5. Wit")
            print("Enter the number to select, or 0 to end")
            selection = int(input())
            if selection == 0:
                return
            abilityList = list(self.abilities.keys())
            self.abilities[abilityList[selection]] = int(input(f"Original value is {self.abilities[abilityList[selection]]}. Input new value: "))
        def EditSkills(self):
            print("Please select the skill type:")
            print("1. Physical Skills")
            print("2. Focus Skills")
            print("3. Social Skills")
            print("4. Knowledge Skills")
            print("5. Trade Skills")
            print("Enter the number to select, or 0 to end")
            selection = int(input())
            if selection == 0:
                return
            elif 1 <= selection <= 4:
                if selection == 1:
                    print("Select the Physical Skill to change: ")
                    print("1. Agility")
                    print("2. Endurance")
                    print("3. Finesse")
                    print("4. Might")
                    print("Enter the number to select, or 0 to end")
                    SkillSelect = int(input())
                    SkillSelect -= 1
                if selection == 2:
                    print("Select the Focus Skill to change: ")
                    print("1. Channeling")
                    print("2. Perception")
                    print("3. Rebellion")
                    print("4. Stealth")
                    print("Enter the number to select, or 0 to end")
                    SkillSelect = int(input())
                    SkillSelect += 3
                if selection == 3:
                    print("Select the Social Skill to change: ")
                    print("1. Boldness")
                    print("2. Coercion")
                    print("3. Manipulation")
                    print("4. Tact")
                    print("Enter the number to select, or 0 to end")
                    SkillSelect = int(input())
                    SkillSelect += 7
                if selection == 4:
                    print("Select the Knowledge Skill to change: ")
                    print("1. Lore")
                    print("2. Medicine")
                    print("3. Spirituality")
                    print("4. Wilderness")
                    print("Enter the number to select, or 0 to end")
                    SkillSelect = int(input())
                    SkillSelect += 11
                skillList = list(self.skills.keys())
                selectedSkill = skillList[SkillSelect]
                self.skills[selectedSkill] = [int(input(f"Please input the number of marks in {selectedSkill.capitalize}: ")), int(input("Please input any other modifiers: "))]
            elif selection == 5:
                print("Select the Trade Skill to change: ")
                print("1. Art")
                print("2. Cartography")
                print("3. Cooking")
                print("4. Herbalism")
                print("5. Literature")
                print("6. Lockpicking")
                print("7. Smithing")
                print("8. Tailoring")
                print("9. Tinkering")
                print("Enter the number to select, or 0 to end")
                SkillSelect = int(input())
                skillList = list(self.tradeskills.keys())
                selectedSkill = skillList[SkillSelect - 1]
                self.tradeskills[selectedSkill] = [int(input(f"Please input the number of marks in {selectedSkill.capitalize}: ")), int(input("Please input any other modifiers: "))]
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
                if i + 1 < len(ModList) and Mod in FunctionalMods and Mod in ValMods:
                    try:
                        Mods[Mod] = int(ModList[i + 1])
                    except ValueError:
                        print(f"Expected a value for modifier {Mod}.")
                        raise ValueError("Input not accepted")
                    i += 2
                elif Mod in FunctionalMods:
                    Mods[Mod] = True
                    i += 1
                elif Mod not in FunctionalMods:
                    print("Modifier not found, check syntax and retry")
                    raise ValueError("Input not accepted")
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
        def Successes(roll, Modifiers):
            successes = 0
            if "chance" in Modifiers:
                for i in roll:
                    if i >= 6:
                        successes = successes + 1
            elif "balance" in Modifiers:
                for i in roll:
                    if i >= 4:
                        successes = successes + 1
            else:
                for i in roll:
                    if i >= 5:
                        successes = successes + 1
            if "power" in Modifiers:
                for i in roll:
                    if i == 6:
                        successes = successes + 1
            if successes > 0 and "leverage" in Modifiers:
                val = Modifiers["leverage"]
                successes += val
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
                        current = Successes([die], Mods)
                        upgraded = Successes([target], Mods)
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
        try:
            Modifiers = ParseModifiers(Modifiers)
        except ValueError:
            print("Input not accepted. Try again.")
        if "reroll" in Modifiers:
            RerVal = Modifiers["reroll"]
            rer, reramt = Reroll(result, RerVal)
            result[-reramt:] = rer
        if "exploding" in Modifiers:
            ExpVal = Modifiers["exploding"]
            exp = Explode(result, ExpVal)
            result += exp
        result.sort(reverse=True)
        print("Diceroll result:", result)
        if "fudge" in Modifiers:
            FudVal = Modifiers["fudge"]
            fud = Fudge(result, FudVal, Modifiers)
            result = fud
            print("Fudge adjusted values:", result)
        successes = Successes(result, Modifiers)
        return successes

    def BaseRoller():
        print("This is the Hemlock dice roller. The instructions are simple.")
        print("Input your dicepool as an integer, then list your roll modifiers.")
        print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
        print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
        print("Enter -1 as your dicepool to end.")
        while True:
            Dicepool = int(input("Please input your dicepool: "))
            if Dicepool == -1:
                break
            Modifiers = input("Please list your modifiers: ")
            result = Roll(Dicepool, Modifiers)
            print("Number of Successes:", result)
    def CharacterRoller():
        def Menu():
            def CharRoll():
                print("Rolling: ")
                ability = input("Please enter your ability: ")
                ability.lower()
                skill = input("Please enter your skill: ")
                skill.lower()
                Dicepool = Selected.GetDicepool(ability, skill)
                plus = int(input("Please enter the amount of additional dice: "))
                Dicepool += plus
                Modifiers = input("Please enter your modifiers: ")
                Successes = Roll(Dicepool, Modifiers)
                print(f"Number of successes: {Successes}.")
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
                        Menu()
                    elif choice > len(CharacterList):
                        print("Invalid selection.")
                        Menu()
                    else:
                        return Characters[choice - 1]
                else:
                    print("Invalid selection.")
                    Menu()
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
                abilities = {
                    "drive": int(input("Input your character's Drive: ")),
                    "grace": int(input("Input your character's Grace: ")),
                    "strength": int(input("Input your character's Strength: ")),
                    "mind": int(input("Input your character's Mind: ")),
                    "wit": int(input("Input your character's Wit: ")),
                    }
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
                    "Cartography": [0, 0],
                    "Cooking": [0, 0],
                    "Herbalism": [0, 0],
                    "Literature": [0, 0],
                    "Lockpicking": [0, 0],
                    "Smithing": [0, 0],
                    "Tailoring": [0, 0],
                    "Tinkering": [0, 0]
                    }
                PlayerCharacter = Character(name, abilities, marks, tradeskills)
                NumChar = len(list(Characters.keys()))
                Characters[NumChar] = PlayerCharacter
                print("Ensure you edit the charater's abilities and skills before use.")
                return
            def SaveChar():
                print("Ensure you have a character selected and input your desired filename")
                charname = Selected.GetName()
                print(f"Your selected character is {charname}.")
                filename = input("Input your desired filename: ")
                Selected.SaveCharacter(filename)
                print("Character successfuly saved!")

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
                selection = input()
                if selection.isdigit():
                    selection = int(selection)
                else:
                    print("Invalid entry.")
                    continue
                if selection == 0:
                    break
                elif selection == 1:
                    CharRoll()
                elif selection == 2:
                    Selected = CharSelect()
                elif selection == 3:
                    print("Input 1 to edit your selected character's abilities, and input 2 to edit their skills. Input 0 to cancel.")
                    print("Ensure you have a character selected.")
                    choice = int(input())
                    if choice == 0:
                        continue
                    elif choice == 1:
                        Selected.EditAttributes()
                    elif choice == 2:
                        Selected.EditSkills()
                    else:
                        print("Invalid selection.")
                    continue
                elif selection == 4:
                    LoadChar()
                elif selection == 5:
                    CreateChar()
                elif selection == 6:
                    SaveChar()
                else:
                    print("Invalid entry.")
                    continue

        print("Welcome to the Character Roller.")
        print("Simply input the ability, skill, bonuses, and modifiers to roll with.")
        print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
        print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
        Menu()
    Characters = {}
    while True:
        print("Welcome to the Hemlock Roller. This roller has two modes: Character and Roller modes.")
        print("To open the character mode, input 1.")
        print("To open the roller mode, input 2.")
        print("To quit, input 0.")
        create = int(input())
        if create == 0:
            return
        elif create == 1:
            CharacterRoller()
        elif create == 2:
            BaseRoller()
        else:
            print("Invalid Input")

Main()
