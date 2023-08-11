"""
Tests for the DB operations.
"""
import logging

import pytest
import redis.asyncio as redis

import db


@pytest.fixture(autouse=True)
def test_db(mocker):
    mocker.patch('db.database', redis.Redis(host='test_redis', db=0))


async def test_create_new_ts_key_successful():
    """Test creating new TS key is successful."""

    await db.database.set('test1', 'test')
    # db.database.set('test2', 'test')

    test_key = await db.get_or_create_ts_key(labels={'test': 'test'})
    # logging.debug(test_key)
    assert test_key == f'{db.KEY_PREFIX}:test'

    assert await db.database.get("test1") == b'test'

#
# async def test_returning_existing_ts_key():
#     """Test returning existing TS key trying to create a new key with the same name."""
#     key = f'{db.KEY_PREFIX}:test'
#     labels = {
#         'test': 'test',
#         'old_key': 'true'
#     }
#     res = db.database.ts().create(key, labels=labels)
#
#     test_key = await db.get_or_create_ts_key(labels={'test': 'test'})
#     logging.debug(test_key)
#     assert test_key == key
#
#     # assert redis_my.get("test1") == 1
#
#
# async def test_returning_existing_ts_key1():
#     """Test returning existing TS key trying to create a new key with the same name."""
#     key = f'{db.KEY_PREFIX}:test'
#     labels = {
#         'test': 'test',
#         'old_key': 'true'
#     }
#     res = db.database.ts().create(key, labels=labels)
#
#     test_key = await db.get_or_create_ts_key(labels={'test': 'test'})
#     logging.debug(test_key)
#     assert test_key == key

# assert redis_my.get("test1") == 1
