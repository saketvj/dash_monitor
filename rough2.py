import time
import random
import threading
import logging


logger = logging.getLogger(__name__)

logging.basicConfig(encoding='utf-8', level=logging.INFO)

# def dec_fun1(fun_to_be_decorated):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         ans = fun_to_be_decorated(*args,**kwargs)
#         end = time.time()
#         print("Ac")
#         print( f"{fun_to_be_decorated.__name__} with arguments = {args,kwargs} has execution time = {end-start}  ")
#         return ans
#     return wrapper

# @dec_fun1
# def foo(a,b):
#     time.sleep(1)
#     return a+b

# print(foo(2,43))

# this decorator takes the functionilities that need to be monitored:
# incudes start-time,end-time,execution-time,caching,function name and arguments,retry with backoff,progress-tracking,Error-logging.




# 3. WRITE A DECORATOR THAT RETIES A FUNCTION IF AN EXCEPTION IS THROWN ADD BACK OFF FEATURE TOO
# ARG FROM USER : - BACKOFF TIME ,NO.OF ATTEMPTS AFTER IT FINALLY THROW THE ERROR.

# def callback():
#     print("result of callback..")

# def retry_with_backoff(attempts =10,backoff = 1,delay = 2,callback_func = None):
#     def wrapper1(fun_to_be_dec,):
#         def wrapper2(*args,**kwargs):
#             # inital waittime equals the delay provided by the user.
#             waittime = delay
#             for attempt in range(0, attempts):
#                 try:
#                     logger.info(f"attempt no. =  {attempt}" )
#                     logger.info(f"wait time = {waittime}")
#                     return fun_to_be_dec(*args, **kwargs)
#                 except Exception as e:
#                     logger.error(e)
#                     time.sleep(waittime)
#                     waittime = backoff*waittime
#                     if attempt < attempts-1:
#                         continue
#                     logger.critical(f"Final error is:{e}")
#                     callback_func()
#                     raise e
#         return wrapper2
#     return wrapper1


# @retry_with_backoff(attempts=5, backoff = 1.5,delay = 1,callback_func = callback)
# def div(a,b):
#     return a/b


# log levels
# show output error
# Every attempt should show the error
#  

# print(div(10,0))


# 4.Write a function that return its results for n times before re reunning itself again then for
#  the next n times it return this new result before rerunning itself function decorator.


# def return_multiple_time(fun_to_be_decorated):
#     def wrapper(*args, **kwargs):
#     #repeat: if repeat n then this function return the same result for n times.
#     #rerun if rerun = m then this fucntion reruns itself for m times.
#         repeat= kwargs.get("repeat", 5)
#         rerun = kwargs.get("rerun", 5)
#         for i in range (0,rerun):
#             a = fun_to_be_decorated(*args, **kwargs)
#             for i in range(0, repeat):
#                 yield a

#     return wrapper


# @return_multiple_time
# def add(a,b,**kwargs):
#     return random.randint(a,b)


# gen = add(1,9,repeat = 3, rerun = 3)

# for num in gen:
#     print(num)

# for i in range(10):
    # print(add(1,3))

# 5.)
# fib series using generator

# def fibo(num):
#     a, b = 1, 1
#     for i in range(0, num):
#         yield a
#         a, b = b, a + b

# gen = fibo(7)
# for num in gen:
#     print(num)

# 6.)
# fib for infinte size 

# def fibo_infinte():
#     a, b = 1, 1
#     while 1:
#         yield a
#         a, b = b, a + b

# gen = fibo_infinte()

# for i in range(0,4):
#     print(next(gen))




# Write a decorator func that caches the result for the arguments and if function is called with same arguments then it will return the cached results.

from collections import defaultdict

def cache(func_to_be_decorated):
    cache = defaultdict(tuple)
    def wrapper(*args,**kwargs):
        
        my_key = tuple(list(args)+list(kwargs.items()))

      
        if my_key in cache:
            return cache[my_key]
        else:
            cache[my_key] = func_to_be_decorated(*args,**kwargs)
            return cache[my_key]

    return wrapper


@cache
def foo(a,b,c):
    print("First time")
    return f" Hello {a} , Hello {b}, Hello {c}" 


results = foo("Saket", "Jini", c = "Vj")
ans = foo("Saket", "Jini", c = "Vj")
print(results)
print(ans)
