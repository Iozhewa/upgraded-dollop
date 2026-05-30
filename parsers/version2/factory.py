#!/usr/bin/env python3
from template import Template
class Factory:
    def __init__(self, filepath, sections):
        self.filepath:str = filepath
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}
    def specify(self) -> None:
        self.specs = {section: [] for section in self.sections}
        try:
            with open(self.filepath, 'r') as reader:
                lines = [line.strip() for line in reader.readlines()
                         if "Page" not in line
                         and "MoTeC C125 Dash Manager" not in line]
        except FileNotFoundError:
            print(f"Factory: Could not find {self.filepath}")
        except Exception as e:
            print(f"Factory: Unknown error {e}")
        else:
            for index, section in enumerate(self.sections):
                if index+1 == len(self.sections): continue
                first:int = lines.index(section)+1
                last:int = lines.index(self.sections[index+1])
                self.specs[section] = lines[first:last]
            penultimate:int = lines.index(self.sections[-1])
            final:int = len(lines)
            self.specs[self.sections[-1]] = lines[penultimate:final]

if __name__ == "__main__":
    print(".")
    path = r"parsers\version2\motec.txt"
    headers = ("Summary Information", "Used Channels", "Channels By Function",
               "RS232", "CAN", "Courier C125", "Calculations", "User Conditions",
               "Alarms", "Incomplete Channels", "Unused Channels")
    test = Factory(path, headers)
    test.specify()
    [print(item, len(test.specs[item])) for item in test.specs]
