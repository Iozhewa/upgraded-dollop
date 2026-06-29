#!/usr/bin/env python3
from Timer.py import Timer

class Interpreter:
    def __init__(self, filepath):
        self.filepath:str = filepath
        self.runtime:float = 0.0
        self.labels:list[str] = []
        self.data:dict[str, list[float]] = []
    
    def __str__(self):
        return f"Interpreter(path={self.filepath})"
    
    def __parse(self, max_index, index_interval) -> bool:
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
    
    def summary(self, max, interval) -> str:
        self.__parse(max_index=max, index_interval=interval)
        return f'''{'-'*25}
Interpreter opened '{self.filepath}' with the following measures:
{', '.join(self.labels)}
Parsing completed in {self.runtime} seconds.
{'-'*25}'''