#!/usr/bin/env python3
"""
Sensor translators.

Each function to take CAN message in raw bytes, decoding
measured values (degrees, kPa, rpm, etc.)

Working with placeholder byte formats until Database CAN
file is provided (that is, need more ECU info).
"""

class ParsePackage:
    def brake_pressure(data:bytes) -> float:
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
    def accelerator_pedal_position(data:bytes) -> float:
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
    def steering_angle(data:bytes) -> float:
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
    def suspension_potentiometer(data:bytes) -> float:
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
    def wheel_speed(data:bytes) -> float:
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
    def intake_air_temp(data:bytes) -> float:
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
    def ambient_air_temp(data:bytes) -> float:
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
    def oil_pressure(data:bytes) -> float:
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
    def engine_coolant_temp(data:bytes) -> float:
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
    def fuel_pressure(data:bytes) -> float:
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
    def manifold_absolute_pressure(data:bytes) -> float:
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
    def camshaft_position(data:bytes) -> float:
        """
        Camshaft Position Parser (for CAM)
        Expects _ bytes. Returns cylinder identification (?).
        https://autoditex.com/page/camshaft-position-sensor-cmp-12-1.html
        
        Verify against ECU datasheet
        """
        raw = data[0]
        return raw  # conversion requirements unknown
    def crankshaft_position(data:bytes) -> float:
        """
        Crankshaft Position Parser (for CRANK)
        Expects _ bytes. Returns position of crankshaft (?).
        https://autoditex.com/page/crankshaft-position-sensor-ckp-11-1.html
        
        Verify against ECU datasheet
        """
        raw = data[0]
        return raw  # conversion requirements unknown
    def knock(data:bytes) -> float:
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
    def turbo_boost(data:bytes) -> float:
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
    def gas(data:bytes) -> float:
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
    def quickshifter(data:bytes) -> float:
        """
        Quickshifter Parser (for QS)
        Expects _ bytes. Returns detected quickshifter use(?).
        https://www.apriliaforum.com/forums/showthread.php?371844-Anatomy-of-a-quickshifter-sensor

        Verify against ECU datasheet
        """
        raw = data[0]
        return raw  # Conversion requirement unknown
    def lambda_to_can(data:bytes) -> float:
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

