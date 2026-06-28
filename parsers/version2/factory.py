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

    def writeFunctionsAt(self, **functions) -> bool:
        '''
        Finds self.filewrite and writes parser code. Explicitly organized into ParserPackage, the collection
        of functions turning MoTec data into known values; and TestPackage, a starting point for quality assurance
        of the ParserPackage class.
        '''
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
            print("Factory now writing. Identified the following measures:")
            proceed = input(">> ")  # Useful for large-scale template programming
            with open(self.filewrite, 'a') as writer:
                counter:int = 1
                writer.write("class ParsePackage:\n")
                for f in functions:
                    addresses = {}
                    writer.write(f"\tdef _parse_{f}(data:dict) -> dict:\n")
                    writer.write(f"\t\t\'Parses [context unknown] data from {f}\'\n")
                    writer.write("\t\tresult = {\n")
                    for spec in self.specs[functions[f]]:
                        if ':' in spec:
                            print(counter, spec.split("Id"))
                            counter += 1
                            s(0.05)
                            label = spec.split("Id")[0]
                            address = "Id" + ''.join(spec.split("Id"))
                            addresses[label] = address
                            writer.write(f"\t\t\t\"{label.strip()}\": 0,\n")
                    writer.write("\t\t}\n")
                    for label in addresses:
                        #  Addressing method unknown, placeholder erroneous
                        addr = ''.join([n for n in addresses[label] if n.isnumeric()])
                        writer.write(f"\t\tif 0x{addr} in data:\n")
                        writer.write(f"\t\t\tmsg = data[0x{addr}]\n")
                        writer.write(f"\t\t\tdata = bytes.fromhex(msg[\"data\"])\n")
                        writer.write(f"\t\t\tresult[\"{label.strip()}\"] = int.from_bytes(data[0:2], byteorder=\'little\')\n")
                    writer.write("\n\t\treturn result\n\n")
                
                writer.write("class TestPackage:\n")
                testCalls = []
                for test in functions:
                    writer.write(f"\tdef _test_{test}():\n")
                    #  Expected behaviour currently undefined. Example, non-functional code supplied.
                    writer.write(f"\t\ttestBytes = bytes([1, 2])\n")
                    writer.write(f"\t\tresult = ParsePackage._parse_{test}(data=testBytes)\n")
                    writer.write(f"\t\tprint(f\"{test} outputs:\", result)\n")
                    writer.write(f"\t\tassert result == 1, \"Expected 1, got \" + result\n\n")
                    testCalls.append(f"TestPackage._test_{test}()")
                writer.write("\tdef runAll():\n")
                for call in testCalls:
                    writer.write(f"\t\t{call}\n")
                writer.write("\nif __name__ == \"__main__\":\n\tTestPackage.runAll()")
                
                return True
            
if __name__ == "__main__":
    print(".")  # Terminal confirmation of execution
    ref = r"parsers\version2\motec.txt"
    draft = r"parsers\version2\product.py"
    fileheaders = ("Summary Information", "Used Channels", "Channels By Function",
               "RS232", "Bus 2 (1) M1_General_0x640_Version 5", "Bus 2 (2) M1_General_0x650_Version 5",
               "Bus 2 (3) M1_General_0x670_Version 1", "Bus 2 (4) M1_General_0x6A0_Version 1", 
               "Courier C125", "Calculations", "User Conditions",
               "Alarms", "Incomplete Channels", "Unused Channels")
    
    facto = Factory(fileread=ref, filewrite=draft, sections=fileheaders)
    facto.setFileDictionary()
    facto.writeFunctionsAt(RX_GPS="RS232", 
                 BUS_1="Bus 2 (1) M1_General_0x640_Version 5", 
                 BUS_2="Bus 2 (2) M1_General_0x650_Version 5", 
                 BUS_3="Bus 2 (3) M1_General_0x670_Version 1", 
                 BUS_4="Bus 2 (4) M1_General_0x6A0_Version 1")
