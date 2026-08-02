from CharacterClass import Character
import json
from HemlockRoller import TestInt

def CharacterCreate(chars): # Output: chars, char
    print("Welcome to the Character Creator.")
    print("Please input a name, and the character will automatically create with basic stats.")
    print("You will then be redirected to the character editor.")
    print("Please input your character's name:")
    name = input()
    chars, char = CharacterInit(chars, name)
    char = CharacterEdit(char)
    return chars, char
    
def CharacterInit(chars, name):
    CharInit = Character(name)
    charactersIndex = list(chars.keys())
    characterNum = len(charactersIndex) + 1
    chars[characterNum] = CharInit
    return chars, CharInit
        
def CharacterSelect(chars, char): # Output: char
    print("Character select:")
    CharNums = list(chars.keys())
    zero = "0:"
    action = "Cancel"
    print(f"{zero:<3} {action}")
    for i in CharNums:
        Char = chars[i]
        name = Char.GetName()
        print(f"{str(i) + ":":<3} {name:>}")
    selection = TestInt("Select your desired character:\n", 0, len(CharNums))
    if selection == 0:
        return char
    else:
        return chars[CharNums[selection - 1]]

def CharacterLoad(chars, filename): # Output: chars, char
    with open(f'{filename}.txt', 'r') as file:
        Retrieved = json.load(file)
    if Retrieved["Is a valid sheet"]:
        name = Retrieved["name"]
        abilities = Retrieved["abilities"]
        skills = Retrieved ["skills"]
        tradeskills = Retrieved["trade skills"]
    CharLoad = Character(name, abilities, skills, tradeskills)
    charactersIndex = list(chars.keys())
    characterNum = len(charactersIndex) + 1
    chars[characterNum] = CharLoad
    return chars, CharLoad

def CharacterEdit(char): # Output: char
    selection = 1
    while selection != 0:
        print(f"Select what you would like to edit in {char.GetName()}:")
        num = [0, 1, 2]
        action = ["Cancel", "Abilities", "Skills"]
        for i in num:
            print(f"{str(i) + ":":<3} {action[i]}")
        selection = TestInt("", 0, len(num))
        if selection == 0:
            return char
        elif selection == 1:
            char.EditAbilities()
        elif selection == 2:
            char.EditSkills()
    return char

def CharacterDelete(chars): # Output: chars
    print("Character select:")
    CharNums = list(chars.keys())
    zero = "0:"
    action = "Cancel"
    print(f"{zero:<3} {action}")
    for i in CharNums:
        char = chars[i]
        name = char.GetName()
        print(f"{str(i) + ":":<3} {name:>}")
    selection = TestInt("Select the character you want to delete:\n", 0, len(CharNums))
    if selection == 0:
        return chars
    else:
        selection = selection - 1
        newChars = {}
        for i in CharNums[:selection]:
            newChars[i] = chars[i]
        if selection + 1 <= len(CharNums):
            for i in CharNums[selection + 1:]:
                newChars[i - 1] = chars[i]
        return newChars

def CharacterSave(char): # No outputs
    filename = input("Please enter your desired filename:\n")
    print(f"Saving character to {filename}.txt...")
    char.SaveCharacter(filename)
    print("Character saved!")


if __name__ == "__main__":
    chars = {}
    for i in range(5):
        chars, char = CharacterCreate(chars)
    print(chars)
    print(CharacterDelete(chars))