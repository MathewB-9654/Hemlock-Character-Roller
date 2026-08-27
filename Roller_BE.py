import random

#%% BASE FUNCTIONS

def roll(dicepool):
    # The base roll function, used throughout the program. Returns the final result. 
    result = []
    for i in len(dicepool):
        result.append(random.randint(1,6))
    return result

def testdie(roll, modifiers):
    # Uses modifier values to test dice for successes. Returns the number of successes. 
    successes = 0
    if "chance" in modifiers and not "balance" in modifiers and roll == 6:
        successes += 1
    elif "balance" in modifiers and not "chance" in modifiers and roll >= 4:
        successes += 1
    elif roll >= 5:
        successes += 1
    if "power" in modifiers and roll == 6:
        successes += 1
        
    return successes

def applymods(roll, modifiers):
    # Given the roll and modifier dictionary, applies the modifier functions. Returns a dictionary with initial roll, modified roll and successes. 
    final = {}
    final["initial"] = roll[:]
    if "reroll" in modifiers:
        val = modifiers["reroll"]
        roll = reroll(roll, val)
    if "exploding" in modifiers:
        val = modifiers["exploding"]
        roll = explode(roll, val)
    if "fudge" in modifiers:
        val = modifiers["fudge"]
        roll = fudge(roll, val, modifiers)
    successes = 0
    for i in roll:
        successes += testdie(i, modifiers)
    if "leverage" in modifiers and successes > 0:
        successes += modifiers["leverage"]
    if "hinderance" in modifiers:
        successes -= modifiers["leverage"]
    final["final"] = roll[:]
    final["successes"] = successes
    return final

#%% MODIFIER FUNCTIONS
# These functions apply modifiers and return the new total roll. 

def reroll(roll, val):
    #The reroll modifier rerolls any dice equal to or below the value. 
    amt = sum(1 for x in roll if x <= val)
    _roll = [x for x in roll if x > val]
    roll = _roll
    return roll.extend(roll(amt))

def explode(roll, val):
    # The explode modifier rolls additional dice equal to the number of dice equal to or above the value. Recursive. 
    nroll = roll
    while any(x > 10 for x in nroll):
        amt = sum(1 for x in nroll if x >= val)
        nroll = roll(amt)
        roll.extend(nroll)
    return roll

def fudge(roll, val, modifiers):
    roll.sort(reverse=True)
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
                current = testdie(die, modifiers)
                upgraded = testdie(target, modifiers)
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
    
