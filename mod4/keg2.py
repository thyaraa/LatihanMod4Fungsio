def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def say_hi():
    return 'hello there'

result = say_hi()
print(result)  


# import time

# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
#         return result
#     return wrapper

# @timing_decorator
# def slow_function():
#     time.sleep(2)
#     print("Function executed.")

# slow_function()

