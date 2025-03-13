from fastapi import FastAPI

app = FastAPI()

@app.route('/api/')
def read():
    return {"message": "This is root!"}