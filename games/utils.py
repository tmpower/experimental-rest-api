from games.models import User
from flask import abort

# import time
# from functools import wraps

# from flask import request, jsonify
# import redis

# r = redis.StrictRedis(host='localhost', port=6379, db=0)

# def ratelimit(limit=10, interval=60, shared_limit=True, key_prefix="rl"):
#     def rate_limit_decorator(f):
#         @wraps(f)
#         def wrapper(*args, **kwargs):
#             t = int(time.time())
#             closest_minute = t - (t % interval)
#             if shared_limit:
#                 key = "%s:%s:%s" % (key_prefix, request.remote_addr, closest_minute)
#             else:
#                 key = "%s:%s:%s.%s:%s" % (key_prefix, request.remote_addr,
#                                           f.__module__, f.__name__, closest_minute)
#             current = r.get(key)

#             if current and int(current) > limit:
#                 retry_after = interval - (t - closest_minute)
#                 resp = jsonify({
#                     'code': 429,
#                     "message": "Too many requests. Limit %s in %s seconds" % (limit, interval)
#                 })
#                 resp.status_code = 429
#                 resp.headers['Retry-After'] = retry_after
#                 return resp
#             else:
#                 pipe = r.pipeline()
#                 pipe.incr(key, 1)
#                 pipe.expire(key, interval + 1)
#                 pipe.execute()

#                 return f(*args, **kwargs)
#         return wrapper
#     return rate_limit_decorator


def abort_if_no_auth(token):
    user = User.verify_auth_token(token)
    if user is None:
        abort(401)