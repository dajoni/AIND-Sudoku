import solution
import unittest

class TestNakedTwins(unittest.TestCase):

    def get_simple_grid(self):
        values = {}
        for box in solution.boxes:
            values[box] = ''
        return values

    def assert_grid_empty_except(self, values, except_boxes):
        iter_boxes = [box for box in solution.boxes if box not in except_boxes]
        for box in iter_boxes:
            self.assertEqual(values[box], '')

    def test_naked_twin_in_square(self):
        values = self.get_simple_grid()
        values['A1'] = '12'
        values['A2'] = '12'
        values['B1'] = '123'
        values = solution.naked_twins(values)
        self.assertEqual(values['B1'], '3')
        self.assert_grid_empty_except(values, ['A1', 'A2', 'B1'])

    def test_naked_twin_in_row(self):
        values = self.get_simple_grid()
        values['D4'] = '456'
        values['D5'] = '456'
        values['D6'] = '456'
        values['D7'] = '123456'
        values = solution.naked_twins(values)
        self.assertEqual(values['D7'], '123')
        self.assert_grid_empty_except(values, ['D4', 'D5', 'D6', 'D7'])

    def test_naked_twin_in_column(self):
        values = self.get_simple_grid()
        values['A7'] = '4569'
        values['B7'] = '4569'
        values['C7'] = '4569'
        values['D7'] = '4569'
        values['E7'] = '257'
        values = solution.naked_twins(values)
        self.assertEqual(values['E7'], '27')
        self.assert_grid_empty_except(values, ['A7', 'B7', 'C7', 'D7', 'E7'])



if __name__ == '__main__':
    unittest.main()
