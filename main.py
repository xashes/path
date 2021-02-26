#!/usr/bin/env python3

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'Principle': 'Walk on the main path.'}
