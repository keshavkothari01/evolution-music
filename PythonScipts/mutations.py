

import random as r
import midiNote as m

#   Mutations:
#       Crossover and a number of single point mutations
#   Input:  the population of songs, the amount of top songs, and
#           the number of single point mutations
#   Output: The population of songs after mutations; no fitness values yet


def mutation(pop, numOfBest, mnm):
    bestInGen = list()
    nextGen = list()
    child = list()
    parentOne = list()
    parentTwo = list()
    # Copy over the top songs
    for i in range(numOfBest):
        bestInGen.append(pop[i][0][:])
        nextGen.append(bestInGen[i])

    neededSongs = len(pop) - numOfBest
    for i in range(neededSongs):
        # Randomly select two of the best songs
        parentOne = bestInGen[r.randint(0, len(bestInGen)-1)]
        parentTwo = bestInGen[r.randint(0, len(bestInGen)-1)]
        subLen = r.randint(1, len(parentOne)-1)
        pt = r.randint(0, len(parentOne) - subLen)
        subList = parentOne[pt:pt+subLen]
        pt = r.randint(0, len(parentOne) - subLen)
        child = parentTwo[:]
        child[pt:pt+subLen] = subList

        # Have variable size songs (DOESN"T WORK NICELY)
#        # Take a random sublist from parent one
#        ptOne = r.randint(0,len(parentOne)-subLen)
#        ptTwo = r.randint(0,len(parentOne))
#        if ptOne > ptTwo: ptOne, ptTwo = ptTwo, ptOne
#        subList = parentOne[ptOne: ptTwo]
#        # splice it into a random section from parent two
#        ptOne = r.randint(0,len(parentTwo))
#        ptTwo = r.randint(0,len(parentTwo))
#        if ptOne > ptTwo: ptOne, ptTwo = ptTwo, ptOne
#        child = parentTwo[:]
#        child[ptOne:ptTwo] = subList
#        # Make sure child isn't empty
#        if len(child) == 0: child.append(0)

        # Single point mutations
        for i in range(0, mnm):
            note = r.randint(0, len(child)-1)
            child[note] = m.setPitch(child[note], r.randint(30, 110))
            child[note] = m.setDur(child[note], r.randint(30, 110))

        # Add to next generation
        nextGen.append(child)

    return nextGen
