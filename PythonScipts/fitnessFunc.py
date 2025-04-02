

import midiNote

#   Input : List of lists; the population of songs.
#   Output: population with fitness, average fitness, maximum fitness


def fitness(popu, files):
    i = 0
    total = 0
    maxfit = 0
    fitness = []
    for song in popu:
        fitness.append(0)
#        for k in range(files):
#            #Do fitness function thing here....
        a = arpeggio(song)
        b = longBass(song)
        c = scaleC(song)
        d = noRepeat(song)
        e = notTooHigh(song)
        fitness[i] = a + b + c + d + e
        total = total + fitness[i]
        maxfit = fitness[i] if fitness[i] > maxfit else maxfit
        i = i + 1
    return ([list(a) for a in zip(popu, fitness)], total/float(i), maxfit)


def arpeggio(song):
    fitness = 0
    for i in range(len(song) - 4):
        prev, dum, note, dum, next = song[i:i+5]  # Compare notes of same track
        noteDiff1 = abs(midiNote.getPitch(note) - midiNote.getPitch(next))
        noteDiff2 = abs(midiNote.getPitch(prev) - midiNote.getPitch(note))
        noteDiff3 = abs(midiNote.getPitch(next) - midiNote.getPitch(prev))
        if noteDiff1 == 4 and noteDiff2 == 3:
            fitness += 0.5
        if noteDiff1 == 3 and noteDiff2 == 4:
            fitness += 0.5
        if noteDiff3 == 7 or noteDiff3 == 6:
            fitness += 0.5
    fitness /= float(len(song)) if len(song) > 0 else 0
    return fitness*0.25


def longBass(song):
    fitness = 0
    for note in song:
        pitch = midiNote.getPitch(note)
        dur = midiNote.getDur(note)
        if pitch > 59 and dur < 64:
            fitness += 1
        if pitch < 51 and dur > 92:
            fitness += 1
    return fitness/float(len(song))*0.25


def scaleC(song):
    fitness = 0
    for note in song:
        pitch = midiNote.getPitch(note)
        if pitch % 12 in [0, 2, 3, 5, 7, 8, 10]:
            fitness += 1
    return fitness/float(len(song))*0.25


def noRepeat(song):
    fitness = 0
    for i in range(len(song) - 4):
        prev, dum, dum, dum, next = song[i:i+5]  # Compare notes of same track
        noteDiff3 = abs(midiNote.getPitch(next) - midiNote.getPitch(prev))
        if noteDiff3 != 0:
            fitness += 1
    fitness /= float(len(song)) if len(song) > 0 else 0
    return fitness*0.1


def notTooHigh(song):
    fitness = 0
    for note in song:
        if midiNote.getPitch(note) < 75:
            fitness += 1
    return fitness/float(len(song))*0.15
