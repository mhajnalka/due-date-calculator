import unittest
import main
from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_calculate(self):
        # Assert to check when week changes
        result = main.calculate(input_date=datetime.strptime('2021-04-27 09:42:00', '%Y-%m-%d %H:%M:%S'),
                                turnaround=39)
        self.assertEqual(result, datetime.strptime('2021-05-03 16:42:00', '%Y-%m-%d %H:%M:%S'))
        # Assert to check day change
        result = main.calculate(input_date=datetime.strptime('2021-04-27 09:42:00', '%Y-%m-%d %H:%M:%S'),
                                turnaround=8)
        self.assertEqual(result, datetime.strptime('2021-04-28 09:42:00', '%Y-%m-%d %H:%M:%S'))
        # Assert to check negative turnaround values
        result = main.calculate(input_date=datetime.strptime('2021-04-27 09:42:00', '%Y-%m-%d %H:%M:%S'),
                                turnaround=-1)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
