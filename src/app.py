from fastapi import FastAPI
import logging
from helpers.logging_uuid import change_logging
from routers import test_router

change_logging()

app = FastAPI( title="test_app", version="1.0")
app.include_router(test_router.router)
