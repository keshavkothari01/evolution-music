#!/usr/bin/python

import writeNote
import midiNote
import random

# ----------------------------------------------------------------------
#   Input : Number of Tracks, Number of notes, Number of songs in population
#   Output: initialized list with population of songs
# ----------------------------------------------------------------------


def initPop(numTracks, numNotes, popSize):
    song = list()
    population = list()
    note = 0
    note = midiNote.setInst(note, 0)
    for k in range(popSize):
        del song[:]
        for i in range(numNotes):
            for j in range(numTracks):
                note = midiNote.setChan(note, j+1)
                note = midiNote.setTrack(note, j+1)
                note = midiNote.setPitch(note, random.randint(40, 90))
                note = midiNote.setDur(note, random.randint(16, 128))
                song.append(note)
        population.append(song[:])  # song[:] for splicing a copy of song
    return population
