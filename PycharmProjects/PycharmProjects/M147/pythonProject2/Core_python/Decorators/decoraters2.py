from time import sleep,time

def measure_time(func):
    def inner(*args,**kwargs):
        startpoint = time()
        res = func(*args,**kwargs)
        endpoint = time()
        print(f'execution time of function {func.__name__}:{endpoint-startpoint}')
        return res
    return inner
@measure_time
def mul(a,b,c):
    sleep(5)
    return a*b*c
print(mul(10,20,2))
#execution time of function mul:5.000744581222534
#400

# keeps track of func name and number of times it is being called

count = {}
def _count(func_name):
    if func_name in count:
        count[func_name]+=1
    else:
        count[func_name] = 1

def count_calls(func):
    def wrapper(*args,**kwargs):
        _count(func.__name__)
        return func(*args,**kwargs)
    return wrapper

def max_call(func):
    def wrapper(*args):
        _count(func.__name__)
        if count[func.__name__]>5:
            raise ValueError('max call exceeds which is 5')
        return  func(*args)
    return wrapper

@max_call
def greet():
    return 'hello world'
@max_call
def greeting(name):
    return f'hello {name}'
@max_call
def add(a,b):
    return a+b
@max_call
def sub(a,b):
    return a-b
@max_call
def mul(a,b,c):
    return a*b*c
# -------------------------------------------------------------------------

