import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_USER_ORDER,json=body, headers=data.headers)



response = post_new_order(data.body).json()
order_track = response.get('track')


def get_order_by_number():
    return requests.get(configuration.URL_SERVICE + configuration.CHECK_USER_ORDER + str(order_track), headers=data.headers)




