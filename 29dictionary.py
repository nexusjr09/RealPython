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

