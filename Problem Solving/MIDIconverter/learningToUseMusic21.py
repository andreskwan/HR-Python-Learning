import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from music21 import *
from music21 import converter, corpus, instrument, midi, note, chord, pitch
# Listing current data on our folder.
import os

us = environment.UserSettings()
# mscore_local = '/Applications/MuseScore 3.5.app/Contents/MacOS/mscore'
# us['mscore'] = mscore_local
# for key in sorted(us.keys()):
#     print(key)

# print("-----------array of directories--------")
# print(os.listdir("."))

midi_path = "/Users/andres.kwan/Downloads/death.mid"
# sonic_folder = "sonic"

# !rm -r $midi_path
# !mkdir $midi_path

# Some helper methods.    
def concat_path(path, child):
    return path + "/" + child

# complete_path = concat_path(midi_path,sonic_folder)

# print(midi_path)

def open_midi(midi_path, remove_drums):
    # There is an one-line method to read MIDIs
    # but to remove the drums we need to manipulate some
    # low level MIDI events.
    mf = midi.MidiFile()
    mf.open(midi_path)
    mf.read()
    mf.close()
    # print("print tracks", mf.tracks)
    if (remove_drums):
        for i in range(len(mf.tracks)):
            # print("track number", i)
            mf.tracks[i].events = [ev for ev in mf.tracks[i].events if ev.channel != 10]          

    return midi.translate.midiFileToStream(mf)
    
# base_midi = open_midi(concat_path(sonic_path, "green-hill-zone.mid"), True)
score = open_midi(midi_path, True)
# base_midi

# midi.translate.channelInstrumentData(base_midi)
# <music21.stream.iterator.StreamIterator for Score:0x7feaee3120d0_flat @:0>
# print(base_midi.flat.notes)
# print(type(score)) # <class 'music21.stream.Score'>
# print(type(score.elements)) # 
#K
# print(type(score.flat.notes)) # <class 'music21.stream.iterator.StreamIterator'>

# shift-enter
# score.elements
# score[0].elements
score[0].flat.elements
type(score[0].flat.elements[3]) #Metronome
mm = score[0].flat.elements[3]
score.duration.quarterLength


# for n in score.notes:
#     print(n)

# stream object 
# score.show()

# Command history in interactive window %history
g_part = score[0]
# g_part.flat
# g_part.elements
# g_part.show('text')
# g_part.flat.notes.stream().show('text')
# g_part.pitches
# p1_pitches = g_part.pitches
# len(p1_pitches)
# g_part.secondsMap
g_p1_sec = g_part.secondsMap
# g_p1_sec[5]
# g_p1_sec[7]
# g_p1_sec[11]
# type(g_p1_sec[11])
g_p1_sec_11 = g_p1_sec[11]
# g_p1_sec_11
# # %history

def getElement(dictionary):
    el = dictionary['element'] 
    ch = chord.Chord() 
    sil = note.Rest()
    nota = note.Note()
    if type(el) == type(ch): 
        #process chord
        ordered_chord = el.sortAscending()
        el = ordered_chord[-1]
        return (str(el.pitch),str(el.duration.type))
    if type(el) == type(nota):
       #process note
        return (str(el.pitch),str(el.duration.type))
    if type(el) == type(sil):
        #process rest
        return ("0",str(el.duration.type))

extracted_notes = list(filter(None,list(map(getElement, g_p1_sec))))
print(extracted_notes)

g_p1_sec
score.duration
score.duration.quarterLength
# # score[0].finalBarLine
# type(score)
# # score.seconds
score[0].seconds
# score[0].timeSignature
score[0].metadata
# g_p1_sec_11
# g_p1_sec_11['element']
# type(g_p1_sec_11['element'])
c_unknown = g_p1_sec_11['element']
c_unknown.duration
# c_unknown.duration.type
# c_unknown.duration.dots
# c_unknown.commonName
# c_unknown.fullName
# c_unknown.notes
# c_unknown.root

# c_unknown.pitchNames                #['D', 'F']
# chord_pitches = [p.midi for p in c_unknown.pitches] #[74, 77] # type list<int>
# #How to get the pitch form the midi 
# c_unknown.sortAscending()


# c_unknown.pitchNames
# c_unknown.notes
# c_unknown.duration.type #'quarter'
# g_p1_sec_11
# g_p1_sec_11
# g_p1_sec
# g_p1_sec_11['element']
# c_unknown.bass
# c_unknown.canBeTonic
# type(g_p1_sec_11['element']) #Chord
# c_unknown.containsTriad
# c_unknown.pitchNames
# c_unknown.isChord

