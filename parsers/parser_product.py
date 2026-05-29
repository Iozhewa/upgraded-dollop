#!/usr/bin/env python3
"""
Sensor translators.

Each function to take CAN message in raw bytes, decoding
measured values (degrees, kPa, rpm, etc.)

Working with placeholder byte formats until Database CAN
file is provided (that is, need more ECU info).
"""
class ParsePackage:
	
	def parse_turbo_recirculation_valve(data:bytes) -> float:
		'''
		Turbo Recirculation Valve Parser (for TRV)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_camshaft_position_sensor(data:bytes) -> float:
		'''
		Camshaft Position Sensor Parser (for CAM)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_oil_pressure_sensor(data:bytes) -> float:
		'''
		Oil Pressure Sensor Parser (for OIL)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_crankshaft_position_sensor(data:bytes) -> float:
		'''
		Crankshaft Position Sensor Parser (for CRANK)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_knock_sensor(data:bytes) -> float:
		'''
		Knock Sensor Parser (for KNOCK)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_quickshifter_sensor(data:bytes) -> float:
		'''
		Quickshifter Sensor Parser (for QS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_throttle_position_sensor(data:bytes) -> float:
		'''
		Throttle Position Sensor Parser (for TPS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_brake_pressure_sensor(data:bytes) -> float:
		'''
		Brake Pressure Sensor Parser (for BPS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_oil_temperature_sensor(data:bytes) -> float:
		'''
		Oil Temperature Sensor Parser (for OTS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_mac_valve__boost_control_solenoid(data:bytes) -> float:
		'''
		MAC Valve  Boost Control Solenoid Parser (for MAC)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_engine_coolant_temperature(data:bytes) -> float:
		'''
		Engine Coolant Temperature Parser (for ECT)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_accelerator_pedal_position_sensor(data:bytes) -> float:
		'''
		Accelerator Pedal Position Sensor Parser (for APPS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_manifold_absolute_pressure(data:bytes) -> float:
		'''
		Manifold Absolute Pressure Parser (for MAP)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_lambda_to_can(data:bytes) -> float:
		'''
		Lambda to CAN Parser (for LTC)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
	
	def parse_fuel_pressure_sensor(data:bytes) -> float:
		'''
		Fuel Pressure Sensor Parser (for FPS)
		Expects _ bytes. Returns unit TBA.
		[source recommended]
	
		Verify against ECU datasheet
		'''
		raw = data[0]
		conversion = lambda x: x  # Conversion formula recommended
		standard = conversion(raw)
		return standard
	
class TestPackage:	
	def test_turbo_recirculation_valve():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_turbo_recirculation_valve(testBytes)
		print(f"Turbo Recirculation Valve:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_camshaft_position_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_camshaft_position_sensor(testBytes)
		print(f"Camshaft Position Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_oil_pressure_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_oil_pressure_sensor(testBytes)
		print(f"Oil Pressure Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_crankshaft_position_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_crankshaft_position_sensor(testBytes)
		print(f"Crankshaft Position Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_knock_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_knock_sensor(testBytes)
		print(f"Knock Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_quickshifter_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_quickshifter_sensor(testBytes)
		print(f"Quickshifter Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_throttle_position_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_throttle_position_sensor(testBytes)
		print(f"Throttle Position Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_brake_pressure_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_brake_pressure_sensor(testBytes)
		print(f"Brake Pressure Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_oil_temperature_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_oil_temperature_sensor(testBytes)
		print(f"Oil Temperature Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_mac_valve__boost_control_solenoid():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_mac_valve__boost_control_solenoid(testBytes)
		print(f"MAC Valve  Boost Control Solenoid:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_engine_coolant_temperature():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_engine_coolant_temperature(testBytes)
		print(f"Engine Coolant Temperature:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_accelerator_pedal_position_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_accelerator_pedal_position_sensor(testBytes)
		print(f"Accelerator Pedal Position Sensor:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_manifold_absolute_pressure():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_manifold_absolute_pressure(testBytes)
		print(f"Manifold Absolute Pressure:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_lambda_to_can():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_lambda_to_can(testBytes)
		print(f"Lambda to CAN:", result)
		assert result == 14, "Expected 14, got " + result
		
	def test_fuel_pressure_sensor():
		testBytes = bytes([14, 28])
		result = ParsePackage.parse_fuel_pressure_sensor(testBytes)
		print(f"Fuel Pressure Sensor:", result)
		assert result == 14, "Expected 14, got " + result
	
	def runAll():
		TestPackage.test_turbo_recirculation_valve()
		TestPackage.test_camshaft_position_sensor()
		TestPackage.test_oil_pressure_sensor()
		TestPackage.test_crankshaft_position_sensor()
		TestPackage.test_knock_sensor()
		TestPackage.test_quickshifter_sensor()
		TestPackage.test_throttle_position_sensor()
		TestPackage.test_brake_pressure_sensor()
		TestPackage.test_oil_temperature_sensor()
		TestPackage.test_mac_valve__boost_control_solenoid()
		TestPackage.test_engine_coolant_temperature()
		TestPackage.test_accelerator_pedal_position_sensor()
		TestPackage.test_manifold_absolute_pressure()
		TestPackage.test_lambda_to_can()
		TestPackage.test_fuel_pressure_sensor()

if __name__ == "__main__":
	TestPackage.runAll()