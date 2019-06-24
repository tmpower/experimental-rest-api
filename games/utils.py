from games.models import User
from flask import abort

# import redis
# from flask import g

# def ratelimit(requests=100, window=60, by="ip", group=None):
#     if not callable(by):
#         by = { 'ip': lambda: request.headers.remote_addr }[by]

#     def decorator(f):
#         @functools.wraps(f)
#         def wrapped(*args, **kwargs):
#             group = group or request.endpoint
#             key = ":".join(["rl", group, by()])

#             try:
#                 remaining = requests - int(redis.get(key))
#             except (ValueError, TypeError):
#                 remaining = requests
#                 redis.set(key, 0)

#             ttl = redis.ttl(key)
#             if not ttl:
#                 redis.expire(key, window)
#                 ttl = window

#             g.view_limits = (requests,remaining-1,time()+ttl)

#             if remaining > 0:
#                 redis.incr(key, 1)
#                 return f(*args, **kwargs)
#             else:
#                 return Response("Too Many Requests", 429)
#         return wrapped
#     return decorator


def abort_if_no_auth(token):
    user = User.verify_auth_token(token)
    if user is None:
        abort(401)