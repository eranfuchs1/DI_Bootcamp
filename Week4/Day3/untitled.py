'''

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sampleDict['class']['student']['marks']['history'])


sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]

for key in keysToRemove:
    if key in sampleDict:
        del sampleDict[key]
print(sampleDict)
'''
print([x if x % 3 == 0 else x * 3 for x in range(10) if x % 2 == 0])
