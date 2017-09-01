# -*- coding: utf-8 -*-

import json

with open('1.json') as json_data:
    primeiro = json.load(json_data)

with open('2.json') as json_data:
    segundo = json.load(json_data)

novo_json = []
bibl = {}
for d in segundo:
    for i in primeiro:
        if d['id'] == i['id']:
            contagem_semana = d['playback_count'] - i['playback_count']
            print('subtracao', contagem_semana)
            bibl = d
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
