import math

def solve_math(expression):
    try:
        allowed = {"__builtins__": None}
        result = eval(expression, allowed, math.__dict__)
        return str(result)
    except Exception:
        return "I couldn't solve that."