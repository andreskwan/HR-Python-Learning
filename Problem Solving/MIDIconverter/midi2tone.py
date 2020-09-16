from music21 import converter, corpus, instrument, midi, note, chord, pitch, meter
import os
from functools import *
import operator

# us = environment.UserSettings()

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

#how to make this function lazy
# if found do not keep looking 
def getTimeSignature(dictionary):
    el = dictionary['element'] 
    ts = meter.TimeSignature()
    if type(el) == type(ts):
        return el

timeSignature = list(filter(None,list(map(getTimeSignature, g_p1_sec))))
print("timeSignature:",type(timeSignature))

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

notes_from_midi = list(filter(None,list(map(getElement, g_p1_sec))))
print("notes_from_midi:\n",notes_from_midi)
print()
#split word 
def split(word): 
    return [char for char in word]  

#split data
def getSplittedNote(tuple_value):
    return split(tuple_value[0])

def getTimeDuration(tuple_value):
    return tuple_value[1]

# print(map(getSplittedNote, extracted_notes))
split_note = list(map(getSplittedNote, notes_from_midi))
print("split_notes:\n",split_note)
print()

def charToTone(character):
    if character == "0":
        return "0"
    if character.isdigit():
        return character 
    if character == "#":
        return "S"
    return "NOTE_"+character

notes_duration = list(map(getTimeDuration, notes_from_midi))

# “whole”, “half”, “quarter”, “eighth”, “16th”, “32nd”, “64th”
def durationToToneDuration(m21_duration):
    if m21_duration == "whole":
        return "1"
    if m21_duration == "half":
        return "2"
    if m21_duration == "quarter":
        return "4"
    if m21_duration == "eight":
        return "8"
    if m21_duration == "16th":
        return "16"
    if m21_duration == "32nd":
        return "32"
    if m21_duration == "64th":
        return "64" 

tones_duration = list(map(durationToToneDuration, notes_duration))
print("tones_duration:\n",tones_duration)
print()
# print("funcion('0'):",funcion('0'))
# print("funcion('1'):",funcion('1'))
# print("funcion('C'):",funcion('C'))
# print("funcion('#'):",funcion('#'))

# [funcion(y) for y in x for x in split_notes]
# map(reduce(operator.add, ) splitted_notes)
# reduce(operator.add, ["a","b","c"],"") #'abc'
# list(map(partial(reduce, operator.add, ""), split_notes))
# def getTone(list_split_note):
    # return reduce(+,map(func, list_split_note,""),"")
    # return reduce(lambda x, y: +, map(func, list_split_note,""),"")

# splitted_notes = list(map(getTone, splitted_notes))
# print(splitted_notes)

# splitted_notes = list(map(reduce, splitted_notes))



# from functools import partial
# nested_list = list(map( partial(map, str.lower), split_notes))

# [reduce(operator.add, x, "") for x in split_notes]
# list(map(funcion,x) for x in [["a","b","c"],["a","b","c"]])
# [funcion(val) for sublist in [["a","b","c"],["a","b","c"]] for val in sublist]
print("processing and flattening split_notes")
ready_to_concatenate = [charToTone(val) for sublist in split_note for val in sublist]
# [ for sublist in split_notes for val in sublist funcion(val)]
print(ready_to_concatenate)
[map(charToTone,x) for x in split_note]
# [x for x in split_notes]

# I dont want to flat the 
# [" ".join([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]
# [list([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]

partial_list = [list([charToTone(e) for e in sub_array]) for sub_array in split_note]
# tones_list = 

print(["".join([e for e in sub_array]) for sub_array in partial_list])
# [" ".join([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]

notes = ["".join([e for e in sub_array]) for sub_array in partial_list]