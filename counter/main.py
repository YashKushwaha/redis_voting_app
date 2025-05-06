import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)
pubsub = r.pubsub()
pubsub.subscribe('votes')

print("Counter listening for votes...")
for message in pubsub.listen():
    if message['type'] == 'message':
        option = message['data']
        key = f"count:{option}"
        r.incr(key)
        print(f"Vote counted for {option}")