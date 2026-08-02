from HemlockRoller import TestInt

def MainMenu(): # Output: Choice
    options = {
        "0:": "Exit",
        "1:": "Single Roll",
        "2:": "Stat Roll",
        "3:": "Set Rolls",
        "4:": "View Character",
        "5:": "Character Options",
        "6:": "Overview",
        "7:": "Preferences"
        }
    print("Main Menu:")
    keys = list(options.keys())
    for i in keys:
        print(f"{i:<3} {options[i]:>}")
    Choice = TestInt("Enter your choice:\n", 0, 7)
    if Choice == 0:
        return None
    return Choice 

def AbilityMenu(CharName): # Output: selected, newValue
    abilList = [
        "Drive",
        "Grace",
        "Strength",
        "Mind",
        "Wit"
        ]
    print(f"Editing ability of {CharName}: ")
    number = "0:"
    function = "Exit"
    print(f"{number:<3} {function:>}")
    for count, ability in enumerate(abilList, start=1):
        print(f"{str(count) + ":":<3} {ability:>}")
    Choice = TestInt("Select an ability:\n", 0, 5)
    if Choice == 0:
        return None
    selected = abilList[Choice - 1]
    newValue = TestInt("Enter a new value for the ability: ", 0)
    return selected, newValue

def SkillMenu(CharName): # Output: selected, marks, bonus
    skills = {
        "Physical Skills": ("Agility", "Endurance", "Finesse", "Might"),
        "Focus Skills": ("Channeling", "Perception", "Rebellion", "Stealth"),
        "Social Skills": ("Boldness", "Coercion", "Manipulation", "Tact"), 
        "Knowledge Skills": ("Lore", "Medicine", "Spirituality", "Wilderness"), 
        "Trade Skills": ("Art", "Cartography", "Cooking", "Herbalism", "Literature", "Lockpicking", "Smithing", "Tailoring", "Tinkering")
        }
    CatList = ["Physical Skills", "Focus Skills", "Social Skills", "Knowledge Skills", "Trade Skills"]
    skillTypes = list(skills.keys())
    print("Changing a skill value for {CharName}: ")
    number = "0:"
    function = "Exit"
    print(f"{number:<3} {function:>}")
    for count, _type in enumerate(skillTypes, start=1):
        print(f"{str(count) + ":":<3} {_type}")
    Choice = TestInt("Choose the skill category:\n", 0, 5)
    if Choice == 0:
        return None
    selected = CatList[Choice - 1]
    SkillList = skills[selected]
    number = "0:"
    function = "Exit"
    print(f"{number:<3} {function:>}")
    for count, skill in enumerate(SkillList, start=1):
        print(f"{str(count) + ":":<3} {skill:>}")
    Choice = TestInt("Choose the skill in the category:\n", 0, len(SkillList))
    if Choice == 0:
        return None
    selected = SkillList[Choice - 1]
    marks = TestInt("Input the number of marks in the skill:\n", 0, 4)
    test = False
    while test == False:
        try:
            bonus = int(input("Input any additional modifiers:\n"))
            test = True
        except ValueError:
            continue
    return selected, marks, bonus

def Preferences(prefs): # Output: Preferences (NOT IMPLEMENTED)
    print("Preferences not yet implemented. Estimated to be implemented in version 6.")

def CharMenu(chars, char): # Output: Exited, limited, Choice
    OptionsLim = ["Create Character", "Load Character"]
    Options = ["Select Character", "Edit Character", "Create Character", "Delete Character", "Load Character", "Save Character"]
    if char == None:
        print("No character selected. Limited menu:\n")
        number = "0:"
        function = "Exit"
        print(f"{number:<3} {function:>}")
        for number, option in enumerate(OptionsLim, start=1):
            print(f"{str(number) + ":":<3} {option:>}")
        Choice = TestInt("Choose an option:\n", 0, len(OptionsLim))
        if Choice == 0:
            return True, True, None
        return False, True, Choice
    else:
        print(f"Selected character: {char.GetName()}.")
        number = "0:"
        function = "Exit"
        print(f"{number:<3} {function:>}")
        for number, option in enumerate(Options, start=1):
            print(f"{str(number) + ":":<3} {option:>}")
        Choice = TestInt("Choose an option:\n", 0, len(Options))
        if Choice == 0:
            return True, False, None
        return False, False, Choice

def RollerMenu(): # Returns dicepool and modifiers
    print("\nInitializing Roll...")
    print("Enter a number to roll, enter 0 to exit.")
    print("Ensure you separate modifiers with spaces and include values for those that require it.")
    dicepool = TestInt("Please enter your dicepool:\n", 0, 36)
    if dicepool == 0:
        return None
    print("Please enter your modifiers:")
    modifiers = input()
    return dicepool, modifiers
