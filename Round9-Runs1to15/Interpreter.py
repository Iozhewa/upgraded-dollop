#!/usr/bin/env python3
import time

class Interpreter:
    def __init__(self, filepath, click):
        self.filepath:str = filepath
        self.click:int = click
    def __str__(self):
        f"Interpreter(path={self.filepath})"
    
    def parse(self):
        try:
            self.elapse()
            with open(self.filepath, 'r') as reader:
                lines:list[str] = reader.readlines()
        except FileNotFoundError:
            print(f"Interpreter: Could not find '{self.filepath}'")
        except Exception as e:
            print(f"Interpreter: Unknown error '{e}'")
        else:
            pass
            #  self.elapse()
    
    def elapse(self, initial=0, final=0) -> float:
        if click == 0:
            initial = time.time()
            click += 1
        else:
            final = time.time()
            return round(final-initial, 2)

if __name__ == "__main__":
    print(".")