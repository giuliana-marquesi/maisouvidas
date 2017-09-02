# -*- coding: utf-8 -*-

import requests
import json
import codecs

novo_json = []

url = 'URL'

segundo = requests.get(url).json()

with open('1.json') as json_data:
    primeiro = json.load(json_data)

with codecs.open( "primeiro.json", 'w', 'latin1') as f:
    json.dump(segundo, f)


def pegaNumeroViews(item):
    return item['playback_count']

views_primeiro = 0

for seg in segundo:
    for prim in primeiro:
        if prim['id'] == seg['id']:
            views_primeiro = pegaNumeroViews(prim)
            break
        else:
            views_primeiro = 0
    contagem_semana = seg['playback_count'] - views_primeiro
    seg['playback_count'] = contagem_semana
    novo_json.append(seg)



ordenado = sorted(novo_json, key=pegaNumeroViews, reverse=True)

for audio in range(0, 10):
    titulo = ordenado[audio]['title']
    numeroViews = str(ordenado[audio]['playback_count'])
    numeroDownloads = str(ordenado[audio]['download_count'])

    print(titulo + ' ' + numeroViews + ' ' + numeroDownloads)
