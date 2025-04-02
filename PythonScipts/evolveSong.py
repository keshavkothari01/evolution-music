

import initPop as init
import fitnessFunc
import mutations

#   Evolve song:
#       Creates an initial population of songs
#       Runs "genLength" generations
#           Each checks fitness of each member in population
#           Sort them from highest to lowest
#           Replace bottom members with mutations from higher members
#       Output the top XX songs in integer format.
#
#       Variable Description:
#           pop is list of [song, fitness] lists
#           popu is list of songs
#           song is a list of notes
#           notes are 32 bit integers

numTracks = 2
numNotes = 80
popSize = 40
genLength = 400
numOfBest = 20
mnm = 3

popu = list()
popu = init.initPop(numTracks, numNotes, popSize)

# Generation 0
(pop, avgFit, maxFit) = fitnessFunc.fitness(popu, 3)
pop.sort(key=lambda x: float(x[1]), reverse=True)
# print "Init Pop.    Avg Fit ", avgFit, "      Max Fit ", maxFit
print(0, avgFit, maxFit)

# Generation 1->genLength
for i in range(genLength):
    popu = mutations.mutation(pop, numOfBest, mnm)
    (pop, avgFit, maxFit) = fitnessFunc.fitness(popu, 3)
    pop.sort(key=lambda x: float(x[1]), reverse=True)
    # print("Gen ", i+1, "      Avg Fit ", avgFit, "      Max Fit ", maxFit)
    print(i, avgFit, maxFit)

# Write best song to file
f = open("best", "w")
for note in pop[0][0]:
    f.write(str(note) + "\n")
f.close()
