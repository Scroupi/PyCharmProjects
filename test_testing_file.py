from unittest import TestCase
import testing_file

class Test(TestCase):
    def test_convert_gender(self):
        expected = "MALE"
        actual = testing_file.convert_gender("M")
        self.assertEqual(actual,expected)