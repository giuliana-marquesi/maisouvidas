# -*- coding: utf-8 -*-
### Este arquivo faz parte de uma serie para automatizar o trabalho de enviar as musicas mais ouvidas da semana
## no formato de um grafico
##
## Este arquivo especificamente pega as musicas criadas na ultima semana e as ordena. Por fim exporta um grafico

import codecs
import requests
from datetime import datetime, timedelta
#import texttable as tt
import plotly.offline as offline
import plotly.figure_factory as ff
import sys

#resolve problemas com acentuação das strings, erro dado no python 2.7
reload(sys)
sys.setdefaultencoding('utf8')

#tab = tt.Texttable()
#tab.header(header)
#tab.set_cols_width([100,12,10])
matriz = [["Título", "Reproduções", "Downloads"]]

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
    matriz.append(linha_tabela)

tabela = ff.create_table(matriz, height_constant=20)

#def adjust_column_widths(ff_table, n_cols=2, new_xs=[1.]):
#    for i,entry in enumerate(ff_table['layout']['annotations']):
#        print(i)
#        if i % n_cols!=0:
#            entry['x'] = new_xs[(i % n_cols)-1]
#
#adjust_column_widths(tabela)

offline.plot(tabela, {'layout': {'title': 'As mais ouvidas'}},
             image='png',link_text='um link text', output_type='file',filename='temp-plot.html', image_filename='um_teste', image_width=800, image_height=600, validate=False)
