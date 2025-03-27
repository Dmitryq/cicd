import redis
from flask import Flask

app = Flask(__name__)
redis_hits = redis.Redis(host='redis', port=6379)


def get_hit_count():
  try:
    return redis_hits.incr('hits')
  except redis.exception.ConnectionError as e:
    raise e

@app.route('/')
def hello():
  count = get_hit_count()
  return f"Эту страницу посетили {count} раз/а.\n"


