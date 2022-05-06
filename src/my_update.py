import math
import time

import requests
from coin_market_cap_api import get_id_of_coin
from my_classes import DateData
from time_const import *
from time_data import time_data
import my_schemas
import my_dbase

URL_HIST_PER_HOUR = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/chart"


async def get_json(id, t_s, t_e):
    """Получаем список катировок в выбранном диапазоне"""
    my_range = str(t_s) + "~" + str(t_e)
    parameters = {
        "id": id,
        "range": my_range
    }
    return requests.get(URL_HIST_PER_HOUR, params=parameters).json()


async def get_id(coin_name):
    """Получаем id криптовалюты через запрос"""
    return get_id_of_coin(coin_name, "USD")


async def find_new(coin_name):
    """Получив самое посленнее время криптовалюты t_s начинаем делать запросы ПО ЧАСАМ
    и сохранять последние элементы в БД так как именно они будут следующими данными
    (через час) с того самого последнего времени t_s"""
    current_time = math.floor(time.time())
    t_s = my_dbase.get_time_of_last_update_of_coin(coin_name)
    t_e = t_s + HOUR
    id = None
    print(coin_name)
    while t_e < current_time - DAY:
        if id is None:
            id = await get_id(coin_name)
        print(id)
        my_json = await get_json(id, t_s, t_e)
        new_row_time = (list(my_json["data"]["points"].items()))[-1][0]
        new_row = my_json["data"]["points"][new_row_time]
        hour_date = DateData(coin_name,
                             time_data(time.ctime(int(new_row_time)), time_need=True),
                             new_row_time,
                             new_row["v"][0])
        print(hour_date)
        await my_dbase.insert_one_coin(hour_date)
        t_s = t_e
        t_e = t_e + HOUR


async def main_update():
    """Получаем список названий криптовалют и через цикр начинаем проверку"""
    crypt_list = my_dbase.get_all_coin_names()
    for coin_name in crypt_list:
        await find_new(coin_name)
