#hash table
#metoder: insert key-value pair, del key-value pair, search for value given a key
#Program skal lese liste med ord og bruke hash table for å telle frekvensen av hvert ord

class hashElement:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# Lagt for oppgaven spesifikk, value er antall ganger ordet gjentar seg, key er ordet
# eksempel "Kalle Kalle" vil bli lagret som key:"Kalle" value:2
class hashTable:
    def __init__(self):
        self.list = []
    
    # inKey = insertKey, key used in parameter
    def insertKeyValue(self,inKey):
        if self.cheackForDuplicateKey(inKey):
            for element in self.list:
                if element.key == inKey:
                    element.value +=1
                    return
        else:
            element = hashElement(inKey,1)
            self.list.append(element)
    
    def deleteValueGivenKey(self,inKey):
        for element in self.list:
            if element.key == inKey:
                self.list.remove(element)
                return

    def cheackForDuplicateKey(self,inKey):
        for element in self.list:
            if element.key == inKey:
                return True
        return False
    
    def searchForValueGivenKey(self, inKey):
        for element in self.list:
            if element.key == inKey:
                return element.value
        print("Did not find it")
    
    def printKeyAndValue(self):
        for element in self.list:
            print("key:",element.key, "value:", element.value)

str = "Kalle Anka og Cookiemonster dro til alicante i spania og leide en bil . Kalle Anka likte ikke bilen og Cookiemonster spiste en cookie"

arr = str.split(" ")
print(arr)
table = hashTable()
i = 0
for element in arr:
    table.insertKeyValue(arr[i])
    i += 1

table.printKeyAndValue()

print(table.searchForValueGivenKey("Kalle"))

table.deleteValueGivenKey("Anka")

table.printKeyAndValue()