# def getElement(dictionary):
#     el = dictionary['element'] 
#     ch = chord.Chord() 
#     sil = note.Rest()
#     nota = note.Note()
#     if type(el) == type(ch): 

#         # print(el)
#         # print("pitch names:", el.pitchNames)
        

#         ordered_chord = el.sortAscending()
#         el = ordered_chord[-1]
#         # print("nota:", el.pitch)
#         # print(str(el.pitch))
#         # print(el.duration.type) #'quarter'
#         return (str(el.pitch),str(el.duration.type))
#     if type(el) == type(nota):
#         # print(el)
#         # print("pitch type",type(str(el.pitch)))
#         # print("duration type",type(str(el.duration.type))) #'quarter'
#         # print("nota:",str(el.pitch))
#         # print(str(el.pitch))
#         # print("duration:",str(el.duration.type)) #'quarter'
#         # print(el.duration.type) #'quarter'
#         return (str(el.pitch),str(el.duration.type))
#     if type(el) == type(sil):
#         # print(el)
#         # print(el.pitch)
#         # print("rest")
#         # print(el.duration.type) #'quarter'
#         return ("0",str(el.duration.type))



# def getDuration(duration):


#identify if it is None -> next
#identify if it is 0 -> 
#it is a note build the equivalent. 


# for diccionario in g_p1_sec:
#     print(getElement(diccionario))





















# for n in base_midi.flat.notes:
#     print("Note: %s%d %0.1f" % (n.pitch.name, n.pitch.octave, n.duration.quarterLength))

# def list_instruments(midi):
#     partStream = midi.parts.stream()
#     print("List of instruments found on MIDI file:")
#     for p in partStream:
#         aux = p
#         print (p.partName)

# list_instruments(base_midi)


# def extract_notes(midi_part):
#     parent_element = []
#     ret = []
#     for nt in midi_part.flat.notes:        
#         if isinstance(nt, note.Note):
#             ret.append(max(0.0, nt.pitch.ps))
#             parent_element.append(nt)
#         elif isinstance(nt, chord.Chord):
#             for pitch in nt.pitches:
#                 ret.append(max(0.0, pitch.ps))
#                 parent_element.append(nt)
    
#     return ret, parent_element
# print(extract_notes())

# def extract_notes(midi_part):
#     parent_element = []
#     ret = []
#     for nt in midi_part.flat.notes:        
#         if isinstance(nt, note.Note):
#             print(nt)
#             ret.append(max(0.0, nt.pitch.ps))
#             parent_element.append(nt)
#         elif isinstance(nt, chord.Chord):
#             for pitch in nt.pitches:
#                 ret.append(max(0.0, pitch.ps))
#                 parent_element.append(nt)
    
#     return ret, parent_element

# def print_parts_countour(midi):
#     fig = plt.figure(figsize=(12, 5))
#     ax = fig.add_subplot(1, 1, 1)
#     minPitch = pitch.Pitch('C10').ps
#     maxPitch = 0
#     xMax = 0
    
#     # Drawing notes.
#     for i in range(len(midi.parts)):
#         top = midi.parts[i].flat.notes  
#         # print(top)                
#         y, parent_element = extract_notes(top)
#         # print(parent_element)
#         if (len(y) < 1): continue
            
#         x = [n.offset for n in parent_element]
#         # print(x) 
#         ax.scatter(x, y, alpha=0.6, s=7)
        
#         aux = min(y)
#         if (aux < minPitch): minPitch = aux
            
#         aux = max(y)
#         if (aux > maxPitch): maxPitch = aux
            
#         aux = max(x)
#         if (aux > xMax): xMax = aux
    
#     for i in range(1, 10):
#         linePitch = pitch.Pitch('C{0}'.format(i)).ps
#         if (linePitch > minPitch and linePitch < maxPitch):
#             ax.add_line(mlines.Line2D([0, xMax], [linePitch, linePitch], color='red', alpha=0.1))            

#     plt.ylabel("Note index (each octave has 12 notes)")
#     plt.xlabel("Number of quarter notes (beats)")
#     plt.title('Voices motion approximation, each color is a different instrument, red lines show each octave')
#     plt.show()

# # Focusing only on 6 first measures to make it easier to understand.
# print_parts_countour(base_midi.measures(0, 6))


# listsToReduce = [[[1,2,3], [3,2,1]], [[1,3,5], [5,3,1]]]
# reducedLists = [list(map(sum, zip(*lst))) for lst in listsToReduce]
# print(reducedLists)