#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"原则": ["行于大道", "熵减"]}


@app.get("/accounts")
async def accounts():
    return {"Accounts": []}


@app.post("/accounts/add")
async def add_account():
    return {}


@app.get("/transactions")
async def transactions():
    return {}


@app.get("/transactions/add")
async def add_transaction():
    return {}
