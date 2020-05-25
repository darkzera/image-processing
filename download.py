import codecs 
import json
import urllib.request

pasta = '/home/darkzera/testeDo/'

with codecs.open('/home/darkzera/Documentos/wallpaper-downloader/t.json', encoding='utf-8-sig') as infos:
    datas = json.load(infos)
    counter = 0
    for id in datas["results"]:
        link = id["links"]
        linkStr = link.get(" download")
        print(linkStr)
        fileName = pasta + str(counter) 
        print("Downloading " + fileName)
        urllib.request.urlretrieve(linkStr, fileName)
        print(fileName + " done")
        counter += 1