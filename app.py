#     discord-time-tags helps you create multi-timezone messages for discord
#     Copyright (C) 2022 NebulaBC

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.

#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import Flask, render_template, request
from datetime import datetime
from waitress import serve
import re
import logging

logging.basicConfig()
logger = logging.getLogger("waitress")
logger.setLevel(logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def gettime():
    date = datetime.strptime(request.form["datetime"], "%Y-%m-%dT%H:%M")
    formattedTimestamp = "&lt;t:%s&gt;" % (
        str(datetime.timestamp(date)).split(".", 1)[0]
    )
    print(formattedTimestamp)
    return render_template(
        "index.html",
        timestamp="<br>Paste this code into discord for<br>a multi-timezone timestamp: %s <button onclick='copyToClipboard()'>copy</button>"
        % (formattedTimestamp),
        exTimestamp=(str(datetime.timestamp(date)).split(".", 1)[0]),
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=3001)
