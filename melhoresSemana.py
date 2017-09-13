# -*- coding: utf-8 -*-

import requests
import json
import codecs
#import plotly.offline as offline
#import plotly.figure_factory as ff
import texttable as tt

tab = tt.Texttable()
header = [["Título", "Reproduções", "Download"]]
matriz = []
url = 'QUERY_URL'
views_primeiro = 0

segundo = requests.get(url).json()

with open('1.json') as json_data:
    primeiro = json.load(json_data)
with codecs.open( "primeiro.json", 'w', 'latin1') as f:
    json.dump(segundo, f)

for seg in segundo:
    for prim in primeiro:
        if prim['id'] == seg['id']:
            views_primeiro = prim['playback_count']
            break
        else:
            views_primeiro = 0
    contagem_semana = seg['playback_count'] - views_primeiro
    matriz.append([seg['title'], contagem_semana, seg['download_count']])

def pegaNumeroViews(item):
    return item[1]

ordenado = sorted(matriz, key=pegaNumeroViews, reverse=True)
ordenado = ordenado[0:10]

nova_matriz = header + ordenado

#tabela = ff.create_table(nova_matriz, height_constant=20)

#offline.plot(tabela, {'layout': {'title': 'As mais ouvidas'}},
#             image='png',link_text='um link text', output_type='file',filename='temp-plot.html',
#             image_filename='um_teste', image_width=800, image_height=600, validate=False)

tab.set_cols_width([100,12,10])
tab.add_rows(nova_matriz)
tabela = tab.draw()
print(tabela)
