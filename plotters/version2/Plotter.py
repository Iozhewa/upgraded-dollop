# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 2026

@author: Yoshi
"""

import time  # See Timer class
import pandas as pd  # See Plotter class
import numpy as np
import matplotlib.pyplot as plt

class Timer:
    '''
    When insantiated, can begin recording time of execution via timer.elapse()
    '''
    def __init__(self):
        self.click:int = 0  # Toggle
        self.initial:float = 0.0  # ms value
        self.final:float = 0.0

    def elapse(self) -> float:
        '''
        Call once to begin timing latency, and call again to return elapsed time.
        '''
        if self.click == 0:
            self.initial = time.time()
            self.click += 1
        else:  # imperative programming trick
            self.final = time.time()
            return round(self.final - self.initial, 3)  # for time complexity evaluation, 3 d.p. is sufficient

class Interpreter:
    def __init__(self, filepath):
        pass