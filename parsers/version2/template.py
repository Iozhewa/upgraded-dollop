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

class Parsers:
    def _parse_this(self, can_data: dict) -> dict:
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

class Testers:
    def _test_this():
        pass

if __name__ == "__main__":
    print('.')