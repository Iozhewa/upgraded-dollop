#!/usr/bin/env python3
import time  # Measures time complexity

class Timer:
    def __init__(self):
        self.click:int = 0
        self.initial:float = 0.0
        self.final:float = 0.0
    
    def elapse(self) -> float:
        if self.click == 0:
            self.initial = time.time()
            self.click += 1
        else:
            self.final = time.time()
            return round(self.final - self.initial, 3)

'''
Use case:

import Timer

timer = Timer()
timer.elapse()
#  TODO
runtime:float = timer.elapse()
print(f"Accessing Timer class took {runtime} seconds.")
'''