# 개요
redis 캐시 연습

# 준비
* redis
```shell
# docker로 redis실행
docker run -d -p 6379:6379 --name redis-test redis:7.0.9
```

# 실행방법
```shell
cd app
pip install requirements.txt
uvicorn main:app --host 127.0.0.1 --port 30000 --reload
```
