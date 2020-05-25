import codecs 
import json
import urllib.request
deposito = '/home/darkzera/path.json'

pasta = '/home/darkzera/testeDown/'

with codecs.open('/home/darkzera/Documentos/trying/full.json', encoding='utf-8-sig') as infos:
    datas = json.load(infos)
    counter = 0
    for id in datas["results"]:
        link = id["links"]
        linkStr = link.get("download")
        print(linkStr)
        fileName = pasta + str(counter) 
        print("Downloading " + fileName)
        urllib.request.urlretrieve(linkStr, fileName)
        print(fileName + "feito")
        counter += 1