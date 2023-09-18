#Ильин Денис, 8-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_request as sr

def test_creat_order_and_check_by_number():
    response = sr.get_order_by_number()
    assert response.status_code == 200








