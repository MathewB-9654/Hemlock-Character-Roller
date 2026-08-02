import random
def Hemlock():
    class Character: # Next update ideas: Add something to increase abilities, skills, etc. Also maybe sort the skills into social, physical, focus, knowledge, trade.
        def __init__(self, name, abilities, marks):
            self.abilities = abilities
            self.marks = marks # Future, add a way to edit the character. Maybe a basic main menu thing that is 'character roll, base roll, edit character, create character'
            self.name = name # Maybe future add other stats, and other kinds of rolls - set up stuff for standard rolls - basic attack (allow added mods), defense (allow for dodge/defend), etc.
            self.name_modified = name.lower()
        def GetDicepool(self, ability, skill):
            ability = ability.lower()
            skill = skill.lower()
            AbilVal = self.abilities.get(ability, 0)
            SkillVal = self.marks.get(skill, 0)
            Dicepool = AbilVal + 2 * SkillVal[0] + SkillVal[1] + 1
            return Dicepool
    def Roll(Dicepool, Modifiers):
        def RollStart(amount):
            rollresult = []
            for i in range(amount):
                rollresult.append(random.randint(1, 6))
            return rollresult
        def Explode(exploding):
            val = int(Modifiers[Modifiers.find("exploding") + 10])
            explode = 0
            explodetimes = 0
            exploderesult = []
            for i in exploding:
                if i >= val:
                    explode = explode + 1
            explode1 = Roll(explode)
            exploderesult.append(explode1)
            while explode > 0 and explodetimes <= len(exploderesult):
                explode = 0
                for i in exploderesult[explodetimes]:
                    if i >= val:
                        explode = explode + 1
                exploderesult.append(Roll(explode))
                explodetimes = explodetimes + 1
            exploderesult = [item for sublist in exploderesult for item in sublist]
            return exploderesult
        def Reroll():
            rerollresult = []
            rerollpool = 0
            for i in result:
                if i <= int(Modifiers[Modifiers.find("reroll") + 7]):
                    result.pop(result.index(i)) # bad idea to pop rerolls like this.
                    rerollpool = rerollpool + 1
            rerollresult = Roll(rerollpool)
            if Modifiers.find("exploding") >= 0:
                rerexp = Explode(rerollresult)
                for i in rerexp:
                    rerollresult.append(i)
            return rerollresult
        def Successes():
            successes = 0
            if Modifiers.find("chance") >= 0:
                for i in result:
                    if i >= 6:
                        successes = successes + 1
            elif Modifiers.find("balance") >= 0:
                for i in result:
                    if i >= 4:
                        successes = successes + 1
            else:
                for i in result:
                    if i >= 5:
                        successes = successes + 1
            if Modifiers.find("power") >= 0:
                for i in result:
                    if i == 6:
                        successes = successes + 1
            if successes > 0 and Modifiers.find("leverage") >= 0:
                ModList = [word for word in Modifiers.split()]
                for i in ModList:
                    if i.find("leverage") >= 0:
                        if ModList[ModList.index("leverage") + 1].isdigit() == False:
                            val = int(ModList[ModList.index("leverage") + 1][:-1])
                        else:
                            val = int(ModList[ModList.index("leverage") + 1])
                successes = successes + val
            return successes
        def Fudge():
            ModList = [word for word in Modifiers.split()]
            for i in ModList:
                if i.find("fudge") >= 0:
                    if ModList[ModList.index("fudge") + 1].isdigit() == False:
                        val = int(ModList[ModList.index("fudge") + 1][:-1])
                    else:
                        val = int(ModList[ModList.index("fudge") + 1])
            fudge = result
            if Modifiers.find("chance") >= 0:
                for i in fudge:
                    if i == 5:
                        fudge[fudge.index(i)] = 6
                        val = val - 1
                        if val == 0:
                            break
            elif Modifiers.find("balance") >= 0:
                for i in fudge:
                    if i == 3:
                        fudge[fudge.index(i)] = 4
                        val = val - 1
                        if val == 0:
                            break
            else:
                for i in fudge:
                    if i == 4:
                        fudge[fudge.index(i)] = 5
                        val = val - 1
                        if val == 0:
                            break
            if Modifiers.find("power") >= 0 and val != 0:
                for i in fudge:
                    if i == 5:
                        fudge[fudge.index(i)] = 6
                        val = val - 1
                        if val == 0:
                            break
            if Modifiers.find("chance") >= 0 and val >=2:
                for i in fudge:
                    if i == 4 and val >= 2:
                        fudge[fudge.index(i)] = 6
                        val = val - 2
                        if val == 0:
                            break
            elif Modifiers.find("balance") >= 0 and val >= 2:
                for i in fudge:
                    if i == 2 and val >= 2:
                        fudge[fudge.index(i)] = 4
                        val = val - 2
                        if val == 0:
                            break
            else:
                for i in fudge:
                    if i == 3 and val >= 2:
                        fudge[fudge.index(i)] = 5
                        val = val - 2
                        if val == 0:
                            break
            if Modifiers.find("power") >= 0 and val >= 2:
                for i in fudge:
                    if i == 4:
                        fudge[fudge.index(i)] = 6
                        val = val - 2
                        if val == 0:
                            break
            if Modifiers.find("chance") >= 0 and val >= 3:
                for i in fudge:
                    if i == 3 and val >= 3:
                        fudge[fudge.index(i)] = 6
                        val = val - 3
                        if val == 0:
                            break
            elif Modifiers.find("balance") >= 0 and val >= 3:
                for i in fudge:
                    if i == 1 and val >= 3:
                        fudge[fudge.index(i)] = 4
                        val = val - 3
                        if val == 0:
                            break
            else:
                for i in fudge:
                    if i == 2 and val >= 3:
                        fudge[fudge.index(i)] = 5
                        val = val - 3
                        if val == 0:
                            break
            if Modifiers.find("power") >= 0 and val >= 3:
                for i in fudge:
                    if i == 3 and val >= 3:
                        fudge[fudge.index(i)] = 6
                        val = val - 3
                        if val == 0:
                            break
            if Modifiers.find("chance") >= 0 and val >= 4:
                for i in fudge:
                    if i == 2 and val >= 4:
                        fudge[fudge.index(i)] = 6
                        val = val - 4
                        if val == 0:
                            break
            elif Modifiers.find("balance") >= 0 and val >= 4:
                pass
            else:
                for i in fudge:
                    if i == 1 and val >= 4:
                        fudge[fudge.index(i)] = 5
                        val = val - 4
                        if val == 0:
                            break
            if Modifiers.find("power") >= 0 and val >= 4:
                for i in fudge:
                    if i == 2 and val >= 4:
                        fudge[fudge.index(i)] = 6
                        val = val - 4
                        if val == 0:
                            break
            if Modifiers.find("chance") >= 0 and val >= 5:
                for i in fudge:
                    if i == 1 and val >= 5:
                        fudge[fudge.index(i)] = 6
                        val = val - 5
                        if val == 0:
                            break
            elif Modifiers.find("balance") >= 0 and val >= 3:
                pass
            return fudge
        while Dicepool > 36 or Dicepool < 0:
            print("Invalid dicepool.")
            return
        result = RollStart(Dicepool)
        Modifiers = Modifiers.lower()
        if Modifiers.find("exploding") >= 0:
            exp = Explode(result)
            for i in exp:
                result.append(i)
        if Modifiers.find("reroll") >= 0:
            rer = Reroll()
            for i in rer:
                result.append(i)
        result.sort(reverse=True)
        print("Diceroll result:", result)
        if Modifiers.find("fudge") >= 0:
            fud = Fudge()
            result = fud
            print("Fudge adjusted values:", result)
        successes = Successes()
        return successes

    def BaseRoller():
        print("This is the Hemlock dice roller. The instructions are simple.")
        print("Input your dicepool as an integer, then list your roll modifiers.")
        print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
        print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
        print("Enter 0 as your dicepool to end.")
        while True:
            Dicepool = int(input("Please input your dicepool: "))
            if Dicepool == 0:
                break
            Modifiers = input("Please list your modifiers: ")
            result = Roll(Dicepool, Modifiers)
            print("Number of Successes:", result)
    def CharacterCreate():
        print("This is the Hemlock dice roller, Character version.")
        print("Firstly, create your character.")
        name = input("Please input your character's name: ")
        abilities = {
            "drive": int(input("Input your character's Drive: ")),
            "grace": int(input("Input your character's Grace: ")),
            "strength": int(input("Input your character's Strength: ")),
            "mind": int(input("Input your character's Mind: ")),
            "wit": int(input("Input your character's Wit: ")),
            }
        marks = {
            "agility": [int(input("Input the number of marks your character has in Agility: ")), int(input("Any other numeric modifiers: "))],
            "endurance": [int(input("Input the number of marks your character has in Endurance: ")), int(input("Any other numeric modifiers: "))],
            "finesse": [int(input("Input the number of marks your character has in Finesse: ")), int(input("Any other numeric modifiers: "))],
            "might": [int(input("Input the number of marks your character has in Might: ")), int(input("Any other numeric modifiers: "))],
            "channeling": [int(input("Input the number of marks your character has in Channeling: ")), int(input("Any other numeric modifiers: "))],
            "perception": [int(input("Input the number of marks your character has in Perception: ")), int(input("Any other numeric modifiers: "))],
            "rebellion": [int(input("Input the number of marks your character has in Rebellion: ")), int(input("Any other numeric modifiers: "))],
            "stealth": [int(input("Input the number of marks your character has in Stealth: ")), int(input("Any other numeric modifiers: "))],
            "boldness": [int(input("Input the number of marks your character has in Boldness: ")), int(input("Any other numeric modifiers: "))],
            "coercion": [int(input("Input the number of marks your character has in Coercion: ")), int(input("Any other numeric modifiers: "))],
            "manipulation": [int(input("Input the number of marks your character has in Manipulation: ")), int(input("Any other numeric modifiers: "))],
            "tact": [int(input("Input the number of marks your character has in Tact: ")), int(input("Any other numeric modifiers: "))],
            "lore": [int(input("Input the number of marks your character has in Lore: ")), int(input("Any other numeric modifiers: "))],
            "medicine": [int(input("Input the number of marks your character has in Medicine: ")), int(input("Any other numeric modifiers: "))],
            "spirituality": [int(input("Input the number of marks your character has in Spirituality: ")), int(input("Any other numeric modifiers: "))],
            "wilderness": [int(input("Input the number of marks your character has in Wilderness: ")), int(input("Any other numeric modifiers: "))],
            "art": [int(input("Input the number of marks your character has in Art: ")), int(input("Any other numeric modifiers: "))],
            "cartography": [int(input("Input the number of marks your character has in Cartography: ")), int(input("Any other numeric modifiers: "))],
            "cooking": [int(input("Input the number of marks your character has in Cooking: ")), int(input("Any other numeric modifiers: "))],
            "cerbalism": [int(input("Input the number of marks your character has in Herbalism: ")), int(input("Any other numeric modifiers: "))],
            "literature": [int(input("Input the number of marks your character has in Literature: ")), int(input("Any other numeric modifiers: "))],
            "lockpicking": [int(input("Input the number of marks your character has in Lockpicking: ")), int(input("Any other numeric modifiers: "))],
            "smithing": [int(input("Input the number of marks your character has in Smithing: ")), int(input("Any other numeric modifiers: "))],
            "tailoring": [int(input("Input the number of marks your character has in Tailoring: ")), int(input("Any other numeric modifiers: "))],
            "tinkering": [int(input("Input the number of marks your character has in Tinkering: ")), int(input("Any other numeric modifiers: "))],
            } # I can probably cut this down on the user side - make it by default all zeroes, and ask the user what stats have marks or modifiers
        PlayerCharacter = Character(name, abilities, marks)
        return PlayerCharacter # Edit this to make a dictionary of different character objects with the name as the character. Maybe make a thing to ensure that repeat names don't cause a problem (background dictionary?)
    def CharacterRoller():
        print("Welcome to the Character Roller.")
        print("Simply input the ability, skill, bonuses, and modifiers to roll with.")
        print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
        print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
        print("Enter 0 as your ability to end")
        while True:
            ability = input("Input your ability: ")
            if ability == "0":
                return
            skill = input("Input your skill: ")
            Dicepool = PlayerCharacter.GetDicepool(ability, skill)
            Modifiers = input("Input your modifiers: ")
            result = Roll(Dicepool, Modifiers)
            print("Number of successes:", result)
    while True:
        print("Welcome to the Hemlock Roller. This roller has two modes: Character and Roller modes.")
        print("To open the character mode, input 1.")
        print("To open the roller mode, input 2.")
        print("To quit, input 0.")
        create = int(input())
        if create == 1:
            PlayerCharacter = CharacterCreate()
            CharacterRoller()
        elif create == 2:
            BaseRoller()
        else:
            "Invalid Input"

Hemlock()
