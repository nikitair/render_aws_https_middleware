from fastapi import FastAPI, Request, HTTPException
import requests
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"success": True, "message": "Hello World"}


@app.options("/")
async def index():
    return {"success": True, "message": "Hello World"}


@app.post("/aws")
async def aws(r: Request):

    # retrieving payload
    try:
        payload = await r.json()
    except Exception as ex:
        print(ex)
        raise HTTPException(400, detail="bad request")


    # sending data to AWS
    aws_response = requests.post(
        url="http://52.23.187.142:5000/post_cookies",
        json=payload
    )

    status_code = aws_response.status_code
    aws_data = None

    try:
        aws_data = aws_response.json()
    except Exception as ex:
        print(ex)

    return {"payload": payload, "aws_response": aws_data, "aws_status_code": status_code}


@app.options("/aws")
async def index():
    return {"success": True, "message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
