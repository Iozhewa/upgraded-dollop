# MoTec C125 Data Parser
Telemetry Garage's `telemetry-capture` file has incomplete parsers, a gap in its data capture processes:

<details>
<summary> Snippet: Incomplete Code </summary>

``` python
def _parse_vehicle_dynamics(self, can_data: Dict, gps_data: Optional[Dict] = None) -> Dict:
    """Parse vehicle dynamics from MPU-9250 IMU sensor and optionally GPS speed."""
    imu_data = self.mpu9250.read_all()

    # Speed: from GPS when speed_from_gps is True, otherwise from CAN bus
    if self.config.get("speed_from_gps", False) and gps_data and gps_data.get("speed_kmh") is not None:
        speed = round(float(gps_data["speed_kmh"]), 2)
    else:
        # TODO: Parse speed from CAN when CAN protocol is implemented
        speed = 0.0

    return {
        "speed": speed,
        "yaw": round(imu_data["yaw"], 2),
        "roll": round(imu_data["roll"], 2),
        "pitch": round(imu_data["pitch"], 2),
        "lateral_g": round(imu_data["lateral_g"], 2),
        "longitudinal_g": round(imu_data["longitudinal_g"], 2),
        "vertical_g": round(imu_data["vertical_g"], 2),
        "steering_angle": 0.0,
    }

def _parse_powertrain(self, can_data: Dict) -> Dict:
    """Parse powertrain data from CAN."""
    return {
        "gear": 0,
        "throttle_position": 0.0,
        "braking_force": 0.0,
        "engine_rpm": 0,
        "engine_temperature": 0.0,
        "oil_pressure": 0.0,
        "oil_temperature": 0.0,
        "coolant_temperature": 0.0,
        "turbo_boost_pressure": 0.0,
        "air_intake_temperature": 0.0,
        "fuel_level": 0.0,
    }

def _parse_suspension(self, can_data: Dict) -> Dict:
    """Parse suspension data from CAN."""
    return {
        "front_left": 0.0,
        "front_right": 0.0,
        "rear_left": 0.0,
        "rear_right": 0.0,
    }

def _parse_wheels(self, can_data: Dict) -> Dict:
    """Parse wheel speed data from CAN."""
    return {
        "front_left": 0.0,
        "front_right": 0.0,
        "rear_left": 0.0,
        "rear_right": 0.0,
    }
```
</details>
<br>

Presumably this is remedied on a case-to-case basis. 
- `version1` samples a solution with a CSV file, propogating parser code via factory program. This was written prior to acquisition of the Dash Manager config file (see version2). The result is a 331-line executable written by a 184-line Python program
- `version2` samples a solution with a TXT file, propogating parser code with greater abstraction. This solution is designed to read any Dash Manager config file supplied. The result is a 1470-line executable written by a 110-line Python program

Development on Factory v1 closes with a proof-of-concept. MoTec properties are assumed, resulting in an immediately executable product. 
``` bash
cd parsers/version1
python3 parser_factory.py  # Generate code based on sensors listed on CSV
python3 parser_product.py  # Product tests mock parser functions
```

Development on Factory v2 is more promising. The ratio of generated code to generating code is greater (331:184 < 1470:110) but the product ought to run in O(1) time. Smelly, unabstracted code, but accounting for hundreds of sensors with narrow margins of error.
``` bash
cd parsers/version2
python3 factory.py  # Generate code based on sensors on converted motec.pdf
python3 product.py  # Syntactically correct, but placeholders will create semantic errors at runtime
```
## Developing Parser Factory v1
At the requirements gathering stage, a `.csv` Sensor Tracker was exported from a `.xlsx` file, in the interest of solutions without external modules. This presumes (.xlsx -> .csv) only loses formatting information, which later inspires the (.pdf -> .txt) export from Dash Manager's config PDF file.

`can_parsers` is archived in the `version1/` subdirectory to preserve an attempt to manually code all known functions. A memento to duplicated code frustrations, pain points to abstract, and the necessity of a factory program.

`parser_module` is archived for similar reasons, now reorganizing the functional code into the classes `ParsePackage` and `TestPackage`. Initially this appeared to add needless complexity to factory development, but the added structure undoubtedly enhances readability. For enhanced code quality, this became an endgoal.

`parser_factory` is the program of the hour. A careful balance of f-strings and File Handling code. Note that for file writing with multiline strings, `\t` is preferable to four space bars, as Python will penalize inconsistent spacing.
- Tasks were decomposed into _reading table_, _defining relevant sensors_, _completing parser templates_, _designing functions_, and _designing classes_
- `__main__` is very hard-coded, essentially everything that could not be guaranteed by decompositions and global variables
    - Terminal output provides useful commentary on functions as they are called

## Developing Parser Factory v2
MoTec C125 Dash Manager exports a configuration PDF, which I crudely imported into Google Docs before exporting out in TXT format. This is likely a technique not limited to Google Docs, but I the idea jumped at me from Drive.

`template` is a closer-to-concept reference point from Telemetry Garage. The author themself doesn't leave hints to interpret MoTec addresses, which becomes a prevailing issue later on.

`factory` is the program of the hour. It's got forced delays as I insisted the terminal output display identified sensors at a semi-readable print rate. 
- While `setFileDictionary()` maintains read mode throughout the Error Handling code, it turns out write mode closed at the try block for `writeFunctionsAt()`
    - You'll notice, then, the latter function uses write mode AND append mode. A sly workaround, if I do say so myself.
    - Template code is closer to the writing function than `parser_factory`'s counterparts, which I hope allows for intuitive edits

## Closing Notes