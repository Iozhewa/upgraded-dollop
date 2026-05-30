class Template:
    def __str__(self):
        return '''def _parse_powertrain(self, can_data: Dict) -> Dict:
"""Parse powertrain data from CAN."""
result = {
    "gear": 0,
    "throttle_position": 0.0,
    "engine_rpm": 0,
    # ... defaults
}

# Example: Parse engine RPM from CAN ID 0x123
if 0x123 in can_data:
    msg = can_data[0x123]
    data = bytes.fromhex(msg["data"])
    # Assuming RPM is in bytes 0-1 (little endian)
    result["engine_rpm"] = int.from_bytes(data[0:2], byteorder='little')

return result'''

    def _parse_powertrain(self, can_data: dict) -> dict:
        """Parse powertrain data from CAN."""
        result = {
            "gear": 0,
            "throttle_position": 0.0,
            "engine_rpm": 0,
            # ... defaults
        }
        
        # Example: Parse engine RPM from CAN ID 0x123
        if 0x123 in can_data:
            msg = can_data[0x123]
            data = bytes.fromhex(msg["data"])
            # Assuming RPM is in bytes 0-1 (little endian)
            result["engine_rpm"] = int.from_bytes(data[0:2], byteorder='little')
        
        return result

if __name__ == "__main__":
    '''
    Took the parser template from Telemetry Garage and created a Python class
    used to return a string copy of its sole function.

    Achieves this by invoking Template.__str__() as seen below.
    '''
    t = Template()
    test:str = str(t)
    print(f"{test}")