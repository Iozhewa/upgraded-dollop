#!/usr/bin/env python3
import Timer
import Interpreter
import pandas as pd  # Useful DataFrames
import numpy as np  # Useful arrays
import matplotlib.pyplot as plt  # Creates graphs

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

    def chart(self):
        timer = Timer()
        timer.elapse()
        self.data.plot(kind='scatter', x=self.__xAxis, 
                       y=self.__yAxis, s=5)
        plt.xticks = self.__xTicks
        plt.yticks = self.__yTicks
        plt.savefig(self.destination)
        plt.show()

        print(f"Task completed in {round(timer.elapse(), 3)} seconds")
        return
    
if __name__ == "__main__":
    print(".")
    path = "upgraded-dollop/Round9-Runs1to15/B2356raw2.dat"  # Spyder reads relative links differently
    interpreter = Interpreter(filepath=path)
    print(interpreter.summary())

    plotter = Plotter(interpreter.labels, interpreter.data)
    print(plotter)
    plotter.chart()