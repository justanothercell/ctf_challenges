import math
from copy import deepcopy

g = {}
exec("print('Welcome to the calculator!')", g, {})
eval = g['__builtins__']["eval"]
input = g['__builtins__']["input"]
del g['__builtins__']["open"]
del g['__builtins__']["exec"]
del g['__builtins__']["eval"]
del g['__builtins__']["input"]

while True:
    try:
        i = input(':').replace('"', '').replace('\'', '').replace('py', '').strip()
        if len(i) > 0:
            print(eval(i, g, {**math.__dict__}))
    except Exception as e:
        print(f'Error: {e}')
