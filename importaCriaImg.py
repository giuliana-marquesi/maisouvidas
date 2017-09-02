# -*- coding: utf-8 -*-

import requests
import json
import codecs

url = 'https://api.soundcloud.com/users/252453423/tracks?client_id=qpqr7lvfbvgt2DrSlaXoHjeiMxH99YR9&limit=200'

segundo = requests.get(url).json()

with open('1.json') as json_data:
    primeiro = json.load(json_data)

with codecs.open( "primeiro.json", 'w', 'latin1') as f:
    json.dump(segundo, f)

novo_json = []
bibl = {}

for seg in segundo:
    bibl = seg
    bibl = (item for item in primeiro if item['id'] == seg['id']).next()
    print(bibl)
    for prim in primeiro if prim['id'] == seg['id']:
        contagem_semana = seg['playback_count'] - prim['playback_count']
        print('subtracao', contagem_semana)
        bibl = seg
        bibl['playback_count'] = contagem_semana
        novo_json.append(bibl)
    novo_json.append(d)


def pegaNumeroViews(item):
    return item['playback_count']

ordenado = sorted(novo_json, key=pegaNumeroViews, reverse=True)

for audio in range(0, 10):
    titulo = ordenado[audio]['title']
    numeroViews = str(ordenado[audio]['playback_count'])
    numeroDownloads = str(ordenado[audio]['download_count'])

    print(titulo + ' ' + numeroViews + ' ' + numeroDownloads)
