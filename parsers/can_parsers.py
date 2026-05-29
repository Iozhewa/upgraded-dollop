#!/usr/bin/env python3
"""
Sensor translators.

Each function to take CAN message in raw bytes, decoding
measured values (degrees, kPa, rpm, etc.)

Working with placeholder byte formats until Database CAN
file is provided (that is, need more ECU info).
"""

def parse_sensor(data:bytes) -> float:
    """
    Sensor Name (Abbrev.)
    Expects 2 bytes. Returns unit in SI.

    Placeholder formula to verify against ECU datasheet
    """
    raw = data[0]
    conversion = lambda x: x
    standardized = conversion(raw)
    return standardized
def test_sensor():
    testBytes = bytes([75, 0])
    result = parse_sensor(testBytes)
    print(f"Sensor data: {result} units")
    assert result == 75  # Or other expected value

def parse_brake_pressure(data:bytes) -> float:
    """
    Brake Pressure Parser (for BPS)
    Expects _ bytes. Returns bar.
    https://www.bestech.com.au/blogs/how-pressure-sensors-are-used-in-hydraulic-brake-test-setup/

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_brake_pressure():
    testBytes = bytes([14, 28])
    result = parse_brake_pressure(testBytes)
    print(f"Brake Pressure: {round(result, 2)} bar")
    assert round(result) == 1.0, f"Result was {round(result, 2)} and not ~1"

def parse_accelerator_pedal_position(data:bytes) -> float:
    """
    Accelerator Pedal Position Parser (for APPS)
    Expects _ bytes. Returns pedal travel (0-100%).
    https://filmelectronics.in/accelerator-pedal-position-sensor-importance/

    Verify against ECU datasheet
    """
    raw = data[0]
    toTravel = lambda volts: 100*(volts/5)
    standard = toTravel(raw)
    return standard
def test_accelerator_pedal_position():
    testBytes = bytes([1, 3])
    result = parse_accelerator_pedal_position(testBytes)
    print(f"Accelerator Pedal Position: {round(result, 2)}%")
    assert round(result) == 20.0, f"Result was {round(result, 2)} and not ~20"

def parse_steering_angle(data:bytes) -> float:
    """
    Steering Angle Parser (for SAS)
    Expects _ bytes. Returns turn (1 tr = 360 deg).
    https://www.delphiautoparts.com/resource-center/article/making-sense-of-sensors-steering-angle-sensor

    Verify against ECU datasheet
    """
    raw = data[0]
    toTurn = lambda degrees: degrees/360
    standard = toTurn(raw)
    return standard
def test_steering_angle():
    testBytes = bytes([45, 90])
    result = parse_steering_angle(testBytes)
    print(f"Steering Angle: {round(result, 2)} turn")
    assert result == 0.125, f"Result was {round(result, 3)} and not ~0.125"

def parse_suspension_potentiometer(data:bytes) -> float:
    """
    Suspension Potentiometer Parser (for SP)
    Expects _ bytes. Returns cm.
    https://www.datamc.org/data-acquisition/adding-sensors/suspension-potentiometers/

    Verify against ECU datasheet
    """
    raw = data[0]
    toCm = lambda mm: mm / 10
    standard = toCm(raw)
    return standard
def test_suspension_potentiometer():
    testBytes = bytes([10, 20])
    result = parse_suspension_potentiometer(testBytes)
    print(f"Suspension Potentiometer: {round(result, 2)} cm")
    assert result == 1.0, f"Result was {round(result, 2)} and not ~0.1"

def parse_wheel_speed(data:bytes) -> float:
    """
    Wheel Speed Parser (for WS)
    Expects _ bytes. Returns m/s.
    https://premierautotrade.com.au/news/wheel-speed-sensors%E2%80%93more-than-just-abs.php

    Verify against ECU datasheet
    """
    raw = data[0]
    toMS = lambda kmh: kmh / 3.6
    standard = toMS(raw)
    return standard
def test_wheel_speed():
    testBytes = bytes([1, 10])
    result = parse_wheel_speed(testBytes)
    print(f"Wheel Speed: {round(result, 2)} m/s")
    assert round(result, 3) == round(0.277778, 3), f"Result was {round(result, 3)} and not ~{round(0.277778, 3)}"

def parse_intake_air_temp(data:bytes) -> float:
    """
    Intake Air Temperature Parser (for IAT)
    Expects _ bytes. Returns Kelvin.
    https://premierautotrade.com.au/news/intake-air-temperature-sensors.php

    Verify against ECU datasheet
    """
    raw = data[0]
    toKelvin = lambda celsius: celsius + 273.15
    standard = toKelvin(raw)
    return standard
def test_intake_air_temp():
    testBytes = bytes([0, 10])
    result = parse_intake_air_temp(testBytes)
    print(f"Intake Air Temperature: {round(result, 2)} Kelvin")
    assert round(result, 2) == 273.15, f"Result was {round(result, 2)} and not ~273.15"

def parse_ambient_air_temp(data:bytes) -> float:
    """
    Ambient Air Temperature Parser (for AMB)
    Expects _ bytes. Returns Kelvin.
    https://www.innova.com/blogs/fix-advices/understanding-the-ambient-temperature-sensor?srsltid=AfmBOorjtpH8TCLyBXSzgSRheK6KPQmtDmIlf7uAL4GIG27tNG5kWpPO

    Verify against ECU datasheet
    """
    raw = data[0]
    toKelvin = lambda celsius: celsius + 273.15
    standard = toKelvin(raw)
    return standard
def test_ambient_air_temp():
    testBytes = bytes([10, 20])
    result = parse_ambient_air_temp(testBytes)
    print(f"Ambient Air Temperature: {round(result, 2)} Kelvin")
    assert round(result, 2) == 283.15, f"Result was {round(result, 2)} and not ~283.15"

def parse_oil_pressure(data:bytes) -> float:
    """
    Oil Pressure Parser (for OIL)
    Expects _ bytes. Returns bar.
    https://cdsentec.com/pressure-oil-sensors/

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_oil_pressure():
    testBytes = bytes([28, 42])
    result = parse_oil_pressure(testBytes)
    print(f"Brake Pressure: {round(result, 2)} bar")
    assert round(result) == 2.0, f"Result was {round(result, 2)} and not ~2"

