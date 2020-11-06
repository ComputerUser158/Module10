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

	def test_student_string(self):
		self.assertEqual(str(self.student), "Collins, Rawley has major Programming with gpa: 0.0")

	def test_object_not_created_error_last_name(self):
		with self.assertRaises(ValueError):
			stu = t.Student("1234kljfdi", "Rawley", "Programming", 0.0)

	def test_object_not_created_error_first_name(self):
		with self.assertRaises(ValueError):
			stu = t.Student("Collins", "1234kljkjg", "Programming", 0.0)

	def test_object_not_created_error_major(self):
		with self.assertRaises(ValueError):
			stu = t.Student("Collins", "Rawley", "Music", 0.0)


if __name__ == '__main__':
	unittest.main()
