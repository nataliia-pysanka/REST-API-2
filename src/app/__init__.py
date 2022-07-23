from flask import Flask
from flask_migrate import Migrate
from .db import db

from datetime import datetime
import pytz

app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def hello_world():  # put application's code here
    PLOVDIV_TZ = pytz.timezone("Europe/Sofia")
    timeInPlovdiv = datetime.now(PLOVDIV_TZ)
    currentTimeInPlovdiv = timeInPlovdiv.strftime("%H:%M")
    msg = f"The current time in Plovdiv is: {currentTimeInPlovdiv}"
    return msg, currentTimeInPlovdiv


if __name__ == '__main__':
    app.run()
