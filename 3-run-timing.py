# EXERCISE 3 ■ Run timing

# Write a function (run_timing) that asks how long it took for you to run 10 km.
from decimal import *


def run_timing():
    current_time = Decimal(input('Enter 10 km run time: '))
    times = []
    while current_time:
        current_time = Decimal(current_time)
        times.append(current_time)
        current_time = (input('Enter 10 km run time: '))
        
    avg_run = sum(times) / len(times)
    return(f'Average of {avg_run}, over {len(times)} runs')


print(run_timing())

# Write a function that takes a float and two integers (before and after). The
# function should return a float consisting of before digits before the decimal
# point and after digits after.

def float_cutter(float_num, before, after):
    before, after = int(before), int(after)
    float_str = str(float_num)
    float_cut = float_str.split('.')

    before_new = float_cut[0][(len(float_cut[0]) - before):]
    after_new = float_cut[1][:after]

    float_new = float(f'{before_new}.{after_new}')

    return float_new

print(float_cutter(1234.56789, 3, 4))



