#!/usr/bin/env python3
import time
import pandas as pd  # Useful DataFrames
import numpy as np  # Useful arrays
import matplotlib.pyplot as plt  # Creates graphs
'''
Stage 1: Transient Replications

Goal: Replicate figure 1.1, 1.2, 1.3 (3/6)
1.1 - V (mph) [-5, 0, 5, ... 30] v. ET (sec) [0, 200, 400, ... 1000]
    Update... Ticks won't work, the DataFrame itself has to be restricted.
1.2 - FZ (lb) [-400, -300, ... 0] v. ET (sec) [0, 200, 400, ... 1000]
1.3 - IA (deg) [-1, 0, 1, ... 4] v. ET (sec) [0, 200, 400, ... 1000]

Stage 2: Cornering Replications

Stage 3: Drive/Brake Replications
'''

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

class Interpreter:
    def __init__(self, filepath):
        self.filepath:str = filepath
        self.runtime:float = 0.0
        self.labels:list[str] = []
        self.data:dict[str, list[float]] = []
    
    def __str__(self):
        return f"Interpreter(path={self.filepath})"
    
    def __parse(self, keyMeasure, roundTo) -> bool:
        try:
            timer = Timer()
            timer.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
        except FileNotFoundError:
            print(f"Interpreter: Could not find {self.filepath}")
            return False
        except Exception as e:
            print(f"Interpreter: Unknown error {e}")
            return False
        else:
            self.labels:list[str] = [entry for entry in lines[1].split()]
            self.data = {l: [] for l in self.labels}
            for line in lines[3:]:
                refPoint:int = self.labels.index(keyMeasure)
                parseRef = float(line.split()[refPoint])
                if abs(parseRef - round(parseRef, roundTo)) < 1e-6:
                    for index, point in enumerate(line.split()):
                        key:str = self.labels[index]
                        self.data[key].append(float(point))
            self.runtime = timer.elapse()
            return True
    
    def summary(self, measure, rounder) -> str:
        self.__parse(measure, rounder)
        return f'''{'-'*25}
Interpreter opened '{self.filepath}' with the following measures:
{', '.join(self.labels)}
Parsing completed in {self.runtime} seconds.
{'-'*25}'''

class Plotter:
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
        ax = self.data.plot(kind='scatter', x=self.__xAxis, 
                       y=self.__yAxis, s=0.001)
        ax.set_title("Title")
        ax.set_xticks(self.__xTicks, labels=[x for x in self.__xTicks])
        ax.set_yticks(self.__yTicks, labels=[y for y in self.__yTicks])
        ax.set_xlim(min(self.__xTicks), max(self.__xTicks))
        ax.set_ylim(min(self.__yTicks), max(self.__yTicks))
        plt.savefig(self.destination)
        plt.show()

        print(f"Plotting completed in {round(timer.elapse(), 3)} seconds")
        return
    
if __name__ == "__main__":
    print(".")
    path = "upgraded-dollop/plotters/version2/A2356raw2.dat"  # Spyder reads relative links differently
    interpreter = Interpreter(filepath=path)
    print(interpreter.summary(measure="ET", rounder=4))

    plotter = Plotter(interpreter.labels, interpreter.data,
                      destination="upgraded-dollop/plotters/version2/transient1-1.png")
    plotter.setAxis(x="ET", y="V")
    plotter.setTicks(x=np.arange(0, 1100, 200), y=np.arange(-5, 35, 5))
    plotter.chart()
