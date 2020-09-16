import json
data='{"var1":"yash","var2":34}'
# print(data.[var1]
parsed=json.loads(data)
print(parsed['var2'])

data2={
    "channe":"yash",
    "cars":['bnw','audi','ferari'],
    "fridge":('roti',23),
    "istask":False
}
jscomp=json.dumps(data2)
print(jscomp)
