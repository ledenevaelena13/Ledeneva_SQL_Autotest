# Елена Леденева, 14-я когорта — Финальный проект. Инженер по тестированию плюс

import requests

import configuration

import data


def post_order():
    return requests.post(url=configuration.URL + configuration.CREATE_AN_ORDER, json=data.body_orders)

def get_track(id_track):
    return requests.get(url=configuration.URL + configuration.RECEIVE_ORDER_BY_TRACK + str(id_track))

