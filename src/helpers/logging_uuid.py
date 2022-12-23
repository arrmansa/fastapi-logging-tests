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
          record.msg = re.sub(r"(\\*\n)|(\\+n)", lambda x: x.group()[:-1]*2 + ('n' if x.group()[-1]=='n' else '\\n'), record.msg)
          # doubles number of \ appearing directly before n. eg '\\\n' -> '\\\\\\n'
          # reverse using 
          # record.msg = re.sub(r"(\\*\n)|(\\+n)", lambda x: '\\' * ((len(x.group())-1)//2) + ('n' if len(x.group())%2 else '\n'), record.msg)
      return record
  logging.setLogRecordFactory(record_factory)
  logging.basicConfig(level=logging.INFO, format= '%(asctime)s | {%(pathname)s:%(lineno)d} | %(levelname)s | %(uuid)s | %(message)s', force=True)
