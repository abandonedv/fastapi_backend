from pydantic import BaseModel
from typing import List


class History_Item_Valid(BaseModel):
    coin_value: float
    coin_time: str


class History_Valid(BaseModel):
    coin_name: str
    history_list: List[History_Item_Valid]


class History_Range_Param_Valid(BaseModel):
    coin_name: str
    time_begin: str
    time_end: str


class History_Range_Resp_Valid(BaseModel):
    coin_name: str
    time_begin: str
    time_end: str
    history_list: List[History_Item_Valid]


class History_Page_Param_Valid(BaseModel):
    coin_name: str
    page: int
    n_rows: int


class History_Page_Resp_Valid(BaseModel):
    coin_name: str
    page: int
    n_rows: int
    history_list: List[History_Item_Valid]
