from fastapi import FastAPI, Request, HTTPException
import requests
import uvicorn


app = FastAPI()


@app.get("/")
async def index():
    return {"success": True, "message": "Hello World"}


@app.post("/aws")
async def aws(r: Request):

    # retrieving payload
    try:
        payload = r.body()
    except Exception as ex:
        print(ex)
        raise HTTPException(400, detail="bad request")


    # sending data to AWS
    aws_response = requests.post(
        url="http://3.98.147.51:5002/",
        json=payload
    )

    status_code = aws_response.status_code
    data = aws_response.text

    if status_code == 200:
        return {"success": True, "data": payload, "aws_response": data}
    
    else:
        return {"success": False, "aws_response": data, "status_code": status_code}



if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=5000)
