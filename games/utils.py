from games.models import User
from flask import abort, current_app


def abort_if_no_auth(token):
    user = User.verify_auth_token(token)
    if user is None:
        abort(401)


import time
from functools import wraps

from flask import jsonify, request
import redis


r = redis.StrictRedis(host='redis', port=6379, db=0) # redis host from docker-compose.yml

def ratelimit(request_limit=10, time_interval=60, shared_limit=True, key_prefix="rl"):
    def rate_limit_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            t = int(time.time())
            closest_minute = t - (t % time_interval)
            if shared_limit:
                key = "%s:%s:%s" % (key_prefix, request.remote_addr, closest_minute)
            else:
                key = "%s:%s:%s.%s:%s" % (key_prefix, request.remote_addr,
                                          f.__module__, f.__name__, closest_minute)
            current = r.get(key)

            if current and int(current) > request_limit:
                retry_after = time_interval - (t - closest_minute)
                resp = jsonify({
                    'code': 429,
                    "message": "Too many requests. Limit %s in %s seconds" % (request_limit, time_interval)
                })
                resp.status_code = 429
                resp.headers['Retry-After'] = retry_after
                return resp
            else:
                pipe = r.pipeline()
                pipe.incr(key, 1)
                pipe.expire(key, time_interval + 1)
                pipe.execute()

                return f(*args, **kwargs)
        return wrapper
    return rate_limit_decorator


# import time
# from functools import update_wrapper
# from flask import request, g

# from redis import Redis
# redis = Redis()

# class RateLimit(object):
#     expiration_window = 10

#     def __init__(self, key_prefix, limit, per, send_x_headers):
#         self.reset = (int(time.time()) // per) * per + per
#         self.key = key_prefix + str(self.reset)
#         self.limit = limit
#         self.per = per
#         self.send_x_headers = send_x_headers
#         p = redis.pipeline()
#         p.incr(self.key)
#         p.expireat(self.key, self.reset + self.expiration_window)
#         self.current = min(p.execute()[0], limit)

#     remaining = property(lambda x: x.limit - x.current)
#     over_limit = property(lambda x: x.current >= x.limit)

# def get_view_rate_limit():
#     return getattr(g, '_view_rate_limit', None)

# def on_over_limit(limit):
#     return 'You hit the rate limit', 429

# def ratelimit(limit, per=300, send_x_headers=True,
#               over_limit=on_over_limit,
#               scope_func=lambda: request.remote_addr,
#               key_func=lambda: request.endpoint):
#     def decorator(f):
#         def rate_limited(*args, **kwargs):
#             key = 'rate-limit/%s/%s/' % (key_func(), scope_func())
#             rlimit = RateLimit(key, limit, per, send_x_headers)
#             g._view_rate_limit = rlimit
#             if over_limit is not None and rlimit.over_limit:
#                 return over_limit(rlimit)
#             return f(*args, **kwargs)
#         return update_wrapper(rate_limited, f)
#     return decorator

# @current_app.after_request
# def inject_x_rate_headers(response):
#     limit = get_view_rate_limit()
#     if limit and limit.send_x_headers:
#         h = response.headers
#         h.add('X-RateLimit-Remaining', str(limit.remaining))
#         h.add('X-RateLimit-Limit', str(limit.limit))
#         h.add('X-RateLimit-Reset', str(limit.reset))
#     return response
