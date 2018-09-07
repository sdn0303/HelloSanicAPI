# -*- Coding: UTF-8 -*-
from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/hello")
async def hello(request):
    return json({"Message": "Hello Sanic!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9999, debug=True, access_log=True)
