import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.student = t.Student('Collins', 'Rawley', 'Programming', 4.0)

	def tearDown(self):
		del self.student

	def test_object_created_required_attributes(self):
		self.assertEqual(self.student.first_name, 'Rawley')
		self.assertEqual(self.student.last_name, 'Collins')
		self.assertEqual(self.student.major, 'Programming')
		self.assertEqual(self.student.gpa, 4.0)


"""
	def test_something(self):
		self.assertEqual(True, False)

	def test_something(self):
		self.assertEqual(True, False)

	def test_something(self):
		self.assertEqual(True, False)

	def test_something(self):
		self.assertEqual(True, False)

	def test_something(self):
		self.assertEqual(True, False)"""


if __name__ == '__main__':
	unittest.main()
