#!/usr/bin/env python3
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

class Parser:
    '''
    Provides dictionary access to DAT files.
    '''
    def __init__(self, filepath):
        self.filepath:str = filepath
        self.runtime:float = 0.0
        self.labels:list[str] = []
        self.data:dict[str, list[float]] = []
    def __str__(self):
        return f"Parser(path={self.filepath})"

    def __parse(self, keyMeasure, roundTo) -> bool:
        '''
        Private function defining the following attributes: labels, data, runtime.
        Helper function of summary().
        '''
        try:
            timer = Timer()
            timer.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
        except FileNotFoundError:
            print(f"Parser: Could not find {self.filepath}")
            return False
        except Exception as e:
            print(f"Interpreter: Unknown error {e}")
            return False
        else:
            self.labels:list[str] = [entry for entry in lines[1].split()]
            self.data = {l : [] for l in self.labels}
            for line in lines[3:]:
                refPoint:int = self.labels.index(keyMeasure)
                refParse = float(line.split()[refPoint])
                if (abs(refParse - round(refParse, roundTo)) < 1e-6):
                    for index, point in enumerate(line.split()):
                        key:str = self.labels[index]
                        self.data[key].append(float(point))
            self.runtime = timer.elapse()  # Evidently begging O(n^2) impl isn't significant to overall latency
            return True

    def summary(self, measure, rounder) -> str:
        '''
        Given something to extract from a DAT file and the decimal values it must run to,
        reports the success or failure to read a DAT file in order to construct a local dictionary. 
        '''
        if (self.__parse(measure, rounder)):
            return f'''{'-'*25}\nParser opened '{self.filepath}' with the following measures:
{', '.join(self.labels)}\nParsing completed in {self.runtime} seconds.\n{'-'*25}'''
        else:
            return f"{'-'*25}\nParser failed to create dictionary with subset of DAT values.\n{'-'*25}"

if __name__ == "__main__":
    print("Hello, world!")