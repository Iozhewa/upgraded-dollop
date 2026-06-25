#!/usr/bin/env python3
class Factory:
    def __init__(self, datasheet, destination, sections):
        self.datasheet:str = datasheet
        self.destination:str = destination
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}
    def specify(self, *bounds) -> bool:
        self.specs = {section: [] for section in self.sections}
        try:
            with open(self.datasheet, 'r') as reader:
                lines = [line.strip() for line in reader.readlines()
                         if "Page" not in line
                         and "MoTeC C125 Dash Manager" not in line]
        except FileNotFoundError:
            print(f"Factory: Could not find {self.datasheet}")
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
            penultimate:int = lines.index(self.sections[-1])
            final:int = len(lines)
            self.specs[self.sections[-1]] = lines[penultimate:final]
            
            #start:int = self.specs.index(bounds[0])
            #end:int = self.specs.index(bounds[1])
            #self.specs = self.specs[start:end]
            return True
        
    def produce(self, *functions) -> None:
        testCalls = []
        with open(self.destination, 'w') as writer:
            writer.write("#!/usr/bin/env python3\n")
            writer.write("class ParsePackage:\n")
            for function in functions:
                writer.write(f"\tdef _parse_{function}(self, can_data:dict) -> dict:\n")
                writer.write(f"\t\t\'Parse __ data from {function}\'\n")
                writer.write("\t\tpass\n\n")
            writer.write("class TestPackage:\n")
            for test in functions:
                writer.write(f"\tdef _test_{test}(self):\n\t\tpass\n\n")
                testCalls.append(f"self._test_{test}()")
            writer.write("\tdef runAll(self):\n")
            for call in testCalls:
                writer.write(f"\t\t{call}\n")
            writer.write("\nif __name__ == \"__main__\":\n\tTestPackage.runAll()")

if __name__ == "__main__":
    print(".")
    ref = r"parsers\version2\motec.txt"
    draft = r"parsers\version2\product.py"
    headers = ("Summary Information", "Used Channels", "Channels By Function",
               "RS232", "CAN", "Courier C125", "Calculations", "User Conditions",
               "Alarms", "Incomplete Channels", "Unused Channels")
    test = Factory(ref, draft, headers)
    test.specify("RX_GPS", "Courier C125")
    #[print(item, len(test.specs[item])) for item in test.specs]
    test.produce("RX_GPS", "BUS_1", "BUS_2", "BUS_3", "BUS_4")
    [print(k,test.specs[k], sep='\n') for k in test.specs]

'''
Currently the template needs to...
allow for parsing a category of motec data (function naming bit)
in terms of what metrics it offers (result dictionary bit)
and how to parse them out of motec (if-else bit)

it would be good to have a testing class for it but that's assuming behaviours
'''