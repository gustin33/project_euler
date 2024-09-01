import numpy as np
import time
from tqdm import tqdm

class Sudoku:
    def __init__(self, board, silent=False):
        self.board = board
        self.silent = silent
        self.update_possible_values()

    def update_possible_values(self):
        zero_coords = np.where(self.board == 0)
        unknown_coordinates = list(zip(zero_coords[0], zero_coords[1]))
        self.possible_values = {
            coordinate: [
                i
                for i in range(1, 10)
                if not i
                in self.get_cell_neighbors_values(coordinate).union(
                    self.get_X_neighbors_values(coordinate)
                )
            ]
            for coordinate in unknown_coordinates
        }

    def get_cell_neighbors_values(self, coordinate):
        row, col = coordinate
        values = set(self.board[row, :].tolist() + self.board[:, col].tolist())
        box_row_start, box_col_start = 3 * (row // 3), 3 * (col // 3)
        values.update(self.board[box_row_start:box_row_start + 3, box_col_start:box_col_start + 3].flatten())
        return values

    def get_X_neighbors_values(self, coordinate):
        row, col = coordinate
        values = set()
        for r in range(9):
            if r != row and self.board[r, col] != 0:
                values.add(self.board[r, col])
        for c in range(9):
            if c != col and self.board[row, c] != 0:
                values.add(self.board[row, c])
        return values

    def find_empty_cell(self):
        for row in range(9):
            for col in range(9):
                if self.board[row, col] == 0:
                    return (row, col)
        return None

    def is_valid(self, num, row, col):
        if num in self.board[row, :]:
            return False
        if num in self.board[:, col]:
            return False
        box_row_start, box_col_start = 3 * (row // 3), 3 * (col // 3)
        if num in self.board[box_row_start:box_row_start + 3, box_col_start:box_col_start + 3]:
            return False
        return True

    def naked_single(self):
        made_progress = False
        for (row, col), values in self.possible_values.items():
            if len(values) == 1:
                self.board[row, col] = values[0]
                self.update_possible_values()
                made_progress = True
        return made_progress

    def hidden_single(self):
        made_progress = False

        # Check rows
        for num in range(1, 10):
            for row in range(9):
                possible_positions = [col for col in range(9) if num in self.possible_values.get((row, col), [])]
                if len(possible_positions) == 1:
                    col = possible_positions[0]
                    if self.board[row, col] == 0:
                        self.board[row, col] = num
                        self.update_possible_values()
                        made_progress = True

        # Check columns
        for num in range(1, 10):
            for col in range(9):
                possible_positions = [row for row in range(9) if num in self.possible_values.get((row, col), [])]
                if len(possible_positions) == 1:
                    row = possible_positions[0]
                    if self.board[row, col] == 0:
                        self.board[row, col] = num
                        self.update_possible_values()
                        made_progress = True

        # Check boxes
        for num in range(1, 10):
            for box_row in range(0, 9, 3):
                for box_col in range(0, 9, 3):
                    possible_positions = [
                        (r, c)
                        for r in range(box_row, box_row + 3)
                        for c in range(box_col, box_col + 3)
                        if num in self.possible_values.get((r, c), [])
                    ]
                    if len(possible_positions) == 1:
                        row, col = possible_positions[0]
                        if self.board[row, col] == 0:
                            self.board[row, col] = num
                            self.update_possible_values()
                            made_progress = True

        return made_progress

    def solve(self, show_steps=False, output_text=None):
        while True:
            if not (self.naked_single() or self.hidden_single()):
                break
        if self.solve_recursive():
            if output_text:
                np.savetxt(output_text, self.board, fmt='%d')
            if show_steps:
                pprint(self.board)
            return True
        else:
            return False

    def solve_recursive(self):
        empty = self.find_empty_cell()
        if not empty:
            return True  # Solved
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.board[row, col] = num
                if self.solve_recursive():
                    return True
                self.board[row, col] = 0  # Backtrack
        return False

def open_sudoku_file():
    with open("./96_input.txt") as file:
        text = file.readlines()
        sudokus = [text[1 + 10 * i : 10 + 10 * i] for i in range(50)]
        sudokus = [
            np.array([[int(x) for x in list(line.strip("\n"))] for line in sudoku])
            for sudoku in sudokus
        ]
    return sudokus

def get_sum_of_three_digit_numbers(sudokus):
    total_sum = 0
    num_sudokus = len(sudokus)
    
    for index, board in tqdm(enumerate(sudokus), total=num_sudokus, desc="Solving Sudokus"):
        sudoku = Sudoku(board)
        solved = sudoku.solve()
        if solved:
            first_row = sudoku.board[0, :3]  # First row, first three columns
            
            # Form the three-digit number
            if len(first_row) == 3:  # Ensure we have exactly three columns
                three_digit_number = int("".join(map(str, first_row)))
                total_sum += three_digit_number
    
    return total_sum

# Measure the execution time
start_time = time.time()

# Open the Sudoku file and get the Sudokus
sudokus = open_sudoku_file()

# Calculate the sum of all three-digit numbers after solving each Sudoku
sum_of_numbers = get_sum_of_three_digit_numbers(sudokus)

end_time = time.time()
execution_time = end_time - start_time

print(f"The sum of all three-digit numbers formed by the first three columns of the first row is: {sum_of_numbers}")
print(f"Execution time: {execution_time:.2f} seconds")
