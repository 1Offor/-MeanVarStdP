from mean_var_std import calculate

# Test with an example list
try:
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)
except ValueError as e:
    print(e)