#!/usr/bin/env python3
from time import sleep as s

class Factory:
    def __init__(self, fileread, filewrite, sections):
        self.fileread:str = fileread
        self.filewrite:str = filewrite
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}  # Non-inputted attribute
    def __str__(self):
        return f"Factory(fileread={self.fileread}, filewrite={self.filewrite})"

    def setFileDictionary(self) -> bool:
        self.specs = {section: [] for section in self.sections}
        try:
            with open(self.fileread, 'r') as reader:
                lines = [line.strip() for line in reader.readlines()
                         if "Page" not in line
                         and "MoTec C125 Dash Manager" not in line]
        except FileNotFoundError:
            print(f"Factory: Could not find {self.fileread}")
            return False
        except Exception as e:
            print(f"Factory: Unknown error {e}")
            return False
        else:
            pass

    def writeFunctionAt(self, **functions) -> bool:
        pass

if __name__ == "__main__":
    print(".")  # Terminal confirmation of execution