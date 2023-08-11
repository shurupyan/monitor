import logging

import redis.asyncio as redis
from decouple import config

database = redis.Redis(host=config('DB_HOST'), port=config('DB_PORT'), db=0)

TS_TYPE = b'TSDB-TYPE'
NONE_TYPE = b'none'
KEY_PREFIX = 'speedtest'


async def get_or_create_ts_key(labels: dict = None) -> str | None:
    if labels:
        key = f'{KEY_PREFIX}:{":".join(labels.values())}'
    else:
        key = f'{KEY_PREFIX}:fake'
    res = await database.type(name=key)
    if res == TS_TYPE:
        logging.debug(f'Found TS key: {key}')
    elif res == NONE_TYPE:
        logging.debug(f'Key {key} not found, creating')
        await database.ts().create(key, labels=labels)
    else:
        logging.error(f'Found wrong key {key} with type: {res}')
        return None

    return key
