# Дмитрий Толченов, 10-я когорта, дипломный проект
import data
import configuration
import requests

# Функция: cоздать заказ
def create_order(order_body):
   return requests.post(configuration.URL + configuration.CREATE_ORDER_PATH, json=order_body)

# Сохраняем номер заказа
order_track_number = create_order(data.order_body).json()["track"]

# Функция: получить заказ по треку
def get_order_by_track(order_track_number):
    return requests.get(configuration.URL + configuration.GET_ORDER_BY_TRACK_PATH + str(order_track_number))

#получение данных о заказе по его треку
def test_get_order_by_track():
    data_order = get_order_by_track(order_track_number)
    assert data_order.status_code == 200