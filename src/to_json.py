import pprint


def to_json_names(names):
    my_json = {}

    new_list_of_names = []
    for name in names:
        new_list_of_names.append({"coin_name": name.coin_parse,
                                  "coin_value": name.coin_value,
                                  "coin_time": name.coin_time})
    my_json["all_names"] = new_list_of_names
    return my_json


def to_json_all(name, list_of_prices):
    my_json = {"coin_name": name}

    new_list_of_prices = []
    for price in list_of_prices:
        new_list_of_prices.append([price.coin_time_in_sec * 1000, price.coin_value])

    my_json["history_list"] = new_list_of_prices
    return my_json


def to_json_range_coin(params, list_of_prices):
    my_json = {"coin_name": params.coin_name,
               "time_begin": params.time_begin,
               "time_end": params.time_end}

    new_list_of_prices = []
    for price in list_of_prices:
        new_list_of_prices.append({"coin_value": price.coin_value, "coin_time": price.coin_time})

    my_json["history_list"] = new_list_of_prices
    return my_json


def to_json_page_coin(params, list_of_prices):
    my_json = {"coin_name": params.coin_name,
               "page": params.page,
               "n_rows": params.n_rows}

    new_list_of_prices = []
    for price in list_of_prices:
        new_list_of_prices.append({"coin_value": price.coin_value, "coin_time": price.coin_time})

    my_json["history_list"] = new_list_of_prices
    return my_json


def to_json_range_news(params, list_of_news):
    my_json = {"time_begin": params.time_begin,
               "time_end": params.time_end}

    new_list_of_news = []
    for news in list_of_news:
        new_list_of_news.append({"news_title": news.news_title,
                                 "news_lead": news.news_lead,
                                 "news_time": news.news_time})

    my_json["news_list"] = new_list_of_news
    return my_json


def to_json_page_news(params, list_of_news):
    my_json = {"page": params.page,
               "n_rows": params.n_rows}

    new_list_of_news = []
    for news in list_of_news:
        new_list_of_news.append({"news_title": news.news_title,
                                 "news_lead": news.news_lead,
                                 "news_time": news.news_time})

    my_json["news_list"] = new_list_of_news
    return my_json
