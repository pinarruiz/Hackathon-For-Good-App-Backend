from fastapi import FastAPI
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware
from fastapi.middleware.cors import CORSMiddleware

from .others.query_models import Coordinates

from .others.tags import api_tags
from .others.helpers import read_csv
from .config import Settings
from .routers import ia_router, system_router

app = FastAPI(openapi_tags = api_tags,
    docs_url = "/docs" if Settings().DEBUG else None)

app.state.locations = read_csv("dataset_contendores.csv")

app.add_middleware(TrustedHostMiddleware, allowed_hosts = Settings().ALLOWED_HOSTS)
app.add_middleware(ProxyHeadersMiddleware)
app.add_middleware(CORSMiddleware, allow_origins=Settings().ALLOWED_HOSTS,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(router = ia_router, prefix = "/api/v1/ia")
app.include_router(router = system_router, prefix = "/api/v1/system")