import pandas as pd 

file = 'pitches.h'

header_list = ["define", "pitch", "value"]

# data = pd.read_csv(file, skiprows=3, header=0)
data = pd.read_csv(file, sep='\s+',names=header_list, usecols=["pitch", "value"], converters={"value":str.strip})

data.head()

