from music21 import converter, corpus, instrument, midi, note, chord, pitch, meter, duration, stream, environment
import os
from functools import *
import operator

print("\n-------------------- UserSettings --------------------")
us = environment.UserSettings()
# us['mscore'] = '/Applications/MuseScore\ 3.5.app/Contents/MacOS/mscore'
# print("us['mscore']",us['mscore'])
print()

underworld = "Mario-Sheet-Music-Underworld-Theme.mid"
death = "death.mid"
midi_path = "/Users/andres.kwan/Downloads/" + underworld


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
score.show()
score[0].flat.elements
g_part = score[0]


g_p1_sec = g_part.secondsMap
# g_p1_sec[5]
# g_p1_sec[7]
# g_p1_sec[11]
# type(g_p1_sec[11])

# g_p1_sec_11 = g_p1_sec[11]
print("g_p1_sec[9]",g_p1_sec[9])
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
print("timeSignature:",timeSignature[0])

# def splitComplexDuration(duration.Duration):

    
def getElement(dictionary):
    el = dictionary['element'] 
    ch = chord.Chord() 
    sil = note.Rest()
    nota = note.Note()
    complexDuration = duration.Duration()
    complexDuration.quarterLength = 2.25
    if type(el) == type(ch): 
        ordered_chord = el.sortAscending()
        el = ordered_chord[-1]
        if el.duration.type == complexDuration.type:
            # print("\n---split-chord---\n") 
            return [duration for duration in el.splitAtDurations()]
        return [el]
    if type(el) == type(nota):
        if el.duration.type == complexDuration.type: 
            # print("\n---split-note---\n")
            return [duration for duration in el.splitAtDurations()]
        return [el]
    if type(el) == type(sil):
        if el.duration.type == complexDuration.type: 
            # print("\n---split-rest---\n")
            return [duration for duration in el.splitAtDurations()]
        return [el]

def getTuplaPitchDuration(dictionary):
    el = dictionary['element'] 
    ch = chord.Chord() 
    sil = note.Rest()
    nota = note.Note()
    complexDuration = duration.Duration()
    complexDuration.quarterLength = 2.25
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

# print("\n-------------------- notes_from_midi --------------------")
# notes = list(filter(None,list(map(getTuplaPitchDuration, g_p1_sec))))
# print("notes_from_midi:\n",notes)

# print("\n-------------------- pitch & duration --------------------")
# pitch_and_duration = list(filter(None,list(map(getTuplaPitchDuration, g_p1_sec))))
# print("pitch_and_duration:\n",pitch_and_duration)
# print()

def getTuplaPitchDurationFromElement(el):
    ch = chord.Chord() 
    sil = note.Rest()
    nota = note.Note()
    complexDuration = duration.Duration()
    complexDuration.quarterLength = 2.25
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

def getListToneDurationFromElement(el,getTone,getDuration):
    ch = chord.Chord() 
    sil = note.Rest()
    nota = note.Note()
    complexDuration = duration.Duration()
    complexDuration.quarterLength = 2.25
    if type(el) == type(ch): 
        #process chord
        ordered_chord = el.sortAscending()
        el = ordered_chord[-1]
        return [getTone(el.pitch),getDuration(el.duration.type)]
    if type(el) == type(nota):
       #process note
        return [getTone(el.pitch),getDuration(el.duration.type)]
    if type(el) == type(sil):
        #process rest
        return [getTone(el.pitch),getDuration(el.duration.type)]

#split word 
def split(word): 
    return [char for char in word]  

#split data
def getNoteFromTuple(tuple_value):
    return split(tuple_value[0])

def getDurationFromTuple(tuple_value):
    return tuple_value[1]

# print(map(getSplittedNote, extracted_notes))
# print("\n-------------------- split notes --------------------")
# split_note = list(map(getSplittedNote, pitch_and_duration))
# print("split_notes:\n",split_note)
# print()

def charToTone(character):
    #0 represents a rest
    if character == "0":
        return "0"
    if character.isdigit():
        return character 
    if character == "#":
        return "S"
    #TODO: add bemol case
    return "NOTE_"+character

def charToNokia(character):
    #0 represents a rest
    if character == "0":
        return "REST"
    if character.isdigit():
        return character 
    if character == "#":
        return "S"
    #TODO: add bemol case
    return "NOTE_"+character

# notes_duration = list(map(getTimeDuration, pitch_and_duration)) 

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

# tones_duration = list(map(durationToToneDuration, notes_duration))
# print("tones_duration:\n",tones_duration)
# print()


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

print("\n-------------------- Elements --------------------")
elements = list(filter(None,list(map(getElement, g_p1_sec))))
print("elements:\n", elements)
print()

print("\n-------------------- flat list --------------------")
flat_list = [item for sublist in elements for item in sublist]
print("flat list:", flat_list)
print()

print("\n-------------------- stream --------------------")
stream1 = stream.Stream()
stream1.append(meter.TimeSignature('fast 2/2'))
stream1.append(flat_list)
stream1.show()
# print(stream1)

#this output work for nokia. 
print("\n-------------------- notes tuples --------------------")
notes = list(filter(None,list(map(getTuplaPitchDurationFromElement, flat_list))))
print("notes tuples:\n",notes)
print()

print("\n-------------------- split_notes --------------------")
split_note = list(map(getNoteFromTuple, notes))
print("split_notes:\n",split_note)
print()

print("\n-------------------- tones --------------------")
partial_list = [list([charToNokia(e) for e in sub_array]) for sub_array in split_note]
print("partial_list:\n",partial_list)
tones = ["".join([e for e in sub_array]) for sub_array in partial_list]
print("tones:\n",tones)
print()
# print("tones.count: ",tones.count)

print("\n-------------------- duration --------------------")
notes_duration = list(map(getDurationFromTuple, notes)) 
print("notes_duration:\n",notes_duration)
print()

print("\n-------------------- duration in tones notation --------------------")
tones_duration = list(map(durationToToneDuration, notes_duration))
print("tones_duration:\n",tones_duration)
print()
# print("tones_duration.count: ",tones_duration.count)

print("\n-------------------- combined tones and durations --------------------")
list(sum(zip(tones, tones_duration), ()))

# [list(a) for a in sum(zip(tones, tones_duration))]
# def getTone(el):
    #0 getNoote (string) 
    #1 split_note (split string)
    #2 

# ready_to_concatenate = [charToTone(val) for sublist in split_note for val in sublist]
# [ for sublist in split_notes for val in sublist funcion(val)]
# print(ready_to_concatenate)

# [map(charToTone,x) for x in split_note]
# [x for x in split_notes]

# I dont want to flat the 
# [" ".join([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]
# [list([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]

# [" ".join([str(x*y) for y in range(1,x+1)]) for x in range(1,8) ]

# notes = ["".join([e for e in sub_array]) for sub_array in partial_list]

