from music21 import converter, corpus, instrument, midi, note, chord, pitch
import os
from functools import reduce

us = environment.UserSettings()

midi_path = "/Users/andres.kwan/Downloads/death.mid"

def open_midi(midi_path, remove_drums):
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
    
score = open_midi(midi_path, True)
score[0].flat.elements
g_part = score[0]

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
print()
#split word 
def split(word): 
    return [char for char in word]  

#split data
def getSplittedNote(tuple_value):
    return split(tuple_value[0])

splitted_notes = list(map(getSplittedNote, extracted_notes))
print(splitted_notes)
print()

def func(character):
    if character == "0":
        return character

def getTone(list_split_note):
    return reduce(func, list_split_note,"") 

splitted_notes = list(map(getTone, splitted_notes))
print(splitted_notes)

splitted_notes = list(map(reduce, splitted_notes))