class TestPackage:
    def brake_pressure():
        testBytes = bytes([14, 28])
        result = ParsePackage.brake_pressure(testBytes)
        print(f"Brake Pressure: {round(result, 2)} bar")
        assert round(result) == 1.0, f"Result was {round(result, 2)} and not ~1"
    def accelerator_pedal_position():
        testBytes = bytes([1, 3])
        result = ParsePackage.accelerator_pedal_position(testBytes)
        print(f"Accelerator Pedal Position: {round(result, 2)}%")
        assert round(result) == 20.0, f"Result was {round(result, 2)} and not ~20"
    def steering_angle():
        testBytes = bytes([45, 90])
        result = ParsePackage.steering_angle(testBytes)
        print(f"Steering Angle: {round(result, 2)} turn")
        assert result == 0.125, f"Result was {round(result, 3)} and not ~0.125"
    def suspension_potentiometer():
        testBytes = bytes([10, 20])
        result = ParsePackage.suspension_potentiometer(testBytes)
        print(f"Suspension Potentiometer: {round(result, 2)} cm")
        assert result == 1.0, f"Result was {round(result, 2)} and not ~0.1"
    def wheel_speed():
        testBytes = bytes([1, 10])
        result = ParsePackage.wheel_speed(testBytes)
        print(f"Wheel Speed: {round(result, 2)} m/s")
        assert round(result, 3) == round(0.277778, 3), f"Result was {round(result, 3)} and not ~{round(0.277778, 3)}"
    def intake_air_temp():
        testBytes = bytes([0, 10])
        result = ParsePackage.intake_air_temp(testBytes)
        print(f"Intake Air Temperature: {round(result, 2)} Kelvin")
        assert round(result, 2) == 273.15, f"Result was {round(result, 2)} and not ~273.15"
    def ambient_air_temp():
        testBytes = bytes([10, 20])
        result = ParsePackage.ambient_air_temp(testBytes)
        print(f"Ambient Air Temperature: {round(result, 2)} Kelvin")
        assert round(result, 2) == 283.15, f"Result was {round(result, 2)} and not ~283.15"
    def oil_pressure():
        testBytes = bytes([28, 42])
        result = ParsePackage.oil_pressure(testBytes)
        print(f"Brake Pressure: {round(result, 2)} bar")
        assert round(result) == 2.0, f"Result was {round(result, 2)} and not ~2"
    def engine_coolant_temp():
        testBytes = bytes([20, 30])
        result = ParsePackage.engine_coolant_temp(testBytes)
        print(f"Engine Coolant Temperature: {round(result, 2)} Kelvin")
        assert round(result, 2) == 293.15, f"Result was {round(result, 2)} and not ~293.15"
    def fuel_pressure():
        testBytes = bytes([42, 56])
        result = ParsePackage.fuel_pressure(testBytes)
        print(f"Brake Pressure: {round(result, 2)} bar")
        assert round(result) == 3.0, f"Result was {round(result, 2)} and not ~3"
    def manifold_absolute_pressure():
        testBytes = bytes([56, 70])
        result = ParsePackage.manifold_absolute_pressure(testBytes)
        print(f"Brake Pressure: {round(result, 2)} bar")
        assert round(result) == 4.0, f"Result was {round(result, 2)} and not ~4"
    def camshaft_position():
        testBytes = bytes([1, 0])
        result = ParsePackage.camshaft_position(testBytes)
        print(f"Camshaft Position: Cylinder {result}")
        assert result == 1, f"Result was {result} and not 1"
    def crankshaft_position():
        testBytes = bytes([2, 0])
        result = ParsePackage.crankshaft_position(testBytes)
        print(f"Crankshaft Position: {result}")
        assert result == 2, f"Result was {result} and not 2"
    def knock():
        testBytes = bytes([6, 15])
        result = ParsePackage.knock(testBytes)
        print(f"Detonation Frequency: {round(result, 2)} radians per second")
        assert round(result, 2) == round(6000/(2*3.14159), 2), f"Result was {result} and not ~{round(6000/(2*3.14159), 2)}"
    def turbo_boost():
        testBytes = bytes([70, 84])
        result = ParsePackage.brake_pressure(testBytes)
        print(f"Turbo Boost: {round(result, 2)} bar")
        assert round(result) == 5.0, f"Result was {round(result, 2)} and not ~1"
    def gas():
        testBytes = bytes([5, 6])
        result = ParsePackage.gas(testBytes)
        print(f"Gas: {result}%")
        assert result == 5 / 10_000, f"Result was {result} and not {5 / 10_000}"
    def quickshifter():
        testBytes = bytes([0, 1])
        result = ParsePackage.crankshaft_position(testBytes)
        print(f"Quickshifter in Use: {result}")
        assert result == 0, f"Result was {result} and not 0"
    def lambda_to_can():
        testBytes = bytes([65, 98])
        result = ParsePackage.lambda_to_can(testBytes)
        print(f"Lambda: {result}")
        assert result == 0.65, f"Result was {result} and not 0.65"
    def runAll():
        TestPackage.brake_pressure()
        TestPackage.accelerator_pedal_position()
        TestPackage.steering_angle()
        TestPackage.suspension_potentiometer()
        TestPackage.wheel_speed()
        TestPackage.intake_air_temp()
        TestPackage.ambient_air_temp()
        TestPackage.oil_pressure()
        TestPackage.engine_coolant_temp()
        TestPackage.fuel_pressure()
        TestPackage.manifold_absolute_pressure()
        TestPackage.camshaft_position()
        TestPackage.crankshaft_position()
        TestPackage.knock()
        TestPackage.turbo_boost()
        TestPackage.gas()
        TestPackage.quickshifter()
        TestPackage.lambda_to_can()
        print()

if __name__ == "__main__":
    TestPackage.runAll()