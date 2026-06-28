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
        self.__yAxis = self.measures[0]
        self.__xAxis = self.measures[1]
        self.__yTicks = np.arange(0, 50, 3)
        self.__xTicks = np.arange(0, 150, 25)
    
    def __str__(self):
        return f"Plotter(measures={','.join(self.measures)})"

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
    # TODO