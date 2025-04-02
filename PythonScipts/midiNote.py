#
# Track number: 0-15
# Channel number: 0-15 (Channel 10 = percussion)
# Input: 32-bit integer (midi note info)
# Output: 4-bit integer (track info)

def getTrack(note):
    val = note & int('f0000000', 16)
    return val >> 28


# Input: 32-bit integer (midi note info)
# Output: 4-bit integer (channel info)
#---------------------------------------------------------------------- 
def getChan(note):
    val = note & int('0f000000', 16)
    return val >> 24
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info)
# Output: 8-bit integer (instrument info)
#---------------------------------------------------------------------- 
def getInst(note):
    val = note & int('00ff0000', 16)
    return val >> 16
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info)
# Output: 8-bit integer (duration info)
#---------------------------------------------------------------------- 
def getDur(note):
    val = note & int('0000ff00', 16)
    return val >> 8
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info)
# Output: 8-bit integer (pitch info)
#---------------------------------------------------------------------- 
def getPitch(note):
    return note & int('00000ff', 16)

#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info), 4-bit integer (track number)
# Output: 32-bit integer (midi note info with updated track)
#---------------------------------------------------------------------- 
def setTrack(note,track):
    val = note & int('0fffffff', 16)    # Clear current track
    val = val | (track << 28)            # Set track
    return val


#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info), 4-bit integer (channel number)
# Output: 32-bit integer (midi note info with updated channel)
#---------------------------------------------------------------------- 
def setChan(note,channel):
    val = note & int('f0ffffff', 16)    # Clear current channel
    val = val | (channel << 24)         # Set channel
    return val
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info), 4-bit integer (instrument number)
# Output: 32-bit integer (midi note info with updated instrument)
#---------------------------------------------------------------------- 
def setInst(note,instrument):
    val = note & int('ff00ffff', 16)    # Clear current instrument
    val = val | (instrument << 16)      # Set instrument
    return val
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info), 4-bit integer (duration value)
# Output: 32-bit integer (midi note info with updated duration)
#---------------------------------------------------------------------- 
def setDur(note,duration):
    val = note & int('ffff00ff', 16)    # Clear current duration
    val = val | (duration << 8)         # Set duration
    return val
    
#---------------------------------------------------------------------- 
# Input: 32-bit integer (midi note info), 4-bit integer (pitch value)
# Output: 32-bit integer (midi note info with updated pitch)
#---------------------------------------------------------------------- 
def setPitch(note,pitch):
    val = note & int('ffffff00', 16)    # Clear current pitch
    val = val | pitch                    # Set pitch
    return val
    
