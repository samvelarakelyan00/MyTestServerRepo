from fastapi import FastAPI


app = FastAPI()

all_users = [
    {"name": "Samvel", "email": "samvel.arakelyan00@gmail.com"},
    {"name": "Tatev", "email": "tatevikyeghiazaryann5@gmail.com"},
]

@app.get("/")
def main():
    return {"message": "OK"}


@app.get("/users")
def get_all_users():
    return all_users
