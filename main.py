import json

veri = open("data.json","r").read()

loaded = json.loads(veri)

for i in loaded["incidents"]:
	print(str(i["source"])+"\n\n")
