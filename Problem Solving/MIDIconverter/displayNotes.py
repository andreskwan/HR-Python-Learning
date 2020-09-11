from music21 import *

n = note.Note("C4") # what type is 'n' so it could be open by MS
n.duration.type = 'half'
# n.pitch
# This opens Music Score App! 
n.show()

# ch = chord.Chord("G4 B4")
# ch.duration.type = 'half'
# ch.show()
#how to print a chord how to print Chord G4 B4 