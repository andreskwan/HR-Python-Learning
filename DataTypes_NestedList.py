studentsDict = {}
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    if score in studentsDict:
        studentsDict[score].append(name)
    else:
        studentsDict.setdefault(score, []).append(name)

print studentsDict.keys()
print studentsDict.values()

indexSecondScore = sorted(studentsDict.keys())[1]

studentsNames = studentsDict[indexSecondScore]

for name in sorted(studentsNames):
    print name


# dictOutput = {}
# value = 0
# for key in studentsDict:
#     if value == studentsDict[key]:#append
#         value = studentsDict[key]
#         dictOutput[key] = studentsDict[key]
#     if value < studentsDict[key]:
#         value = studentsDict[key]
#         dictOutput = {}
#         dictOutput[key] = studentsDict[key]
#
# for key in dictOutput:
#     print key

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 41
# Akriti
# 41
# Harsh
# 39
# Akriti
# Tina