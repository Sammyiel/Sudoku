
# Import modules
import unittest
import sudoku_intermediate_level


class TestSudoku_intermediate_level(unittest.TestCase):

    # Method that runs before any test is run
    @classmethod
    def setUpClass(cls) -> None:
        print('===== Your test cases have begun executing =====\n')

    # Method that runs after all tests have run
    @classmethod
    def tearDownClass(cls) -> None:
        print('===== All your test cases have run =====\n')

    # Test that checks the number of filled cells is at most 5
    def test_no_filled_spaces_row(self):
        self.assertLessEqual(sudoku_intermediate_level.Sudoku_Intermediate_Level.fill_5_cells(self), 5)

    # Test that checks only single digits are filled
    def test_single_grid_values(self):
        self.assertLess(sudoku_intermediate_level.Sudoku_Intermediate_Level.no_grid_rows(self), 10)
        self.assertLess(sudoku_intermediate_level.Sudoku_Intermediate_Level.no_grid_columns(self), 10)

    # Test that checks the number of columns in the grid is 9
    def test_no_columns(self):
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_columns(self), 9)
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_columns(self) + sudoku_intermediate_level.Sudoku.no_grid_columns(self), 18)
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_columns(self) * sudoku_intermediate_level.Sudoku.no_grid_columns(self), 81)

    # Test that checks the number of rows in the grid
    def test_no_rows(self):
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self), 9)
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self) + sudoku_intermediate_level.Sudoku.no_grid_rows(self), 18)
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self) * sudoku_intermediate_level.Sudoku.no_grid_rows(self), 81)

    # Test that checks that grid is a square grid i.e., n x n
    def test_if_square_grid(self):
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self), sudoku_intermediate_level.Sudoku.no_grid_columns(self))
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self) * sudoku_intermediate_level.Sudoku.no_grid_columns(self), 81)

    # Test that checks number of columns equal that of rows
    def test_equal_rows_columns(self):
        self.assertEqual(sudoku_intermediate_level.Sudoku.no_grid_rows(self), sudoku_intermediate_level.Sudoku.no_grid_columns(self))

if __name__ == '__main__':
    unittest.main()
