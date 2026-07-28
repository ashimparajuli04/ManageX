# from contextlib import asynccontextmanager
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.all_routes import routers

# from app.seed.permissions import seed_permissions


@asynccontextmanager
async def lifespan(app: FastAPI):
    # seed_permissions()
    yield


app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)
