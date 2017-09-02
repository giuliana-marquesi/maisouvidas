# -*- coding: utf-8 -*-
### Este arquivo faz parte de uma série para automatizar o trabalho de enviar as musicas mais ouvidas da semana
## no formato de um grafico
##
## Este documento especificamente ordena as 200 ultimas musicas, das mais ouvidas as menos e exporta um json ordenado

import sys
import requests
import json
import codecs
#import urllib.parse
#urllib.parse.urlenconde()
nome_doc = str(sys.argv[1]) + ".json"

url = 'URL_QUERY'

resposta = requests.get(url).json()

#def pegaNumeroId(item):
#    return item['id']

#ordena_id = sorted(resposta, key=pegaNumeroId)

with codecs.open( "antigo.json", 'w', 'latin1') as f:
    json.dump(resposta, f)

for audio in range(0, 10):
    titulo = resposta[audio]['title']
    numeroViews = str(resposta[audio]['playback_count'])
    numeroDownloads = str(resposta[audio]['download_count'])

    print(titulo + ' ' + numeroViews + ' ' + numeroDownloads)
