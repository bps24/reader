import pandas

def ml_to_payout(value):
    value = float(value)
    if value < 0: return 1 + -100.0 / value
    elif value > 0: return 1 + value / 100 
    else: raise Exception("0 passed as ML")

def ml_to_prop(value):
    value = float(value)
    if value < 0: return value / (value - 100.0)
    elif value > 0: return 100 / (value + 100) 
    else: raise Exception("0 passed as ML")

