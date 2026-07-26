# from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.all_routes import routers

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     yield

# app = FastAPI(lifespan=lifespan)

app = FastAPI()

for router in routers:
    app.include_router(router)
