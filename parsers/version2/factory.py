#!/usr/bin/env python3


class Factory:
    def __init__(self, datasheet, destination, sections):
        self.datasheet:str = datasheet
        self.destination:str = destination
        self.sections:tuple[str] = sections
        self.specs:dict[str, list[str]] = {}
    def specify(self) -> bool:
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
            return True
        
    def produce(self, *functions) -> None:
        with open(self.destination, 'w') as writer:
            writer.write("#!/usr/bin/env python3\n")
            writer.write("class ParsePackage:\n\tpass\n\n")
            # stuff
            writer.write("class TestPackage:\n\tpass\n\n")
            # stuff
            writer.write("if __name__ == \"__main__\":\n\tTestPackage.runAll()")

if __name__ == "__main__":
    print(".")
    ref = r"parsers\version2\motec.txt"
    draft = r"parsers\version2\product.py"
    headers = ("Summary Information", "Used Channels", "Channels By Function",
               "RS232", "CAN", "Courier C125", "Calculations", "User Conditions",
               "Alarms", "Incomplete Channels", "Unused Channels")
    test = Factory(ref, draft, headers)
    test.specify()
    [print(item, len(test.specs[item])) for item in test.specs]
    test.produce("RS232", "CAN")

'''
Currently the template needs to...
allow for parsing a category of motec data (function naming bit)
in terms of what metrics it offers (result dictionary bit)
and how to parse them out of motec (if-else bit)

it would be good to have a testing class for it but that's assuming behaviours
'''