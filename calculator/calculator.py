import math

g = globals()
del g['__builtins__'].open
del g['__builtins__'].exec
del g['__builtins__'].eval

while True:
    try:
        i = input(':').replace('"', '').replace('\'', '').replace('py', '').strip()
        if len(i) > 0:
            print(eval(i, g, {**math.__dict__}))
    except Exception as e:
        print(f'Error: {e}')
