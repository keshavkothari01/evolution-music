

import midiNote

#   Input   : note      -> 32-bit integer for the midiNote info
#             noteDict  -> dictonary with note-to-str key values.
#             f         -> file pointer
#   Output  : f will have written the midiNote tclearo the file in an
#             appropriate format


def writeNote(note, noteDict, f):
    track = midiNote.getTrack(note)
    channel = midiNote.getChan(note)
    noteStr = noteDict[midiNote.getPitch(note)]
    duration = (midiNote.getDur(note)) / 4/8.
    fraction = duration.as_integer_ratio()
    wholeNum = (fraction[0])/int(fraction[1])
    numer = fraction[0] % fraction[1]
    # output = "FOL   (BA %4d   CR %9.6f)   TR %2d   CH %2d   NT  %8s   %d+%d/%d\n"\
    #          % (bar, time, track, channel, noteStr, wholeNum, numer, fraction[1])
    output = "FOL  TR %2d   CH %2d   NT  %8s   %d+%d/%d\n"\
             % (track, channel, noteStr, wholeNum, numer, fraction[1])
    f.write(output)
