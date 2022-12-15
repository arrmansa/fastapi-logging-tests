from fastapi import FastAPI
import logging
from helpers.logging_uuid import logging_uuid
from routers import test_router

old_factory = logging.getLogRecordFactory()
def record_factory(*args, **kwargs):
    record = old_factory(*args, **kwargs)
    record.uuid = logging_uuid.get("uuid")
    return record
logging.setLogRecordFactory(record_factory)

logging.basicConfig(level=logging.INFO, 
     format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s, %(uuid)s %(message)s',
     datefmt='%H:%M:%S')

app = FastAPI( title="test_app", version="1.0")
app.include_router(test_router.router)
