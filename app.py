from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/')
async def index(request: Request):
    return HTMLResponse("<h1>Yash Patel</h1>")



if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)

# from flask import Flask

# @app.route('/', methods=["GET"])
# def index():
#     return "yash patel"

# app = Flask(__name__)

# if __name__ == '__main__':
#     app.run(debug=False)