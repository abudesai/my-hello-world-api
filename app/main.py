import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/say_hello")
def say_hello():
    return {
        "message": "Hello World! Welcome to my app!!!” "
    }
    

if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=80)               