import xmltodict, json
import time
starttime=time.time()
for i in range (100):
    with open("scratch.xml", "r", encoding="utf-8") as myfile:
        obj=xmltodict.parse(myfile.read())
    data=json.dumps(obj, ensure_ascii=False)
    #print(data)
    my_file = open("scratch.json", "w+", encoding="utf-8")
    my_file.write(data)
print(time.time()-starttime)