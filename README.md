# fastapi-logging-tests
tests with contextvars and adding a custom arrtibute to the log record with https://docs.python.org/3/library/logging.html#logrecord-objects when multithreading

tested with 
```bash
time yes -- '-f' | head -20 | xargs -n 1 -P 20 \
curl http://0.0.0.0:5432/test \
--write-out "" --silent --output null
```
Uses .replace to eliminate newline spam
Changes the recordfactory to add uuid
