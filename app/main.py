from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def dummy_get():
    return {'message': "Hello from docker hub image and CI/CD workflow"}