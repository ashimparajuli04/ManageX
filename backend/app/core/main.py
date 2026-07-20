from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()  # create tables, seed data, etc.
    yield
    # cleanup code here if needed

app = FastAPI(lifespan=lifespan)