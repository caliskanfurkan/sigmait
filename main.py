import json

veri = open("data.json","r").read()

loaded = json.loads(veri)

for i in loaded["incidents"]:
	for j in i["events"]:
		if i["source"] == "drops" or i["source"] == "process" or i["source"] == "registry":
			print(str(i["source"]))
			print(str(j)+"\n\n")
