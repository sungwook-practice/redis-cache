from fastapi import APIRouter, Depends
from database import get_redis_session
import httpx
import redis
import json


router = APIRouter(
  prefix="/posts",
)


@router.get('')
def get_posts():
  """get posts"""
  response = httpx.get("https://jsonplaceholder.typicode.com/posts")
  return response.json()


@router.get('/{id}')
async def get_post(id: int, redis_session: redis.Redis = Depends(get_redis_session)):
  """get post by id"""
  post = None

  try:
    post = redis_session.get(id)
  except (redis.exceptions.ConnectionError,
          redis.exceptions.TimeoutError,
          redis.exceptions.ResponseError):
  # redis 장애로 간주
    pass

  if post:
    return post

  # cache hit을 하지 못한 경우 직접 API 호출
  cache_ttl = 20
  cache_key = f"post:{id}"

  async with httpx.AsyncClient() as client:
    response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    post = response.json()

  # write cache with TTL
  # raise Invalid input of type: 'dict'. Convert to a bytes, string, int or float first..
  redis_session.set(cache_key, json.dumps(post), ex=cache_ttl)

  return post
