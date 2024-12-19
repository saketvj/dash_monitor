import time 
import random
import threading



#1.  Write a decorator that measures execution time of a function. It logs the time taken, function name and arguments used.


# def dec_fun1(fun_to_be_decorated):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         ans = fun_to_be_decorated(*args,**kwargs)
#         end = time.time()
#         print( f"{fun_to_be_decorated.__name__} with arguments = {args,kwargs} has execution time = {end-start}  ")
#         return ans
#     return wrapper

# @dec_fun1
# def foo(a,b):
#     time.sleep(1)
#     return a+b


# print(foo(2,43))


# 2.  Write a decorator that logs functions details when the function fails for some reason.

def dec_fun2(fun_to_be_decorated):
    def wrapper(*args,**kwargs):
        try:
            return fun_to_be_decorated(*args,**kwargs)
        except Exception as e:
            print(f"Function name = {fun_to_be_decorated.__name__}")
            print(f"Arguments  = {args,kwargs}")
            print(f"Error = {e} ")
    return wrapper


@dec_fun2
def demo(a,b):
    return a/b

print(demo(3,0))


#3.  Write a decorator that retries a function if an exception is thrown. Add back off feature too.

# def dec_fun3(fun_to_be_decorated):
#     def wrapper(*args,**kwargs):
#         try:
#             print(fun_to_be_decorated(*args,**kwargs))
#         except Exception as e:
#             print(e)
#             print(time.time())
#             if attempts ==0:
#                 print(e)
#             else:
#                 time.sleep(delay_time)
#                 wrapper(*args,delay_time =delay_time*2,attempts=attempts-1)


#             attempts = 10
#             delay_time = 1
#             if attempts:
#                 while attempts:
#                     print(fun_to_be_decorated(*args,**kwargs))
#                     attempts = attempts - 1
#                     time.sleep(delay_time)
#                     print(attempts)
#                     delay_time = delay_time*2
#             else :
#                 print(e)
#             # i = i*2
#     return wrapper


# @dec_fun3
# def demo(a,b):
#     with open("a","r") as f:
#         content = f.read()
#     return content

# demo(3,0)  


#4. Write a function that returns it's  results for n times before re running itself again. then for the next n times it returns this new result before running itself again. Generator, normal function, decorator etc.




# wrtie a gen that generate fib num

# def fib(n):
#     a, b = 1, 1
#     for 
#     a, b = b, a + b

# write a fun(generator) that can generate infinte fib number. (generator)


