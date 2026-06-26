#!/usr/bin/env python3
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
Planning to add plotting features based on: https://www.w3schools.com/python/pandas/pandas_plotting.asp
Can't remember when I would use NumPy: https://www.w3schools.com/python/numpy/default.asp

Yes, this version only exists because I need to run it on Spyder. I do still want to validate my dev work on VSCode

Note other project: Parser factory with official Motec datasheet
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
    
    def __parse(self) -> None:
        try:
            timer = Timer()
            timer.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
                print(len(lines[1].split()))
                print(len(lines[2].split()))
                print(len(lines[3].split()))
        except FileNotFoundError:
            print(f"Interpreter: Could not find '{self.filepath}'")
        except Exception as e:
            print(f"Interpreter: Unknown error '{e}'")
        else:
            self.labels:list[str] = [entry for entry in lines[1].split()]
            self.data = {l: [] for l in self.labels}
            for index, line in enumerate(lines[3:]):
                if index > 70000: break  # 79864 --> 80,000
                if index % 500 == 0:  # 8000 * 10 = 'tenths'
                    for index, datapoint in enumerate(line.split()):
                        key:str = self.labels[index]
                        self.data[key].append(datapoint)
            self.runtime = timer.elapse()
            return
    
    def summary(self) -> str:
        self.__parse()
        return f'''{'-'*25}
Interpreter opened '{self.filepath}' with the following measures:
{', '.join(self.labels)}
Parsing completed in {self.runtime} seconds.
{'-'*25}'''

class Plotter:
    def __init__(self, series, data):
        self.series:list[str] = series
        self.data:object = pd.DataFrame(data)
    def __str__(self):
        return f"Plotter(series={','.join(self.series)})"
    
    def chart(self):
        timer = Timer()
        timer.elapse()
        self.data.plot(kind='scatter', x='ET', y='AmbTmp')
        plt.yticks(np.arange(0, 50, 3))
        plt.xticks(np.arange(0, 150, 25))
        plt.show()
        print(f"Task completed in {round(timer.elapse(), 3)} seconds")
        return

if __name__ == "__main__":
    print(".")
    path = "upgraded-dollop/Round9-Runs1to15/B2356raw2.dat"  # Spyder reads relative links differently
    inter = Interpreter(path)
    print(inter.summary())
    
    #[print(k, len(inter.data[k]), inter.data[k][0:5]) for k in inter.data]
    plott = Plotter(inter.labels, inter.data)
    print(plott)
    plott.chart()
