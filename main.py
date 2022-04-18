import uvicorn
from fastapi import FastAPI, Depends
import my_dbase
from to_json import *
from my_valids import *
from pyngrok import ngrok
from fastapi.responses import JSONResponse

MY_HEADER = {"Access-Control-Allow-Origin": "*"}

app = FastAPI()


@app.get("/")
async def root():
    names = my_dbase.get_all_coin_names()
    my_json = to_json_names(names)
    return JSONResponse(content=my_json, headers=MY_HEADER)


# http://127.0.0.1:8000/all_hist/bitcoin
@app.get("/all_hist/{coin_name}")
async def all_hist(coin_name):
    hist = my_dbase.get_all_coin_hist_by_time(coin_name)
    my_json = to_json_all(coin_name, hist)
    return JSONResponse(content=my_json, headers=MY_HEADER)


# http://127.0.0.1:8000/coin_range?coin_name=avalanche&time_begin=2020-12-01-00-00-00&time_end=2020-12-02-00-00-00
@app.get("/coin_range")
async def coin_range(params: History_Range_Param_Valid = Depends(History_Range_Param_Valid)):
    hist = my_dbase.get_range_coin_hist_by_time(params)
    my_json = to_json_range_coin(params, hist)
    return JSONResponse(content=my_json, headers=MY_HEADER)


# http://127.0.0.1:8000/coin_page?coin_name=bitcoin&page=1&n_rows=20
@app.get("/coin_page")
async def coin_page(params: History_Page_Param_Valid = Depends(History_Page_Param_Valid)):
    hist = my_dbase.get_page_coin_hist_by_time(params)
    my_json = to_json_page_coin(params, hist)
    return JSONResponse(content=my_json, headers=MY_HEADER)


# http://127.0.0.1:8000/news_range?time_begin=2020-12-01-00-00-00&time_end=2020-12-02-00-00-00
@app.get("/news_range")
async def news_range(params: News_Range_Param_Valid = Depends(News_Range_Param_Valid)):
    news = my_dbase.get_range_news_hist_by_time(params)
    my_json = to_json_range_news(params, news)
    return JSONResponse(content=my_json, headers=MY_HEADER)


# http://127.0.0.1:8000/news_page?page=1&n_rows=20
@app.get("/news_page")
async def news_page(params: News_Page_Param_Valid = Depends(News_Page_Param_Valid)):
    news = my_dbase.get_page_news_hist_by_time(params)
    my_json = to_json_page_news(params, news)
    return JSONResponse(content=my_json, headers=MY_HEADER)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000)
