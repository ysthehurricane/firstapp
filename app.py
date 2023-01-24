from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get('/')
async def index(request: Request):
    return HTMLResponse("<h1>Yash Patel</h1>")

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
