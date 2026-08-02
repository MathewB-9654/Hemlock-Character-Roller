import random
def Hemlock():
    # Master function. From before plans pivoted.
    def Roll(amount):
        #Basic roll function. "Rolls" a set of six-sided dice.
        rollresult = []
        for i in range(amount):
            rollresult.append(random.randint(1, 6))
        return rollresult
    def Explode(exploding):
        # applies the 'exploding' modifier. Rolls more dice if any are above the value. Recursive.
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
        # applies the 'reroll' modifier. Rerolls dice below the value
        rerollresult = []
        rerollpool = 0
        for i in result:
            if i <= int(Modifiers[Modifiers.find("reroll") + 7]):
                result.pop(result.index(i))
                rerollpool = rerollpool + 1
        rerollresult = Roll(rerollpool)
        if Modifiers.find("exploding") >= 0:
            rerexp = Explode(rerollresult)
            for i in rerexp:
                rerollresult.append(i)
        return rerollresult
    def Successes():
        # Determines the number of successes.
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
        # Applies the modifier 'fudge', changing the dice results by a number of difference equal to the value.
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
        else:
            pass
        return fudge
    print("This is the Hemlock dice roller. The instructions are simple.")
    print("Input your dicepool as an integer, then list your roll modifiers.")
    print("Supported modifiers are power, balance, chance, leverage, reroll, fudge, and exploding.")
    print("Ensure you format modifiers with a value as 'modifier value'. Eg: Reroll 1, and separate all modifiers with a ', '.")
    print("Enter 0 as your dicepool to end.")
    while True:
        #Dicepool function. Loops itself, so that you can roll without closing.
        Dicepool = int(input("Please input your dicepool: "))
        if Dicepool == 0:
            break
        while Dicepool > 36 or Dicepool < 0:
            print("Invalid dicepool.")
            Dicepool = int(input("Please input your dicepool: "))
        Modifiers = input("Please list your modifiers: ")
        result = Roll(Dicepool)
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
        print("Number of Successes:", successes)

Hemlock()
