#just trying out dictionaries
#hashTableForFrqTask but better :D
sentence = "Kalle Anka og Cookiemonster dro til alicante i spania og leide en bil . Kalle Anka likte ikke bilen og Cookiemonster spiste en cookie"
arr = sentence.split(" ")

def putInDict(arr):
    dictList = {}
    for element in arr:
        if  element in dictList:
            value = dictList[element] + 1
            dictList.update({element:value})
        else:
            dictList[element] = 1
    return dictList


print(putInDict(arr))
