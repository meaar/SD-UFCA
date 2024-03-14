import datetime
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/dateTime")
async def read_dateTime():
    date = await read_getDate()
    time = await read_getTime()
    return date+','+time


@app.get("/time")
async def read_getTime():
    now = datetime.datetime.now()
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    if len(hour) < 2:   
        hour = '0'+hour
    elif len(minute) < 2:
        minute = '0'+minute
    elif len(second) < 2:
        second = '0'+second
    return hour+':'+minute+':'+second


@app.get("/date")
async def read_getDate():
    now = datetime.datetime.now()
    day = str(now.day)
    month = str(now.month)
    year = str(now.year)
    if len(day) < 2:   
        day = '0'+day
    elif len(month) < 2:
        month = '0'+month
    elif len(year) < 2:
        year = '0'+year
    return day+'-'+month+'-'+year
