import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

sdict = json.loads(sampleJson)
print(sdict['company']['employee']['payable']['salary'])
sdict['company']['employee']['birth_date'] = '1999-09-19'

with open('sampleJson.json', 'w') as f:
    json.dump(sdict, f, indent=4)
