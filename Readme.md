# 개요
redis 캐시 연습

# 준비
* redis
```shell
# docker로 redis실행
docker run -d --rm -p 6379:6379 --name redis-test redis:7.0.9
```

# 실행방법
```shell
cd app
pip install requirements.txt
uvicorn main:app --host 127.0.0.1 --port 30000 --reload
```

# 로드 테스트
```shell
cd load_test
pip install locust
locust -f locustfile.py --host=http://127.0.0.1:30000 --web-host=127.0.0.1 --web-port=12000
```
