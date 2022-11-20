import time
starttime=time.time()
for i in range (100):
    def multiple_replace(target_str, replace_values):
        for i, j in replace_values.items():
            target_str = target_str.replace(i, j)
        return target_str
    def fileToString(xmlFile):
        myfile = open(xmlFile, "r", encoding="utf-8")
        xmlString = ''
        for i in myfile:
            xmlString += i
        return xmlString
    data=fileToString("scratch.xml")
    a="subject"
    b="teacher"
    c="weekNumber"
    d="weekInfo"
    e="format"
    f="place"
    g="class"
    h="startTime"
    i="finishTime"
    l="lesson"
    data=data.replace('<?xml version="1.0" encoding="UTF-8" ?>', "")
    data=data.replace('<root>', '{')
    data=data.replace('</root>', '}')
    replace_lessonsS={'<'+l+'1>':'"'+l+'1":{', '<'+l+'2>':'"'+l+'2":{','<'+l+'3>':'"'+l+'3":{','<'+l+'4>':'"'+l+'4":{',
                      '<'+l+'5>':'"'+l+'5":{','<'+l+'6>':'"'+l+'6":{','<'+l+'7>':'"'+l+'7":{','<'+l+'8>':'"'+l+'8":{' }
    replace_lessonsF={'</'+l+'1>': '},', '</'+l+'2>': '},', '</'+l+'3>': '},', '</'+l+'4>': '},', '</'+l+'5>': '},',
                      '</'+l+'6>': '},', '</'+l+'7>': '},', '</'+l+'8>': '}' }
    replace_empty_values={'<'+a+' />':'"'+a+'": null,', '<'+b+' />':'"'+b+'": null,', '<'+c+' />':'"'+c+'": null,',
                          '<'+d+' />':'"'+d+'": null,', '<'+e+' />':'"'+e+'": null,', '<'+f+' />':'"'+f+'": null,',
                          '<'+g+' />':'"'+g+'": null,', '<'+h+' />':'"'+h+'": null,', '<'+i+' />':'"'+i+'": null,',
                          '<'+l+' />':'"'+l+'": null,', }
    replace_values = {'</'+a+'>': '",',  '</'+b+'>': '",',   '</'+d+'>': '",',  '</'+e+'>': '",',  '</'+f+'>': '",',
                      '</'+g+'>': '",',  '</'+h+'>': '",',  '</'+i+'>': '"',  '</'+c+'>': '",' }

    data=multiple_replace(data, replace_lessonsS)
    data=multiple_replace(data, replace_lessonsF)
    data=multiple_replace(data, replace_empty_values)
    data=multiple_replace(data, replace_values)
    data=data.replace('<', '"')
    data=data.replace('>', '": "')
    #print(data)
    my_file = open("scratch.json", "w+")
    my_file.write(data)
    my_file.close()
print(time.time()-starttime)