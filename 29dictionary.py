#dictionary 

capitals = {"USA":"Washington DC",
        "Nepal": "Kathmandu",
        "China":"Bejing",
        "India": "NewDelhi"}
#print(dir(capitals))
print(capitals.get("Nepal"))
print(capitals.get('USA'))

if capitals.get("Japan"):
    print("Capital Exists ! ")
else:
    print("Capital doesn't exists")

capitals.update({"Japan":"Tokyo"}) # USED TO UPDATE VALUES IN CAPITALS 
print(capitals)
capitals.pop("Nepal")
print(capitals) #removes the value from the dictionary ! 
#capitals.popitem() ------> removes the latest value added . 
#capitals.clear()-----> clears all the value inside dictionary !

#KEYS 
keys = capitals.keys()
for key in capitals.keys():
    print(key)

