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

class Plotter:
    '''
    Provides PyPlot representation of DAT in dictionaries, having been turned into Pandas DataFrames.
    '''
    def __init__(self, measures, data:dict[str, list[float]], destination):
        self.measures:list[str] = measures
        self.data:object = pd.DataFrame(data)
        self.destination:str = destination
        self.__xAxis:str = self.measures[0]
        self.__yAxis:str = self.measures[1]
        self.__xTicks:object = np.arange(0, 10, 2)
        self.__yTicks:object = np.arange(0, 10, 2)
    def __str__(self):
        return f"Plotter(measures={','.join(self.measures)})"

    def setAxis(self, x:str, y:str) -> None:
        '''
        OOP-concious method of adjusting private axis attributes.
        '''
        self.__xAxis = x
        self.__yAxis = y
        return
    def setTicks(self, x:object, y:object) -> None:
        '''
        OOP-concious method of adjusting private ticks attributes.
        '''
        self.__xTicks = x
        self.__yTicks = y
        return

    def chart(self, title:str):
        '''
        Given a title, generates a scatter plot based on title and the following attributes:
        data, axis (x and y), and ticks (x and y). A file is saved based on destination attribute.
        The latency of the Plotter code is measured and printed out. 
        '''
        timer = Timer()
        timer.elapse()
        ax = self.data.plot(kind='scatter', x=self.__xAxis, y=self.__yAxis, s=0.001)
        ax.set_title(title)
        ax.set_xticks(self.__xTicks, labels=[x for x in self.__xTicks])
        ax.set_yticks(self.__yTicks, labels=[y for y in self.__yTicks])
        ax.set_xlim(min(self.__xTicks), max(self.__xTicks))
        ax.set_ylim(min(self.__yTicks), max(self.__yTicks))
        plt.savefig(self.destination)
        plt.show()

        print(f"Plotting completed in {round(timer.elapse(), 3)} seconds")
        return

if __name__ == "__main__":
    print("Hello, world!")