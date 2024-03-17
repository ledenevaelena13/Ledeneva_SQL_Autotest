# Елена Леденева, 14-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data
import configuration

def test_create_an_order():
    response_order = sender_stand_request.post_order()
    id_track = response_order.json()['track']
    response = sender_stand_request.get_track(id_track)
    assert response.status_code == 200