import random

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

def Roll(Dicepool, Modifiers):
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