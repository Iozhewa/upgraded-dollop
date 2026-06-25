#!/usr/bin/env python3
class ParsePackage:
	def _parse_RX_GPS(self, can_data:dict) -> dict:
		'Parse __ data from RX_GPS'
		pass

	def _parse_BUS_1(self, can_data:dict) -> dict:
		'Parse __ data from BUS_1'
		pass

	def _parse_BUS_2(self, can_data:dict) -> dict:
		'Parse __ data from BUS_2'
		pass

	def _parse_BUS_3(self, can_data:dict) -> dict:
		'Parse __ data from BUS_3'
		pass

	def _parse_BUS_4(self, can_data:dict) -> dict:
		'Parse __ data from BUS_4'
		pass

class TestPackage:
	def _test_RX_GPS(self):
		pass

	def _test_BUS_1(self):
		pass

	def _test_BUS_2(self):
		pass

	def _test_BUS_3(self):
		pass

	def _test_BUS_4(self):
		pass

	def runAll(self):
		self._test_RX_GPS()
		self._test_BUS_1()
		self._test_BUS_2()
		self._test_BUS_3()
		self._test_BUS_4()

if __name__ == "__main__":
	TestPackage.runAll()