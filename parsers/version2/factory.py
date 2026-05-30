#!/usr/bin/env python3
'''
In case I forget, the file handling trick was horrendously simple
    [1] Upload PDF to Google Drive
    [2] Open PDF with Google Docs
    [3] Download Gdocs PDF as TXT extension
    [4] Copy here for file handling
Assuming everything was transferred neatly...
'''
from template import Template
#t = str(Template())
#print(t)
class Factory:
    def __init__(self, filepath, sections):
        self.filepath:str = filepath
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}
    def specify(self) -> None:
        self.specs = {section: [] for section in self.sections}
        try:
            with open(self.filepath, 'r') as reader:
                lines = reader.readlines()
        except FileNotFoundError:
            print(f"Factory: Could not find {self.filepath}")
        except Exception as e:
            print(f"Factory: Unknown error {e}")
        else:
            pass

if __name__ == "__main__":
    print(".")
    path = r"parsers\version2\motec.txt"
    headers = ("Summary Information", "Used Channels")
    test = Factory(path, headers)
    test.specify()
    [print(item, len(test.specs[item])) for item in test.specs]
    print(test.specs["Summary Information"])

'''
motec headers obscured by .txt export
Summary Information
Configuration Comments
Used Channels

Channels by Function [...]
    RS232-RX_GPS: Generates Channels, Received Channels
    CAN-BUS_2(1): et al
    CAN-BUS_2(2): et al
    CAN-BUS_2(3): et al
    CAN-BUS_2(4): et al
CoC125r: Generates Channels

Calculations
Lap Gain/Loss
Tables
3D
Timers
User Conditions
Normal
RACE
WARMUP
Alarms
Shift Lights
Incomplete Channels
Unused Channels
'''