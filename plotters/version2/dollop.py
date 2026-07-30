#!/usr/bin/env/python3
import pandas as pd  # For DataFrames and organized data
import numpy as np  # Arrays for efficiency... maybe
import matplotlib.pyplot as pltt  # Creates graphs
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

class Handler:
    def __init__(self, path):
        self.path:str = path
        self.runtime:float = 0.0
        self.metadata:tuple[str] = ()
        self.metrics:tuple[str] = ()
        self.logbook:dict[str, float] = {}
    def __str__(self):
        return f"Handler(path={self.path})"

    def parse(self) -> None:
        with open(self.path, 'r') as reader:
            timer = Timer()
            timer.elapse()
            lines:list[str] = reader.readlines()
            self.metadata =  [char.strip() for char in lines[0].split(';')]
            self.metric =  [char.strip() for char in lines[1].split('\t')]
            # ignore units at lines[2], unaligned with remaining lines
        test = [char.strip() for char in lines[3].split('\t')]
        [print(line, test[i]) for i,line in enumerate(self.metrics)]

        self.runtime = timer.elapse()

    def results(self) -> str:
        return f'''{'-'*25}
Handler opened '{self.filepath}' with the following metadata:
\t{','.join(self.metadata)}
and the following metrics:
\t{','.join(self.metrics)}
Processed in {self.runtime} seconds'''

class Plotter:
    def __init__(self, measures, destination, data:dict[str, list[float]]):
        self.measures:list[str] = measures
        self.destination:str = destination
        self.data:object = pd.DataFrame(data)
        self.__xAxis:str = self.measures[0]
        self.__yAxis:str = self.measures[1]
        self.__xTicks:object = np.arange(0, 10, 2)
        self.__yTicks:object = np.arange(0, 10, 2)
    def __str__(self):
        return f"Plotter(measures={','.join(self.measures)})"

    def setAxis(self, x:str, y:str) -> None:
        self.__xAxis = x
        self.__yAxis = y
        return

    def setTicks(self, x:object, y:object) -> None:
        self.__xTicks = x
        self.__yTicks = y
        return

    def chart(self) -> None:
        timer = Timer()
        timer.elapse()
        # TODO

        print(f"Plotting completed in {round(timer.elapse(), 3)} seconds")
        return

if __name__ == "__main__":
    print(".")
    handler = Handler(path=r"plotters\version2\A2356raw2.dat")
    handler.parse()