def f(*args, **kwargs):
   print('args:', args, 'kwargs:', kwargs)

f('a')
# args: ('a',) kwargs: {}
f(ar='a')
# args: () kwargs: {'ar': 'a'}
f(1,2,param=3)
# args: (1, 2) kwargs: {'param': 3}