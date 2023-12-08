import redis.asyncio as redis


async def write(redis_pool):
    redis_client = redis.StrictRedis(connection_pool=redis_pool)
    await redis_client.set(name="fake1", value=1)
    await redis_client.set(name="fake2", value=1)
    await redis_client.close(close_connection_pool=False)

