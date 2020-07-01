from bottle import route, run, view
from datetime import datetime as dt
from random import random
from horoscope import generate_prophecies

@route("/")
@view("predictions")
def index():
    now = dt.now()
    x = random()
    predictions = generate_prophecies() # Получаю рандомный список предсказаний

    return {
        "date": f"{now.day}-{now.month}-{now.year}",
        "predictions": predictions,
        "special_date": x > 0.5,
        "x": x
    }


@route("/api/forecasts")
def api_forecasts():
    predictions = generate_prophecies(total_num=6, num_sentences=2)

    return {
        "predictions": predictions,
    }


run(
    host="localhost",
    port=8080
)
