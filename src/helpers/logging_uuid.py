import contextvars
import logging
import re

logging_uuid = contextvars.ContextVar("uuid")

def change_logging():
  old_factory = logging.getLogRecordFactory()
  def record_factory(*args, **kwargs):
      record = old_factory(*args, **kwargs)
      record.uuid = logging_uuid.get("uuid")
      if isinstance(record.msg, str):
          record.msg = record.msg.replace("\\", "\\\\").replace("\n", "\\n")
      return record
  logging.setLogRecordFactory(record_factory)
  logging.basicConfig(level=logging.INFO, format= '%(asctime)s | {%(pathname)s:%(lineno)d} | %(levelname)s | %(uuid)s | %(message)s', force=True)
