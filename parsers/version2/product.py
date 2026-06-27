#!/usr/bin/env python3
# Dev note: This code was written automatically by a factory program!
class ParsePackage:
	def _parse_RX_GPS(data:dict) -> dict:
		'Parses [context unknown] data from RX_GPS'
		result = {
			"GPS Time": 0,
			"GPS Latitude": 0,
			"GPS Longitude": 0,
			"GPS Speed": 0,
			"GPS Heading": 0,
			"GPS Date": 0,
			"GPS Sats Used": 0,
			"GPS Altitude": 0,
		}
		if 0x111100 in data:
			msg = data[0x111100]
			data = bytes.fromhex(msg["data"])
			result["GPS Time"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x131100 in data:
			msg = data[0x131100]
			data = bytes.fromhex(msg["data"])
			result["GPS Latitude"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x151100 in data:
			msg = data[0x151100]
			data = bytes.fromhex(msg["data"])
			result["GPS Longitude"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x171852100000 in data:
			msg = data[0x171852100000]
			data = bytes.fromhex(msg["data"])
			result["GPS Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x181100 in data:
			msg = data[0x181100]
			data = bytes.fromhex(msg["data"])
			result["GPS Heading"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x191100 in data:
			msg = data[0x191100]
			data = bytes.fromhex(msg["data"])
			result["GPS Date"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x271100 in data:
			msg = data[0x271100]
			data = bytes.fromhex(msg["data"])
			result["GPS Sats Used"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x291100 in data:
			msg = data[0x291100]
			data = bytes.fromhex(msg["data"])
			result["GPS Altitude"] = int.from_bytes(data[0:2], byteorder='little')


		return result

	def _parse_BUS_1(data:dict) -> dict:
		'Parses [context unknown] data from BUS_1'
		result = {
			"Coolant Temperature": 0,
			"Engine Oil Temperature": 0,
			"Fuel Temperature": 0,
			"Ambient Temperature": 0,
			"Airbox Temperature": 0,
			"Bat Volts ECU": 0,
			"Fuel Used M1": 0,
			"Exhaust Temperature": 0,
			"Engine Load Average": 0,
			"Engine Speed Limit": 0,
			"Ambient Pressure": 0,
			"Ignition Cyl 1 Trim Knock": 0,
			"Ignition Cyl 2 Trim Knock": 0,
			"Ignition Cyl 3 Trim Knock": 0,
			"Ignition Cyl 4 Trim Knock": 0,
			"Ignition Cyl 5 Trim Knock": 0,
			"Ignition Cyl 6 Trim Knock": 0,
			"Ignition Cyl 7 Trim Knock": 0,
			"Ignition Cyl 8 Trim Knock": 0,
			"Engine Run Time": 0,
			"ECU Uptime": 0,
			"Warning Source": 0,
			"Fuel Pressure Warning": 0,
			"Crankcase Pressure Warning": 0,
			"Engine Oil Pressure Warning": 0,
			"Engine Oil Temp Warning": 0,
			"Engine Speed Warning": 0,
			"Coolant Pressure Warning": 0,
			"Coolant Temperature Warning": 0,
			"Knock Warning": 0,
			"Fuel Pump State": 0,
			"Engine State": 0,
			"Launch State": 0,
			"Anti Lag State": 0,
			"Boost Aim State": 0,
			"add: 0, mask:0x F0": 0,
			"Fuel State": 0,
			"Engine Overrun State": 0,
			"Knock State": 0,
			"Fuel Purge State": 0,
			"Fuel Closed Loop State": 0,
			"Throttle Aim State": 0,
			"Gear": 0,
			"Engine Speed Reference State": 0,
			"Engine Speed Limit State": 0,
			"Launch Diagnostic": 0,
			"Anti Lag Diagnostic": 0,
			"Fuel Cut State": 0,
			"Boost Control Diagnostic": 0,
			"Fuel Closed Loop Diagnostic": 0,
			"Gear Neutral Switch": 0,
			"Engine Run Switch": 0,
			"Anti Lag Switch": 0,
			"Brake State": 0,
			"Traction Switch": 0,
			"Launch Switch": 0,
			"Pit Switch": 0,
			"Engine OilPressure Low Switch": 0,
			"Boost Limit Disable Switch": 0,
			"Throttle Pedal Translation Sw": 0,
			"Race Time Reset Switch": 0,
			"Engine Run Hours Total": 0,
			"Fuel Closed Loop Ctrl B1 Trim": 0,
			"Fuel Closed Loop Ctrl B2 Trim": 0,
			"Transmission Temperature": 0,
			"Fuel Tank Level": 0,
			"M1 General 0x640 Version No": 0,
			"Engine Speed": 0,
			"Inlet Manifold Pressure": 0,
			"Inlet Air Temperature": 0,
			"Throttle Position": 0,
			"Fuel Volume": 0,
			"Fuel Mixture Aim": 0,
			"Fuel Pressure Sensor": 0,
			"Fuel Inj Primary Duty Cycle": 0,
			"Engine Efficiency": 0,
			"Throttle Pedal": 0,
			"Engine Load": 0,
			"Ignition Timing": 0,
			"Fuel Timing Primary": 0,
			"Ignition Cyl 1 Knock Level": 0,
			"Ignition Cyl 2 Knock Level": 0,
			"Ignition Cyl 3 Knock Level": 0,
			"Ignition Cyl 4 Knock Level": 0,
			"Ignition Cyl 5 Knock Level": 0,
			"Ignition Cyl 6 Knock Level": 0,
			"Ignition Cyl 7 Knock Level": 0,
			"Ignition Cyl 8 Knock Level": 0,
			"Ignition Output Cut Count": 0,
			"Fuel Output Cut Count": 0,
			"Ignition Output Cut Average": 0,
			"Fuel Output Cut Average": 0,
			"Fuel Cyl1 Prim Pulse Width 1": 0,
			"Ignition Cut State": 0,
			"Ignition Timing State": 0,
			"Engine Oil Pressure": 0,
			"Boost Pressure": 0,
			"Boost Aim": 0,
			"Boost Actuator Duty Cycle": 0,
			"Gear Lever Force Sensor": 0,
			"Inlet Camshaft Aim": 0,
			"add: 0, mask:0xFFFF": 0,
			"Inlet Camshaft Bank1 Position": 0,
			"Inlet Camshaft Bank2 Position": 0,
			"Inlet Cam Bank1 Duty Cycle": 0,
			"Inlet Cam Bank2 Duty Cycle": 0,
			"Exhaust Camshaft Aim": 0,
			"Exhaust Camshaft Bank1 Pos": 0,
			"Exhaust Camshaft Bank2 Pos": 0,
			"Exhaust Cam Bank1 Duty Cycle": 0,
			"Exhaust Cam Bank2 Duty Cycle": 0,
			"Wheel Speed FL": 0,
			"Wheel Speed FR": 0,
			"Wheel Speed RL": 0,
			"Wheel Speed RR": 0,
		}
		if 0x10011014000 in data:
			msg = data[0x10011014000]
			data = bytes.fromhex(msg["data"])
			result["Coolant Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10111014000 in data:
			msg = data[0x10111014000]
			data = bytes.fromhex(msg["data"])
			result["Engine Oil Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10211014000 in data:
			msg = data[0x10211014000]
			data = bytes.fromhex(msg["data"])
			result["Fuel Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10311014000 in data:
			msg = data[0x10311014000]
			data = bytes.fromhex(msg["data"])
			result["Ambient Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10411014000 in data:
			msg = data[0x10411014000]
			data = bytes.fromhex(msg["data"])
			result["Airbox Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x105110100 in data:
			msg = data[0x105110100]
			data = bytes.fromhex(msg["data"])
			result["Bat Volts ECU"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x110621100 in data:
			msg = data[0x110621100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Used M1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11021100 in data:
			msg = data[0x11021100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11221100 in data:
			msg = data[0x11221100]
			data = bytes.fromhex(msg["data"])
			result["Engine Load Average"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11421600 in data:
			msg = data[0x11421600]
			data = bytes.fromhex(msg["data"])
			result["Engine Speed Limit"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x116210100 in data:
			msg = data[0x116210100]
			data = bytes.fromhex(msg["data"])
			result["Ambient Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x112011100 in data:
			msg = data[0x112011100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 1 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x212111100 in data:
			msg = data[0x212111100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 2 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x312211100 in data:
			msg = data[0x312211100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 3 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x412311100 in data:
			msg = data[0x412311100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 4 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x512411100 in data:
			msg = data[0x512411100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 5 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x612511100 in data:
			msg = data[0x612511100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 6 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x712611100 in data:
			msg = data[0x712611100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 7 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x812711100 in data:
			msg = data[0x812711100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 8 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13021100 in data:
			msg = data[0x13021100]
			data = bytes.fromhex(msg["data"])
			result["Engine Run Time"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13221100 in data:
			msg = data[0x13221100]
			data = bytes.fromhex(msg["data"])
			result["ECU Uptime"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13411100 in data:
			msg = data[0x13411100]
			data = bytes.fromhex(msg["data"])
			result["Warning Source"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x135111001 in data:
			msg = data[0x135111001]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pressure Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x135112002 in data:
			msg = data[0x135112002]
			data = bytes.fromhex(msg["data"])
			result["Crankcase Pressure Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x135118008 in data:
			msg = data[0x135118008]
			data = bytes.fromhex(msg["data"])
			result["Engine Oil Pressure Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13511160010 in data:
			msg = data[0x13511160010]
			data = bytes.fromhex(msg["data"])
			result["Engine Oil Temp Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13511320020 in data:
			msg = data[0x13511320020]
			data = bytes.fromhex(msg["data"])
			result["Engine Speed Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13511640040 in data:
			msg = data[0x13511640040]
			data = bytes.fromhex(msg["data"])
			result["Coolant Pressure Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x135111280080 in data:
			msg = data[0x135111280080]
			data = bytes.fromhex(msg["data"])
			result["Coolant Temperature Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x136111280080 in data:
			msg = data[0x136111280080]
			data = bytes.fromhex(msg["data"])
			result["Knock Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14011100 in data:
			msg = data[0x14011100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pump State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1401116000 in data:
			msg = data[0x1401116000]
			data = bytes.fromhex(msg["data"])
			result["Engine State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14111100 in data:
			msg = data[0x14111100]
			data = bytes.fromhex(msg["data"])
			result["Launch State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1411116000 in data:
			msg = data[0x1411116000]
			data = bytes.fromhex(msg["data"])
			result["Anti Lag State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1421116 in data:
			msg = data[0x1421116]
			data = bytes.fromhex(msg["data"])
			result["Boost Aim State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x000 in data:
			msg = data[0x000]
			data = bytes.fromhex(msg["data"])
			result["add: 0, mask:0x F0"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14311100 in data:
			msg = data[0x14311100]
			data = bytes.fromhex(msg["data"])
			result["Fuel State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1431116000 in data:
			msg = data[0x1431116000]
			data = bytes.fromhex(msg["data"])
			result["Engine Overrun State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14411100 in data:
			msg = data[0x14411100]
			data = bytes.fromhex(msg["data"])
			result["Knock State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1441116000 in data:
			msg = data[0x1441116000]
			data = bytes.fromhex(msg["data"])
			result["Fuel Purge State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14511100 in data:
			msg = data[0x14511100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Closed Loop State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1451116000 in data:
			msg = data[0x1451116000]
			data = bytes.fromhex(msg["data"])
			result["Throttle Aim State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14611100 in data:
			msg = data[0x14611100]
			data = bytes.fromhex(msg["data"])
			result["Gear"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1461116000 in data:
			msg = data[0x1461116000]
			data = bytes.fromhex(msg["data"])
			result["Engine Speed Reference State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14711100 in data:
			msg = data[0x14711100]
			data = bytes.fromhex(msg["data"])
			result["Engine Speed Limit State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15011100 in data:
			msg = data[0x15011100]
			data = bytes.fromhex(msg["data"])
			result["Launch Diagnostic"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1501116000 in data:
			msg = data[0x1501116000]
			data = bytes.fromhex(msg["data"])
			result["Anti Lag Diagnostic"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15111100 in data:
			msg = data[0x15111100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Cut State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1511116000 in data:
			msg = data[0x1511116000]
			data = bytes.fromhex(msg["data"])
			result["Boost Control Diagnostic"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1521116000 in data:
			msg = data[0x1521116000]
			data = bytes.fromhex(msg["data"])
			result["Fuel Closed Loop Diagnostic"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x153111001 in data:
			msg = data[0x153111001]
			data = bytes.fromhex(msg["data"])
			result["Gear Neutral Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x153112002 in data:
			msg = data[0x153112002]
			data = bytes.fromhex(msg["data"])
			result["Engine Run Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x153114004 in data:
			msg = data[0x153114004]
			data = bytes.fromhex(msg["data"])
			result["Anti Lag Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x153118008 in data:
			msg = data[0x153118008]
			data = bytes.fromhex(msg["data"])
			result["Brake State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15311160010 in data:
			msg = data[0x15311160010]
			data = bytes.fromhex(msg["data"])
			result["Traction Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15311320020 in data:
			msg = data[0x15311320020]
			data = bytes.fromhex(msg["data"])
			result["Launch Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15311640040 in data:
			msg = data[0x15311640040]
			data = bytes.fromhex(msg["data"])
			result["Pit Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x153111280080 in data:
			msg = data[0x153111280080]
			data = bytes.fromhex(msg["data"])
			result["Engine OilPressure Low Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15411160010 in data:
			msg = data[0x15411160010]
			data = bytes.fromhex(msg["data"])
			result["Boost Limit Disable Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15511320020 in data:
			msg = data[0x15511320020]
			data = bytes.fromhex(msg["data"])
			result["Throttle Pedal Translation Sw"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15511640040 in data:
			msg = data[0x15511640040]
			data = bytes.fromhex(msg["data"])
			result["Race Time Reset Switch"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x16021100 in data:
			msg = data[0x16021100]
			data = bytes.fromhex(msg["data"])
			result["Engine Run Hours Total"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x116215110000 in data:
			msg = data[0x116215110000]
			data = bytes.fromhex(msg["data"])
			result["Fuel Closed Loop Ctrl B1 Trim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x216315110000 in data:
			msg = data[0x216315110000]
			data = bytes.fromhex(msg["data"])
			result["Fuel Closed Loop Ctrl B2 Trim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x16411014000 in data:
			msg = data[0x16411014000]
			data = bytes.fromhex(msg["data"])
			result["Transmission Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x165110100 in data:
			msg = data[0x165110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Tank Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1064016711100 in data:
			msg = data[0x1064016711100]
			data = bytes.fromhex(msg["data"])
			result["M1 General 0x640 Version No"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1021600 in data:
			msg = data[0x1021600]
			data = bytes.fromhex(msg["data"])
			result["Engine Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1221100 in data:
			msg = data[0x1221100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Manifold Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1421100 in data:
			msg = data[0x1421100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Air Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1621100 in data:
			msg = data[0x1621100]
			data = bytes.fromhex(msg["data"])
			result["Throttle Position"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2021100 in data:
			msg = data[0x2021100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Volume"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2221100 in data:
			msg = data[0x2221100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Mixture Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2421100 in data:
			msg = data[0x2421100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pressure Sensor"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x26110100 in data:
			msg = data[0x26110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Inj Primary Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x27110100 in data:
			msg = data[0x27110100]
			data = bytes.fromhex(msg["data"])
			result["Engine Efficiency"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3021100 in data:
			msg = data[0x3021100]
			data = bytes.fromhex(msg["data"])
			result["Throttle Pedal"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3221100 in data:
			msg = data[0x3221100]
			data = bytes.fromhex(msg["data"])
			result["Engine Load"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3421100 in data:
			msg = data[0x3421100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Timing"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3621100 in data:
			msg = data[0x3621100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Timing Primary"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x140110100 in data:
			msg = data[0x140110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 1 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x241110100 in data:
			msg = data[0x241110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 2 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x342110100 in data:
			msg = data[0x342110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 3 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x443110100 in data:
			msg = data[0x443110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 4 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x544110100 in data:
			msg = data[0x544110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 5 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x645110100 in data:
			msg = data[0x645110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 6 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x746110100 in data:
			msg = data[0x746110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 7 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x847110100 in data:
			msg = data[0x847110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 8 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x5011100 in data:
			msg = data[0x5011100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Output Cut Count"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x5111100 in data:
			msg = data[0x5111100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Output Cut Count"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x52110100 in data:
			msg = data[0x52110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Output Cut Average"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x53110100 in data:
			msg = data[0x53110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Output Cut Average"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11541100100 in data:
			msg = data[0x11541100100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Cyl1 Prim Pulse Width 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x5511100 in data:
			msg = data[0x5511100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cut State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x551116000 in data:
			msg = data[0x551116000]
			data = bytes.fromhex(msg["data"])
			result["Ignition Timing State"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x5621100 in data:
			msg = data[0x5621100]
			data = bytes.fromhex(msg["data"])
			result["Engine Oil Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6021100 in data:
			msg = data[0x6021100]
			data = bytes.fromhex(msg["data"])
			result["Boost Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6221100 in data:
			msg = data[0x6221100]
			data = bytes.fromhex(msg["data"])
			result["Boost Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x66110100 in data:
			msg = data[0x66110100]
			data = bytes.fromhex(msg["data"])
			result["Boost Actuator Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x67150009800 in data:
			msg = data[0x67150009800]
			data = bytes.fromhex(msg["data"])
			result["Gear Lever Force Sensor"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x70211 in data:
			msg = data[0x70211]
			data = bytes.fromhex(msg["data"])
			result["Inlet Camshaft Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x00 in data:
			msg = data[0x00]
			data = bytes.fromhex(msg["data"])
			result["add: 0, mask:0xFFFF"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x17221100 in data:
			msg = data[0x17221100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Camshaft Bank1 Position"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x27421100 in data:
			msg = data[0x27421100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Camshaft Bank2 Position"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x176110100 in data:
			msg = data[0x176110100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Cam Bank1 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x277110100 in data:
			msg = data[0x277110100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Cam Bank2 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x8021100 in data:
			msg = data[0x8021100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Camshaft Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x18221100 in data:
			msg = data[0x18221100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Camshaft Bank1 Pos"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x28421100 in data:
			msg = data[0x28421100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Camshaft Bank2 Pos"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x186110100 in data:
			msg = data[0x186110100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Cam Bank1 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x287110100 in data:
			msg = data[0x287110100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Cam Bank2 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9021100 in data:
			msg = data[0x9021100]
			data = bytes.fromhex(msg["data"])
			result["Wheel Speed FL"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9221100 in data:
			msg = data[0x9221100]
			data = bytes.fromhex(msg["data"])
			result["Wheel Speed FR"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9421100 in data:
			msg = data[0x9421100]
			data = bytes.fromhex(msg["data"])
			result["Wheel Speed RL"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9621100 in data:
			msg = data[0x9621100]
			data = bytes.fromhex(msg["data"])
			result["Wheel Speed RR"] = int.from_bytes(data[0:2], byteorder='little')


		return result

	def _parse_BUS_2(data:dict) -> dict:
		'Parses [context unknown] data from BUS_2'
		result = {
			"Ignition Cyl 9 Knock Level": 0,
			"Ignition Cyl 10 Knock Level": 0,
			"Ignition Cyl 11 Knock Level": 0,
			"Ignition Cyl 12 Knock Level": 0,
			"Vehicle Speed": 0,
			"Ignition Cyl 9 Trim Knock": 0,
			"Ignition Cyl 10 Trim Knock": 0,
			"Ignition Cyl 11 Trim Knock": 0,
			"Ignition Cyl 12 Trim Knock": 0,
			"M1 General 0x650 Version No": 0,
			"Lap Time": 0,
			"Running Lap Time": 0,
			"Lap Number": 0,
			"Lap Distance": 0,
			"Differential Temperature": 0,
			"Driver Rotary Switch 7": 0,
			"Driver Rotary Switch 8": 0,
			"Brake Temp FL": 0,
			"Brake Temp FR": 0,
			"Brake Temp RL": 0,
			"Brake Temp RR": 0,
			"Exhaust Pressure Bank 1": 0,
			"Exhaust Pressure Bank 2": 0,
			"Engine Crankcase Pressure": 0,
			"Alternator Current": 0,
			"Knock Threshold": 0,
			"Logging System 1 Used": 0,
			"Vehicle Speed Limit Pit Limit": 0,
			"Driver Rotary Switch 1": 0,
			"Driver Rotary Switch 2": 0,
			"Driver Rotary Switch 3": 0,
			"Driver Rotary Switch 4": 0,
			"Driver Rotary Switch 5": 0,
			"Driver Rotary Switch 6": 0,
			"Driver Switch 8": 0,
			"Driver Switch 7": 0,
			"Driver Switch 6": 0,
			"Driver Switch 5": 0,
			"Driver Switch 4": 0,
			"Driver Switch 3": 0,
			"Driver Switch 2": 0,
			"Driver Switch 1": 0,
			"Exhaust Lambda": 0,
			"Exhaust Lambda Bank 1": 0,
			"Exhaust Lambda Bank 2": 0,
			"Exhaust Temp Bank 1": 0,
			"Exhaust Temp Bank 2": 0,
			"Fuel Inj Sec Contribution": 0,
			"add: 0, mask:0xFFFF": 0,
			"Fuel Timing Secondary": 0,
			"Fuel Inj Secondary Duty Cycle": 0,
			"Fuel Pres Direct": 0,
			"Fuel Pres Direct Aim": 0,
			"Fuel Pres Direct Ctrl": 0,
			"Fuel Pres Direct Ctrl FF": 0,
			"Fuel Pres Direct Ctrl Prop": 0,
			"Fuel Pres Direct Ctrl Int": 0,
			"Fuel Pres Direct B2": 0,
			"Fuel Pres Direct B2 Aim": 0,
			"Fuel Pres Direct B2 Ctrl": 0,
			"Fuel Pres Direct B2 Ctrl FF": 0,
			"Fuel Pres Direct B2 Ctrl Prop": 0,
			"Fuel Pres Direct B2 Ctrl Int": 0,
			"Brake Pressure Front": 0,
			"Brake Pressure Rear": 0,
			"Coolant Pressure": 0,
			"Steering Pressure": 0,
			"Steering Angle": 0,
			"Inlet Mass Flow": 0,
			"Airbox Mass Flow": 0,
			"Fuel Flow": 0,
			"Fuel Inj Primary Press": 0,
			"Fuel Inj Secondary Press": 0,
			"Gear Input Shaft Speed": 0,
			"Gear Output Shaft Speed": 0,
			"Vehicle Accel Lateral": 0,
			"Vehicle Accel Long": 0,
			"Vehicle Accel Vert": 0,
			"Vehicle Yaw Rate": 0,
		}
		if 0x9100110100 in data:
			msg = data[0x9100110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 9 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10101110100 in data:
			msg = data[0x10101110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 10 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11102110100 in data:
			msg = data[0x11102110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 11 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12103110100 in data:
			msg = data[0x12103110100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 12 Knock Level"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10421100 in data:
			msg = data[0x10421100]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x911011100 in data:
			msg = data[0x911011100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 9 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1011111100 in data:
			msg = data[0x1011111100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 10 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1111211100 in data:
			msg = data[0x1111211100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 11 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1211311100 in data:
			msg = data[0x1211311100]
			data = bytes.fromhex(msg["data"])
			result["Ignition Cyl 12 Trim Knock"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x1065011411100 in data:
			msg = data[0x1065011411100]
			data = bytes.fromhex(msg["data"])
			result["M1 General 0x650 Version No"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12021100 in data:
			msg = data[0x12021100]
			data = bytes.fromhex(msg["data"])
			result["Lap Time"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12221100 in data:
			msg = data[0x12221100]
			data = bytes.fromhex(msg["data"])
			result["Running Lap Time"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12421100 in data:
			msg = data[0x12421100]
			data = bytes.fromhex(msg["data"])
			result["Lap Number"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12621100 in data:
			msg = data[0x12621100]
			data = bytes.fromhex(msg["data"])
			result["Lap Distance"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13021100 in data:
			msg = data[0x13021100]
			data = bytes.fromhex(msg["data"])
			result["Differential Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x713211100 in data:
			msg = data[0x713211100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 7"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x813311100 in data:
			msg = data[0x813311100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 8"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x140211000 in data:
			msg = data[0x140211000]
			data = bytes.fromhex(msg["data"])
			result["Brake Temp FL"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x142211000 in data:
			msg = data[0x142211000]
			data = bytes.fromhex(msg["data"])
			result["Brake Temp FR"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x144211000 in data:
			msg = data[0x144211000]
			data = bytes.fromhex(msg["data"])
			result["Brake Temp RL"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x146211000 in data:
			msg = data[0x146211000]
			data = bytes.fromhex(msg["data"])
			result["Brake Temp RR"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x115021100 in data:
			msg = data[0x115021100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Pressure Bank 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x215221100 in data:
			msg = data[0x215221100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Pressure Bank 2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15421100 in data:
			msg = data[0x15421100]
			data = bytes.fromhex(msg["data"])
			result["Engine Crankcase Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x156211000 in data:
			msg = data[0x156211000]
			data = bytes.fromhex(msg["data"])
			result["Alternator Current"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x16021100 in data:
			msg = data[0x16021100]
			data = bytes.fromhex(msg["data"])
			result["Knock Threshold"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x116221100 in data:
			msg = data[0x116221100]
			data = bytes.fromhex(msg["data"])
			result["Logging System 1 Used"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x16421100 in data:
			msg = data[0x16421100]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Speed Limit Pit Limit"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11011100 in data:
			msg = data[0x11011100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x21111100 in data:
			msg = data[0x21111100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x31211100 in data:
			msg = data[0x31211100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 3"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x41311100 in data:
			msg = data[0x41311100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 4"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x51411100 in data:
			msg = data[0x51411100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 5"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x61511100 in data:
			msg = data[0x61511100]
			data = bytes.fromhex(msg["data"])
			result["Driver Rotary Switch 6"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x817111001 in data:
			msg = data[0x817111001]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 8"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x717112002 in data:
			msg = data[0x717112002]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 7"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x617114004 in data:
			msg = data[0x617114004]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 6"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x517118008 in data:
			msg = data[0x517118008]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 5"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x41711160010 in data:
			msg = data[0x41711160010]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 4"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x31711320020 in data:
			msg = data[0x31711320020]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 3"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x21711640040 in data:
			msg = data[0x21711640040]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x117111280080 in data:
			msg = data[0x117111280080]
			data = bytes.fromhex(msg["data"])
			result["Driver Switch 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2011100 in data:
			msg = data[0x2011100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Lambda"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12211100 in data:
			msg = data[0x12211100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Lambda Bank 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x22311100 in data:
			msg = data[0x22311100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Lambda Bank 2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12421100 in data:
			msg = data[0x12421100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Temp Bank 1"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x22621100 in data:
			msg = data[0x22621100]
			data = bytes.fromhex(msg["data"])
			result["Exhaust Temp Bank 2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x30211 in data:
			msg = data[0x30211]
			data = bytes.fromhex(msg["data"])
			result["Fuel Inj Sec Contribution"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x00 in data:
			msg = data[0x00]
			data = bytes.fromhex(msg["data"])
			result["add: 0, mask:0xFFFF"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3221100 in data:
			msg = data[0x3221100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Timing Secondary"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x34110100 in data:
			msg = data[0x34110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Inj Secondary Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x4021100 in data:
			msg = data[0x4021100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x4221100 in data:
			msg = data[0x4221100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x4415100 in data:
			msg = data[0x4415100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct Ctrl"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x45110100 in data:
			msg = data[0x45110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct Ctrl FF"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x46110100 in data:
			msg = data[0x46110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct Ctrl Prop"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x47110100 in data:
			msg = data[0x47110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct Ctrl Int"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x25021100 in data:
			msg = data[0x25021100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x25221100 in data:
			msg = data[0x25221100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2 Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x25415100 in data:
			msg = data[0x25415100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2 Ctrl"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x255110100 in data:
			msg = data[0x255110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2 Ctrl FF"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x256110100 in data:
			msg = data[0x256110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2 Ctrl Prop"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x257110100 in data:
			msg = data[0x257110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Pres Direct B2 Ctrl Int"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6021100 in data:
			msg = data[0x6021100]
			data = bytes.fromhex(msg["data"])
			result["Brake Pressure Front"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6221100 in data:
			msg = data[0x6221100]
			data = bytes.fromhex(msg["data"])
			result["Brake Pressure Rear"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6421100 in data:
			msg = data[0x6421100]
			data = bytes.fromhex(msg["data"])
			result["Coolant Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x6621100 in data:
			msg = data[0x6621100]
			data = bytes.fromhex(msg["data"])
			result["Steering Pressure"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x7021100 in data:
			msg = data[0x7021100]
			data = bytes.fromhex(msg["data"])
			result["Steering Angle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x7221100 in data:
			msg = data[0x7221100]
			data = bytes.fromhex(msg["data"])
			result["Inlet Mass Flow"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x7421100 in data:
			msg = data[0x7421100]
			data = bytes.fromhex(msg["data"])
			result["Airbox Mass Flow"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x7621100 in data:
			msg = data[0x7621100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Flow"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x8021100 in data:
			msg = data[0x8021100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Inj Primary Press"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x8221100 in data:
			msg = data[0x8221100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Inj Secondary Press"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x8421600 in data:
			msg = data[0x8421600]
			data = bytes.fromhex(msg["data"])
			result["Gear Input Shaft Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x8621600 in data:
			msg = data[0x8621600]
			data = bytes.fromhex(msg["data"])
			result["Gear Output Shaft Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9021100 in data:
			msg = data[0x9021100]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Accel Lateral"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9221100 in data:
			msg = data[0x9221100]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Accel Long"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x9421100 in data:
			msg = data[0x9421100]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Accel Vert"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x962501800 in data:
			msg = data[0x962501800]
			data = bytes.fromhex(msg["data"])
			result["Vehicle Yaw Rate"] = int.from_bytes(data[0:2], byteorder='little')


		return result

	def _parse_BUS_3(data:dict) -> dict:
		'Parses [context unknown] data from BUS_3'
		result = {
			"Fuel Comp Sensor Diag": 0,
			"Alt Fuel Mode": 0,
			"Alt Fuel Timing Prim Blend": 0,
			"Alt Fuel Timing Sec Blend": 0,
			"Alt Fuel Ign Timing Blend": 0,
			"Alt Fuel Mix Aim Blend": 0,
			"Fuel Composition": 0,
			"Alt Fuel Ign Timing": 0,
			"Alt Fuel Timing Prim": 0,
			"Alt Fuel Timing Sec": 0,
			"Alt Fuel Mix Aim": 0,
			"Alt Fuel Pressure Sensor": 0,
			"Alt Fuel Temperature": 0,
			"Alt Fuel Cont Efficiency": 0,
			"Alt Fuel Pump Active": 0,
			"Alt Fuel Press Warning": 0,
			"Alt Fuel Pump State": 0,
		}
		if 0x1011100 in data:
			msg = data[0x1011100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Comp Sensor Diag"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x101116000 in data:
			msg = data[0x101116000]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Mode"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x11110100 in data:
			msg = data[0x11110100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Timing Prim Blend"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x12110100 in data:
			msg = data[0x12110100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Timing Sec Blend"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x13110100 in data:
			msg = data[0x13110100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Ign Timing Blend"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x14110100 in data:
			msg = data[0x14110100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Mix Aim Blend"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x15110100 in data:
			msg = data[0x15110100]
			data = bytes.fromhex(msg["data"])
			result["Fuel Composition"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x16110200 in data:
			msg = data[0x16110200]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Ign Timing"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2021100 in data:
			msg = data[0x2021100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Timing Prim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2221100 in data:
			msg = data[0x2221100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Timing Sec"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x2421100 in data:
			msg = data[0x2421100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Mix Aim"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3021100 in data:
			msg = data[0x3021100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Pressure Sensor"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x3211014000 in data:
			msg = data[0x3211014000]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Temperature"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x33110100 in data:
			msg = data[0x33110100]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Cont Efficiency"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x34111001 in data:
			msg = data[0x34111001]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Pump Active"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x34112002 in data:
			msg = data[0x34112002]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Press Warning"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x341116000 in data:
			msg = data[0x341116000]
			data = bytes.fromhex(msg["data"])
			result["Alt Fuel Pump State"] = int.from_bytes(data[0:2], byteorder='little')


		return result

	def _parse_BUS_4(data:dict) -> dict:
		'Parses [context unknown] data from BUS_4'
		result = {
			"Aux Output 1 Duty Cycle": 0,
			"Aux Output 2 Duty Cycle": 0,
			"Aux Output 3 Duty Cycle": 0,
			"Aux Output 4 Duty Cycle": 0,
			"Aux Output 5 Duty Cycle": 0,
			"M1 General 0x6A0 Version No": 0,
			"Turbo Bank 1 Speed": 0,
			"Turbo Bank 1 Temp Inlet": 0,
			"Turbo Bank 1 Temp Outlet": 0,
			"Turbo Bank 1 Pressure Inlet": 0,
			"Turbo Bank 2 Speed": 0,
			"Turbo Bank 2 Temp Inlet": 0,
			"Turbo Bank 2 Temp Outlet": 0,
		}
		if 0x11021100 in data:
			msg = data[0x11021100]
			data = bytes.fromhex(msg["data"])
			result["Aux Output 1 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x21221100 in data:
			msg = data[0x21221100]
			data = bytes.fromhex(msg["data"])
			result["Aux Output 2 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x31421100 in data:
			msg = data[0x31421100]
			data = bytes.fromhex(msg["data"])
			result["Aux Output 3 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x41621100 in data:
			msg = data[0x41621100]
			data = bytes.fromhex(msg["data"])
			result["Aux Output 4 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x52021100 in data:
			msg = data[0x52021100]
			data = bytes.fromhex(msg["data"])
			result["Aux Output 5 Duty Cycle"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x10606011100 in data:
			msg = data[0x10606011100]
			data = bytes.fromhex(msg["data"])
			result["M1 General 0x6A0 Version No"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x170210600 in data:
			msg = data[0x170210600]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 1 Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x172111400 in data:
			msg = data[0x172111400]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 1 Temp Inlet"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x173111400 in data:
			msg = data[0x173111400]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 1 Temp Outlet"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x17421100 in data:
			msg = data[0x17421100]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 1 Pressure Inlet"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x280210600 in data:
			msg = data[0x280210600]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 2 Speed"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x282111400 in data:
			msg = data[0x282111400]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 2 Temp Inlet"] = int.from_bytes(data[0:2], byteorder='little')

		if 0x283111400 in data:
			msg = data[0x283111400]
			data = bytes.fromhex(msg["data"])
			result["Turbo Bank 2 Temp Outlet"] = int.from_bytes(data[0:2], byteorder='little')


		return result

class TestPackage:
	def _test_RX_GPS():
		testBytes = bytes([1, 2])
		result = ParsePackage._parse_RX_GPS(data=testBytes)
		print(f"RX_GPS outputs:", result)
		assert result == 1, "Expected 1, got " + result

	def _test_BUS_1():
		testBytes = bytes([1, 2])
		result = ParsePackage._parse_BUS_1(data=testBytes)
		print(f"BUS_1 outputs:", result)
		assert result == 1, "Expected 1, got " + result

	def _test_BUS_2():
		testBytes = bytes([1, 2])
		result = ParsePackage._parse_BUS_2(data=testBytes)
		print(f"BUS_2 outputs:", result)
		assert result == 1, "Expected 1, got " + result

	def _test_BUS_3():
		testBytes = bytes([1, 2])
		result = ParsePackage._parse_BUS_3(data=testBytes)
		print(f"BUS_3 outputs:", result)
		assert result == 1, "Expected 1, got " + result

	def _test_BUS_4():
		testBytes = bytes([1, 2])
		result = ParsePackage._parse_BUS_4(data=testBytes)
		print(f"BUS_4 outputs:", result)
		assert result == 1, "Expected 1, got " + result

	def runAll():
		TestPackage._test_RX_GPS()
		TestPackage._test_BUS_1()
		TestPackage._test_BUS_2()
		TestPackage._test_BUS_3()
		TestPackage._test_BUS_4()

if __name__ == "__main__":
	TestPackage.runAll()