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

url = 'QUERY_URL'

resposta = requests.get(url).json()

def pegaNumeroId(item):
    return item['id']

ordena_id = sorted(resposta, key=pegaNumeroId)

with codecs.open( nome_doc, 'w', 'latin1') as f:
    json.dump(ordena_id, f)

for audio in range(0, 10):
    titulo = ordena_id[audio]['title']
    numeroViews = str(ordena_id[audio]['playback_count'])
    numeroDownloads = str(ordena_id[audio]['download_count'])

    print(titulo + ' ' + numeroViews + ' ' + numeroDownloads)
