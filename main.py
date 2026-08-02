from HemlockRoller import Roll
import Menus as m
import CharacterOptions as co

def initialize():
    print("Welcome to the Hemlock roller version 5!")
    print("This is a program currently run through the command prompt,")
    print("which has functions to roll dice using Hemlock's system.")
    print("When asked for an input, ensure that a numeric input is just a number,")
    print("and a modifier input only contains modifiers and the required values.")
    print("I hope you enjoy!")
    print("In the future, the initialization will include a preferences selection")
    print("Press enter to continue...")
    input()
    prefs = {}
    return prefs

def printRules():
    with open("overview.txt", 'r') as file:
        overview = file.read()
        print(overview)
    input()

def main(prefs):
    chars = {}
    char = None
    choice = 0
    while choice != None:
        choice = m.MainMenu()
        if choice == 1: # Single Roll
            roll = ()
            while roll != None:
                roll = m.RollerMenu()
                if roll == None:
                    continue
                dicepool = roll[0]
                modifiers = roll[1]
                try:
                    result = Roll(dicepool, modifiers)
                except ValueError:
                    print("Input not accepted.")
                    return
                print("Roll result:", result["Roll"])
                if "Fudge" in result:
                    print("Fudge adjusted values:", result["Fudge"])
                print("Number of Successes:", result["Successes"])        
        elif choice == 2 and char == None: # Stat roll
            print("No character selected")
        elif choice == 2: # Stat roll
            ability = input("Please enter an ability:\n")
            abilityOptions = ["drive", "grace", "strength", "mind", "wit"]
            skill = input("Please enter a skill:\n")
            skillOptions = ["agility", "endurance", "finesse", "might", "channeling", "perception", "rebellion", "stealth", "boldness", "coercion", "manipulation", "tact", "lore", "medicine", "spirituality", "wilderness", "art", "cartography", "cooking", "herbalism", "literature", "lockpicking", "smithing", "tailoring", "tinkering"]
            if ability.lower() not in abilityOptions:
                print("Invalid ability")
                continue
            if skill.lower() not in skillOptions:
                print("Invalid skill")
                continue
            dicepool = char.GetDicepool(ability, skill)
            modifiers = input("Please enter your modifiers:\n")
            try:
                result = Roll(dicepool, modifiers)
            except ValueError:
                print("Input not accepted.")
                return
            print("Roll result:", result["Roll"])
            if "Fudge" in result:
                print("Fudge adjusted values:", result["Fudge"])
            print("Number of Successes:", result["Successes"])
        elif choice == 3: # Preset roll
            print("Preset rolls not implemented. Expected to be in version 6.")
        elif choice == 4: # Display character
            if char == None:
                print("No character selected")
                continue
            else:
                char.display()
        elif choice == 5: # Character menu
            exited = False
            while exited == False:
                exited, limited, _choice = m.CharMenu(chars, char)
                if limited == True:
                    if _choice == 1:
                        chars, char = co.CharacterCreate(chars)
                    elif _choice == 2:
                        chars, char = co.CharacterLoad(chars, input("Input your desired filename:\n"))
                else:
                    if _choice == 1:
                        char = co.CharacterSelect(chars, char)
                    elif _choice == 2:
                        char = co.CharacterEdit(char)
                    elif _choice == 3:
                        chars, char = co.CharacterCreate(chars)
                    elif _choice == 4:
                        chars = co.CharacterDelete(chars)
                    elif _choice == 5:
                        chars, char = co.CharacterLoad(chars, input("Input your desired filename:\n"))
                    elif _choice == 6:
                        char.SaveCharacter(input("Input your desired filename:\n"))
        elif choice == 6: # Overview
            printRules()
        elif choice == 7: # Preferences
            m.Preferences(prefs)

prefs = initialize()
main(prefs)
