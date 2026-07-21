# from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.auth import routes
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

# app = FastAPI(lifespan=lifespan)

app = FastAPI()

app.include_router(routes.router)