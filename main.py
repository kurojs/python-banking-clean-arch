from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "code": 200,
        "message": "Success",
    }
