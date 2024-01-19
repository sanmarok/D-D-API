from classes import *
from os import system
from fastapi import FastAPI


api = FastAPI()


@api.get("/")
async def test():
    return "uwu"

if __name__ == "__main__":
    system('python -m uvicorn main:api --reload')
