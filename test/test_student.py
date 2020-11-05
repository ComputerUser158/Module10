import unittest
from class_definitions import student as t


class MyTestCase(unittest.TestCase):
	def setUp(self):
		self.student = t.Student('Collins', 'Rawley', 'Programming')

	def tearDown(self):
		del self.student

	def test_object_created_required_attributes(self):
		self.assertEqual(self.student.first_name, 'Rawley')
		self.assertEqual(self.student.last_name, 'Collins')
		self.assertEqual(self.student.major, 'Programming')
		self.assertEqual(self.student.gpa, 0.0)

	def test_object_created_all_attributes(self):
		student = t.Student('Collins', 'David', 'Programming', 4.0)
		assert student.first_name == 'David'
		assert student.last_name == 'Collins'
		assert student.major == 'Programming'
		assert student.gpa == 4.0

"""
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
