#!/usr/bin/env python3
from time import sleep as s

class Factory:
    '''
    Given a file to read (MoTec config) and a file to write (Python file),
    attempts to outline sensors to code parsers for. The resulting parser
    program comprises of a ParserPackage class, and a TestPackage class as quality assurance.

    Since the ParserPackage is propogated template code, edits are intended to be implemented
    systematically in this Factory class. Edits to the automatically created product program is
    not recommended.
    '''
    def __init__(self, fileread, filewrite, sections):
        self.fileread:str = fileread
        self.filewrite:str = filewrite
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}  # Non-inputted attribute
    def __str__(self):
        return f"Factory(fileread={self.fileread}, filewrite={self.filewrite})"

    def setFileDictionary(self) -> bool:
        '''
        Reads self.fileread to create a dictionary of file lines.
        self.sections establishes what lines can be grouped under a category
            e.g. Incomplete Channels is a key to file lines describing MoTec partial channels
        '''
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
            for index, section in enumerate(self.sections):
                if index+1 == len(self.sections): continue

                first:int = lines.index(section)+1
                last:int = lines.index(self.sections[index+1])
                self.specs[section] = lines[first:last]
            
            semifinal:int = lines.index(self.sections[-1])
            final:int = len(lines)
            self.specs[self.sections[-1]] = lines[semifinal:final]
            return True

    def writeFunctionAt(self, **functions) -> bool:
        try:
            with open(self.filewrite, 'w') as writer:
                writer.write("#!/usr/bin/env python3\n")
                writer.write("#  Dev note: This code was written automatically by factory program!\n")
        except FileNotFoundError:
            print(f"Factory: Could not find {self.filewrite}")
            return False
        except Exception as e:
            print(f"Factory: Unknown error {e}")
            return False
        else:
            pass

if __name__ == "__main__":
    print(".")  # Terminal confirmation of execution