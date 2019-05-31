import unittest
from loader import check
from loader import load_level

class LoaderTestCase(unittest.TestCase):
	"""Tests forloader.py."""

	def test_check_fuction1(self):
		self.assertEqual(check("test/unittest/invalid1.level"), False)
	def test_check_fuction2(self):
		self.assertEqual(check("test/unittest/invalid2.level"), False)
	def test_check_fuction3(self):
		self.assertEqual(check("test/unittest/invalid3.level"), False)
	def test_check_fuction4(self):
		self.assertEqual(check("test/unittest/invalid4.level"), False)
	def test_check_fuction5(self):
		self.assertEqual(check("test/unittest/invalid5.level"), False)
	def test_check_fuction6(self):
		self.assertEqual(check("test/unittest/invalid6.level"), False)
	def test_check_fuction7(self):
		self.assertEqual(check("test/unittest/valid1.level"), True)
	def test_check_fuction8(self):
		self.assertEqual(check("test/unittest/valid2.level"), True)
	def test_check_fuction9(self):
		self.assertEqual(check("test/unittest/valid1.level"), True)
		

if __name__ == '__main__':
	unittest.main()
