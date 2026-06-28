import Timer
import pandas as pd  # Useful DataFrames
import numpy as np  # Useful arrays
import matplotlib.pyplot as plt  # Creates graphs

class Interpreter:
    def __init__(self, filepath):
        self.filepath:str = filepath
        self.runtime:float = 0.0
        self.labels:list[str] = []
        self.data:dict[str, list[float]] = []
    
    def __str__(self):
        return f"Interpreter(path={self.filepath})"
    
    def __parse(self) -> bool:
        try:
            timer = Timer()
            timer.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
        except FileNotFoundError:
            print(f"Interpreter: Could not find {self.filepath}")
        except Exception as e:
            print(f"Interpreter: Unknown error {e}")
        else:
            pass