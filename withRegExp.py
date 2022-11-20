import re
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
    data=data.replace('<?xml version="1.0" encoding="UTF-8" ?>', "")
    data=data.replace('<root>', '{')
    data=data.replace('</root>', '}')


    pattern=r"<(.*)?>(.*)?<\/\1>"
    pattern1 = r"<(.*)? />"
    pattern2=r"<(.*)?>(([^<\1>])*)?(<\/\1>)"
    pattern3 = r",((\s)*})"

    data = re.sub(pattern, r'"\1": "\2",', data)
    data = re.sub(pattern1, r'"\1": null,', data)
    data = re.sub(pattern2, r'"\1": {\2},', data)
    data = re.sub(pattern3, r'\1', data)

    #print(data)
    my_file = open("scratch.json", "w+")
    my_file.write(data)
    my_file.close()
print(time.time()-starttime)