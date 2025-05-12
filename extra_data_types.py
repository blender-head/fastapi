from fastapi import FastAPI
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID

app = FastAPI()


'''
additional data types you can use:
- UUID
- datetime.datetime (2008-09-15T15:53:00+05:00)
- datetime.date (2008-09-15)
- datetime.time (14:23:55.003)
- datetime.timedelta
- frozenset
- bytes
- Decimal
'''
@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }