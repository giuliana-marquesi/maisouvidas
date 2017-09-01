#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Este arquivo faz parte de uma serie para automatizar o trabalho de enviar as musicas mais ouvidas da semana
## no formato de um grafico
##
## Este arquivo especificamente pega as musicas criadas na ultima semana e as ordena. Por fim exporta um grafico

import codecs
import requests
from datetime import datetime, timedelta
import texttable as tt

tab = tt.Texttable()
header = ["Título", "Reproduções", "Downloads"]
tab.header(header)
tab.set_cols_width([100,12,10])

url = 'QUERY_URL'
sete_dias_atras = datetime.now() - timedelta(days=7)
url_completa = url + "created_at[from]=" + str(sete_dias_atras)

resposta = requests.get(url_completa).json()

def pegaNumeroViews(item):
    return item['playback_count']

ordenado = sorted(resposta, key=pegaNumeroViews, reverse=True)


for audio in range(0, 10):
    titulo = ordenado[audio]['title']
    numero_views = str(ordenado[audio]['playback_count'])
    numero_downloads = str(ordenado[audio]['download_count'])
    linha_tabela = [titulo, numero_views, numero_downloads]
    tab.add_row(linha_tabela)

tabela = tab.draw()

print(tabela)
arquivo_tabela = codecs.open("criadasMaisOuvidas.md", 'a', 'utf-8')
arquivo_tabela.write(tabela)
arquivo_tabela.close()