def parse_engine_coolant_temp(data:bytes) -> float:
    """
    Engine Coolant Parser (for ECT)
    Expects _ bytes. Returns Kelvin.
    https://autoditex.com/page/engine-coolant-temperature-sensor-ect-13-1.html

    Verify against ECU datasheet
    """
    raw = data[0]
    toKelvin = lambda celsius: celsius + 273.15
    standard = toKelvin(raw)
    return standard
def test_engine_coolant_temp():
    testBytes = bytes([20, 30])
    result = parse_engine_coolant_temp(testBytes)
    print(f"Engine Coolant Temperature: {round(result, 2)} Kelvin")
    assert round(result, 2) == 293.15, f"Result was {round(result, 2)} and not ~293.15"

def parse_fuel_pressure(data:bytes) -> float:
    """
    Fuel Pressure Parser (for FPS)
    Expects _ bytes. Returns bar.
    https://support.haltech.com/portal/en/kb/articles/fuel-pressure-sensor-and-diagnosis

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_fuel_pressure():
    testBytes = bytes([42, 56])
    result = parse_fuel_pressure(testBytes)
    print(f"Brake Pressure: {round(result, 2)} bar")
    assert round(result) == 3.0, f"Result was {round(result, 2)} and not ~3"

def parse_manifold_absolute_pressure(data:bytes) -> float:
    """
    Manifold Absolute Pressure Parser (for MAP)
    Expects _ bytes. Returns bar.
    https://autoditex.com/page/manifold-absolute-pressure-sensor-map-sensor-20-1.html

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_manifold_absolute_pressure():
    testBytes = bytes([56, 70])
    result = parse_manifold_absolute_pressure(testBytes)
    print(f"Brake Pressure: {round(result, 2)} bar")
    assert round(result) == 4.0, f"Result was {round(result, 2)} and not ~4"

def parse_camshaft_position(data:bytes) -> float:
    """
    Camshaft Position Parser (for CAM)
    Expects _ bytes. Returns cylinder identification (?).
    https://autoditex.com/page/camshaft-position-sensor-cmp-12-1.html
    
    Verify against ECU datasheet
    """
    raw = data[0]
    return raw  # conversion requirements unknown
def test_camshaft_position():
    testBytes = bytes([1, 0])
    result = parse_camshaft_position(testBytes)
    print(f"Camshaft Position: Cylinder {result}")
    assert result == 1, f"Result was {result} and not 1"

