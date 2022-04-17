import uvicorn
from fastapi import FastAPI, Depends
import my_dbase
from to_json import *
from my_valids import *

app = FastAPI()


@app.get("/")
async def root():
    names = my_dbase.get_all_coin_names()
    my_json = to_json_names(names)
    return my_json


# http://127.0.0.1:8000/all_hist/bitcoin
@app.get("/all_hist/{coin_name}")
async def all_hist(coin_name):
    hist = my_dbase.get_all_coin_hist_by_time(coin_name)
    my_json = to_json_all(coin_name, hist)
    return History_Valid(**my_json)


# http://127.0.0.1:8000/range?coin_name=avalanche&time_begin=2020-12-01-00-00-00&time_end=2020-12-02-00-00-00
@app.get("/range")
async def my_range(params: History_Range_Param_Valid = Depends(History_Range_Param_Valid)):
    hist = my_dbase.get_range_coin_hist_by_time(params)
    my_json = to_json_range(params, hist)
    return History_Range_Resp_Valid(**my_json)


# http://127.0.0.1:8000/page?coin_name=bitcoin&page=1&n_rows=20
@app.get("/page")
async def page_and_limit(params: History_Page_Param_Valid = Depends(History_Page_Param_Valid)):
    hist = my_dbase.get_page_coin_hist_by_time(params)
    my_json = to_json_page(params, hist)
    return History_Page_Resp_Valid(**my_json)


if __name__ == "__main__":
    uvicorn.run("main:app")
