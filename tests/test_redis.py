
from unittest.mock import patch

import fakeredis.aioredis as fakeredis
import redis.asyncio as redis

import pytest

import app


@pytest.mark.asyncio
@pytest.fixture(autouse=True)
async def before_and_after_test(pytestconfig):
    fake = fakeredis.FakeRedis()
    redis_patch1 = patch("redis.asyncio.StrictRedis")
    redis_mock1 = redis_patch1.start()
    redis_mock1.return_value = fake

    yield

    redis_mock1.stop()
    await fake.flushall()

@pytest.mark.asyncio
async def test_redis():
    redis_client = fakeredis.FakeRedis()
    await app.write(redis_client.connection_pool)
    await redis_client.close()
