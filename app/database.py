import redis


async def get_redis_session():
    redis_session = redis.Redis(host='localhost', port=6379, db=0)
    try:
        yield redis_session
    finally:
        redis_session.close()
