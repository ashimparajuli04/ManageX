from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scalar_fastapi import get_scalar_api_reference

from app.core.all_needed_imports import routers
from app.seed.permissions import seed_permissions

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    seed_permissions()
    yield


app = FastAPI(
    lifespan=lifespan,
    swagger_ui_parameters={
        "persistAuthorization": True
    }
)

for router in routers:
    app.include_router(router)


@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="ManageX API",
        persist_auth=True,
    )



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000","http://192.168.1.66:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
