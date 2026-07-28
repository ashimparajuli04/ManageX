# from contextlib import asynccontextmanager
from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

from app.core.all_routes import routers

# from app.seed.permissions import seed_permissions


@asynccontextmanager
async def lifespan(app: FastAPI):
    # seed_permissions()
    yield


app = FastAPI(lifespan=lifespan)

for router in routers:
    app.include_router(router)

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="ManageX API",
    )
