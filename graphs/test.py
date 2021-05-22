import unittest
from main import *


class TestGr(unittest.TestCase):
    def test_from_str_to_dict(self):
        lst = ['date, resource, count, staff_id\n', '2020-01, 2, 10, 4\n', '2020-01, 1, 10, 2\n', '2020-02, 4, 20, 4\n', '2020-09, 1, 44, 1\n', '2020-10, 3, 34, 3\n']
        result = from_str_to_dict(lst)
        print(result)
        expect = [{'date': '2020-01', 'resource': '2', 'count': '10', 'staff_id': '4'}, {'date': '2020-01', 'resource': '1', 'count': '10', 'staff_id': '2'}, {'date': '2020-02', 'resource': '4', 'count': '20', 'staff_id': '4'}, {'date': '2020-09', 'resource': '1', 'count': '44', 'staff_id': '1'}, {'date': '2020-10', 'resource': '3', 'count': '34', 'staff_id': '3'}]
        self.assertEqual(expect, result)

if __name__ == '__main__':
    unittest.main()