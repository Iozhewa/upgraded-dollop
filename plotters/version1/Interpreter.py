#!/usr/bin/env python3
import time

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
        self.header:list[str] = []
        self.data:dict[str, list[float]] = []
    def __str__(self):
        return f"Interpreter(path={self.filepath})"
    
    def __parse(self) -> None:
        try:
            timer = Timer()
            timer.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
        except FileNotFoundError:
            print(f"Interpreter: Could not find '{self.filepath}'")
        except Exception as e:
            print(f"Interpreter: Unknown error '{e}'")
        else:
            self.header = lines[1].split(';')
            #  lines[0] has not been designated a variable yet
            acronyms:list[str] = [entry for entry in lines[2].split()]
            self.data = {a: [] for a in acronyms}

            for line in lines[2:]:
                for index, datapoint in enumerate(line.split()):
                    key:str = acronyms[index]
                    self.data[key].append(datapoint)
            self.runtime = timer.elapse()
            return
    
    def summary(self) -> str:
        self.__parse()
        return f'''{'-'*25}
Interpreter opened '{self.filepath}' with the following information:
{' \n'.join(self.header)}
Parsing completed in {self.runtime} seconds.
{'-'*25}'''

if __name__ == "__main__":
    print(".")
    path = r"plotters\version1\B2356raw2.dat"
    inter = Interpreter(path)
    print(inter.summary())
