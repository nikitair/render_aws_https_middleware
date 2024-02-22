from fastapi import FastAPI, Request, HTTPException
import requests
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from logging_config import logger


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:5000",

    "https://aws-https-midleware.onrender.com/aws",
    "https://aws-https-midleware.onrender.com",

    "https://52.41.36.82:5000",
    "https://54.191.253.12:5000",
    "https://44.226.122.3:5000",

    "https://52.41.36.82:5000/aws",
    "https://54.191.253.12:5000/aws",
    "https://44.226.122.3:5000/aws",

    # dragontail
    "https://dragontail.choiceqr.com"
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
    logger.info(f"{index.__name__} -- index endpoint triggered")
    return {"success": True, "message": "index options"}


@app.options("/")
async def index_options():
    logger.info(f"{index_options.__name__} -- index_options endpoint triggered")
    return {"success": True, "message": "Hello World"}


@app.post("/aws")
async def aws(r: Request):

    # retrieving payload
    try:
        payload = await r.json()
        logger.info(f"{aws.__name__} -- payload received - {payload}")
    except Exception as ex:
        logger.error(f"{aws.__name__} -- !!! error occurred with payload - {ex}")
        raise HTTPException(400, detail="bad request")


    # sending data to AWS
    logger.info(f"{aws.__name__} -- sending data to AWS")
    aws_response = requests.post(
        url="http://52.23.187.142:5000/post_cookies_dragontail",
        json=payload
    )

    status_code = aws_response.status_code
    aws_data = None
    

    try:
        aws_data = aws_response.json()
    except Exception as ex:
        logger.error(f"{aws.__name__} -- !!! AWS error occurred - {ex}")

    logger.info(f"{aws.__name__} -- AWS status code - {status_code} - AWS response - {aws_data}")
    return {"payload": payload, "aws_response": aws_data, "aws_status_code": status_code}


@app.options("/aws")
async def aws_options():
    logger.info(f"{aws_options.__name__} -- aws_options endpoint triggered")
    return {"success": True, "message": "aws options"}


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
