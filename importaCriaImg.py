#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

with open('1.json') as json_data:
    primeiro = json.load(json_data)

with open('2.json') as json_data:
    segundo = json.load(json_data)


def pegaNumeroViews(item):
    return item['playback_count']

ordenado = sorted(resposta, key=pegaNumeroViews, reverse=True)