def parse_crankshaft_position(data:bytes) -> float:
    """
    Crankshaft Position Parser (for CRANK)
    Expects _ bytes. Returns position of crankshaft (?).
    https://autoditex.com/page/crankshaft-position-sensor-ckp-11-1.html
    
    Verify against ECU datasheet
    """
    raw = data[0]
    return raw  # conversion requirements unknown
def test_crankshaft_position():
    testBytes = bytes([2, 0])
    result = parse_crankshaft_position(testBytes)
    print(f"Crankshaft Position: {result}")
    assert result == 2, f"Result was {result} and not 2"

def parse_knock(data:bytes) -> float:
    """
    Knock Parser (for KNOCK)
    Expects _ bytes. Returns detonation frequency (6 kHz to 15 kHz) in radians per second
    https://autoditex.com/page/knock-sensor-ks-18-1.html

    Verify against ECU datasheet
    """
    raw = data[0]
    toRadiansPerSec = lambda kiloHertz: 1000*(kiloHertz/(2*3.14159))
    standard = toRadiansPerSec(raw)
    return standard
def test_knock():
    testBytes = bytes([6, 15])
    result = parse_knock(testBytes)
    print(f"Detonation Frequency: {round(result, 2)} radians per second")
    assert round(result, 2) == round(6000/(2*3.14159), 2), f"Result was {result} and not ~{round(6000/(2*3.14159), 2)}"

def parse_turbo_boost(data:bytes) -> float:
    """
    Turbo Boost Parser (for TURBO)
    Expects _ bytes. Returns bar.
    https://autoditex.com/page/boost-pressure-sensor-bps-24-1.html

    Verify against ECU datasheet
    """
    raw = data[0]
    toBar = lambda psi: psi / 14.504
    standard = toBar(raw)
    return standard
def test_turbo_boost():
    testBytes = bytes([70, 84])
    result = parse_brake_pressure(testBytes)
    print(f"Turbo Boost: {round(result, 2)} bar")
    assert round(result) == 5.0, f"Result was {round(result, 2)} and not ~1"

def parse_gas(data:bytes) -> float:
    """
    Gas Parser (for GS)
    Expects _ bytes. Returns percent volume from ppm.
    https://www.rhopointcomponents.com/resources/engineering-calculators/ppm-to-percent-converter/

    Verify against ECU datasheet
    """
    raw = data[0]
    toPercentVol = lambda ppm: ppm / 10_000
    standard = toPercentVol(raw)
    return standard
def test_gas():
    testBytes = bytes([5, 6])
    result = parse_gas(testBytes)
    print(f"Gas: {result}%")
    assert result == 5 / 10_000, f"Result was {result} and not {5 / 10_000}"

def parse_quickshifter(data:bytes) -> float:
    """
    Quickshifter Parser (for QS)
    Expects _ bytes. Returns detected quickshifter use(?).
    https://www.apriliaforum.com/forums/showthread.php?371844-Anatomy-of-a-quickshifter-sensor

    Verify against ECU datasheet
    """
    raw = data[0]
    return raw  # Conversion requirement unknown
def test_quickshifter():
    testBytes = bytes([0, 1])
    result = parse_crankshaft_position(testBytes)
    print(f"Quickshifter in Use: {result}")
    assert result == 0, f"Result was {result} and not 0"

def parse_lambda_to_can(data:bytes) -> float:
    """
    Lambda-to-CAN Parser (for LTC)
    Expects _ bytes. Returns level of oxygen in exhaust gases.
    https://linkecu.com/tech-articles/can-lambda-explained/

    Verify against ECU datasheet
    """
    raw = data[0]
    toDecimal = lambda percent: percent / 100
    standard = toDecimal(raw)
    return standard
def test_lambda_to_can():
    testBytes = bytes([65, 98])
    result = parse_lambda_to_can(testBytes)
    print(f"Lambda: {result}")
    assert result == 0.65, f"Result was {result} and not 0.65"

if __name__ == "__main__":
    test_brake_pressure()
    test_accelerator_pedal_position()
    test_steering_angle()
    test_suspension_potentiometer()
    test_wheel_speed()
    test_intake_air_temp()
    test_ambient_air_temp()
    test_oil_pressure()
    test_engine_coolant_temp()
    test_fuel_pressure()
    test_manifold_absolute_pressure()
    test_camshaft_position()
    test_crankshaft_position()
    test_knock()
    test_turbo_boost()
    test_gas()
    test_quickshifter()
    test_lambda_to_can()
    print()
