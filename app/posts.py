from fastapi import APIRouter
import httpx


router = APIRouter(
  prefix="/posts",
)


@router.get('')
def get_posts():
    """get posts"""
    response = httpx.get("https://jsonplaceholder.typicode.com/posts")
    return response.json()


# get post from id
@router.get('/{id}')
def get_post(id: int):
    """get post from id"""
    response = httpx.get(f"https://jsonplaceholder.typicode.com/posts/{id}")
    return response.json()
