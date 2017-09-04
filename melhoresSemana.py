# -*- coding: utf-8 -*-

import requests
import json
import codecs
import texttable as tt

tab = tt.Texttable()
header = ["Título", "Reproduções", "Downloads"]


matriz = [["Título", "Reproduções", "Downloads"]]

url = 'QUERY'

segundo = requests.get(url).json()

with open('1.json') as json_data:
    primeiro = json.load(json_data)

with codecs.open( "primeiro.json", 'w', 'latin1') as f:
    json.dump(segundo, f)

def pegaNumeroViews(item):
    return item[1]

views_primeiro = 0

for seg in segundo:
    for prim in primeiro:
        if prim['id'] == seg['id']:
            views_primeiro = prim['playback_count']
            break
        else:
            views_primeiro = 0
    contagem_semana = seg['playback_count'] - views_primeiro
    matriz.append([seg['title'], contagem_semana, seg['download_count']])

ordenado = sorted(matriz, key=pegaNumeroViews, reverse=True)
ordenado = ordenado[0:11]

tab.set_cols_width([100,12,10])
tab.header(header)
tab.add_rows(ordenado)
tabela = tab.draw()
print(tabela)

arquivo_tabela = codecs.open("melhoresSemana.md", 'a', 'utf-8')
arquivo_tabela.write(tabela)
arquivo_tabela.close()
