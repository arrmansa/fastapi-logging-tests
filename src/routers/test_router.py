from fastapi import APIRouter
import logging
import uuid
from helpers.logging_uuid import logging_uuid
from helpers.some_function import some_function

import time

router = APIRouter()

@router.get("/test")
def status():
    current_uuid = uuid.uuid4()
    logging_uuid.set(current_uuid)
    logging.info("AMAZING")
    time.sleep(1)
    some_function()
    return str(current_uuid)
