#Ильин Денис, 8-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_request as sr

def test_creat_order_and_check_by_number():
    response = sr.post_new_order(data.body).json()
    order_track = response.get('track')
    response = sr.get_order_by_number(order_track)
    assert response.status_code == 200








