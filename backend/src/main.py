import logging.config

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from asgi_correlation_id import CorrelationIdMiddleware
from log_config import LOGGING_CONFIG
from resources.routers import api_router


origins = [
    "http://localhost",
]

logging.config.dictConfig(LOGGING_CONFIG)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(CorrelationIdMiddleware)

app.include_router(api_router)
