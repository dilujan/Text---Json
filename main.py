import json

parentDict = {}
with open('textfile.txt') as f:
    parentDict['result'] = f.readline().strip()

    for i in range(2):
        tempDict = {}
        tempDict['Team'], tempDict['Score'] = f.readline().strip().split()
        tempList = f.readline().strip().split(' ', 1)
        tempDict[tempList[0]] = tempList[1]
        tempList.clear()
        tempList = f.readline().strip().split(' ', 1)
        tempDict[tempList[0]] = tempList[1]

        if i == 0:
            first_inning = tempDict
        else:
            second_inning = tempDict

    parentDict['first_inning'], parentDict['second_inning'] = first_inning, second_inning
    jsonOut = open('result.json', 'w')
    json.dump(parentDict, jsonOut, indent=4, sort_keys=False)
    jsonOut.close()
