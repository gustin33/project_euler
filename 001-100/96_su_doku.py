import numpy as np
from pprint import pprint


class Sudoku:
    def __init__(self, board, silent):
        self.silent = silent
        self.board = board
        zero_coords = np.where(self.board == 0)
        unknown_coordinates = list(zip(zero_coords[0], zero_coords[1]))
        self.state = [
            ("Solving the following sudoku...", board)
        ]  # (description, board)

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

        self.cells_coordinates = [
            [
                coord
                for coord in self.get_cell_coordinates((3 * i, 3 * j))
                if coord in self.possible_values.keys()
            ]
            for i in range(3)
            for j in range(3)
        ]

        self.rows_coordinates = [
            [
                coord
                for coord in self.get_row_coordinates((i, 0))
                if coord in self.possible_values.keys()
            ]
            for i in range(9)
        ]

        self.cols_coordinates = [
            [
                coord
                for coord in self.get_col_coordinates((0, i))
                if coord in self.possible_values.keys()
            ]
            for i in range(9)
        ]
        self.step = 1

    def get_cell_coordinates(self, coord):
        cell_x, cell_y = coord[0] // 3, coord[1] // 3
        cell_neighbors_coordinates = [
            (3 * cell_x + k, 3 * cell_y + i)
            for i in range(3)
            for k in range(3)
            # if (3 * cell_x + k, 3 * cell_y + i) != coord
        ]
        return cell_neighbors_coordinates

    def get_cell_neighbors_values(self, coord):
        cell_neighbors = set(
            self.board[x, y] for x, y in self.get_cell_coordinates(coord)
        )
        return cell_neighbors

    def get_row_coordinates(self, coord):
        x, _ = coord
        row_neighbors_coordinates = [(x, i) for i in range(9)]
        row_neighbors_coordinates = [c for c in row_neighbors_coordinates]
        return row_neighbors_coordinates

    def get_col_coordinates(self, coord):
        _, y = coord
        col_neighbors_coordinates = [(i, y) for i in range(9)]
        col_neighbors_coordinates = [c for c in col_neighbors_coordinates]
        return col_neighbors_coordinates

    def get_X_coordinates(self, coord):
        X_neighbors_coordinates = self.get_row_coordinates(
            coord
        ) + self.get_col_coordinates(coord)
        return X_neighbors_coordinates

    def get_X_neighbors_values(self, coord):
        # print(f"Getting X neighbors for {coord}")
        x, y = coord
        X_neighbors = set(self.board[x, y] for x, y in self.get_X_coordinates(coord))
        # print(X_neighbors)
        return X_neighbors

    def print_sudoku(self, board=None, silent=False):
        print_message = ""

        for i, row in enumerate(board if board is not None else self.board):
            # Add horizontal lines every 3 rows
            if i % 3 == 0 and i != 0:
                print_message += "-" * 21
                print_message += "\n"
                if not self.silent and not silent:
                    print("-" * 21)
            row_str = ""
            for j, val in enumerate(row):
                # Add vertical lines every 3 columns
                if j % 3 == 0 and j != 0:
                    row_str += "| "
                # Replace 0 with empty space for better readability
                row_str += str(val)
                row_str += " "
            print_message += row_str
            print_message += "\n"

            if not self.silent and not silent:
                print(row_str)
        print_message += "\n"
        if not self.silent and not silent:
            print()
        return print_message

    def print_step(self, action, final=False, silent=False):
        description = f"{f'Step {self.step} ' if not final else ''}{action}"
        self.state.append((description, self.board.copy()))
        self.step += 1
        if not self.silent:
            print(description)
            self.print_sudoku()

    def naked_singles(self):
        # get naked singles
        defined_coordinates = []
        for coordinate, values in self.possible_values.items():
            if len(values) == 1:
                defined_coordinates.append(coordinate)
        # set naked single
        for coordinate in defined_coordinates:
            value = self.possible_values[coordinate][0]
            self.board[coordinate[0], coordinate[1]] = value
            self.print_step(
                f"Naked single - R{coordinate[0]+1}C{coordinate[1]+1} = {value}"
            )
        self.clean_possible_values(defined_coordinates)

    def pointing_pair(self):
        changed_coordinates = []

        # Check each block (3x3 subgrid) for pointing pairs
        for cell_index, block_coords in enumerate(self.cells_coordinates):
            candidate_map = {i: [] for i in range(1, 10)}

            # Collect coordinates for each candidate in the block
            for coord in block_coords:
                if coord in self.possible_values:  # Check if the coordinate is still unsolved
                    for value in self.possible_values[coord]:
                        candidate_map[value].append(coord)

            # Look for pointing pairs
            for value, coords in candidate_map.items():
                if len(coords) == 2:
                    # Check if the two coordinates are aligned horizontally or vertically
                    if coords[0][0] == coords[1][0]:  # Same row
                        row = coords[0][0]
                        col_range = {coords[0][1], coords[1][1]}
                        for col_coord in self.rows_coordinates[row]:
                            if col_coord[1] not in col_range and col_coord in self.possible_values:
                                if value in self.possible_values[col_coord]:
                                    self.possible_values[col_coord].remove(value)
                                    changed_coordinates.append(col_coord)
                                    self.print_step(
                                        f"Pointing pair in Cell {cell_index + 1} - Eliminated {value} from R{col_coord[0] + 1}C{col_coord[1] + 1}"
                                    )
                    elif coords[0][1] == coords[1][1]:  # Same column
                        col = coords[0][1]
                        row_range = {coords[0][0], coords[1][0]}
                        for row_coord in self.cols_coordinates[col]:
                            if row_coord[0] not in row_range and row_coord in self.possible_values:
                                if value in self.possible_values[row_coord]:
                                    self.possible_values[row_coord].remove(value)
                                    changed_coordinates.append(row_coord)
                                    self.print_step(
                                        f"Pointing pair in Cell {cell_index + 1} - Eliminated {value} from R{row_coord[0] + 1}C{row_coord[1] + 1}"
                                    )

        # Ensure that we only attempt to clean coordinates that still exist
        self.clean_possible_values([coord for coord in changed_coordinates if coord in self.possible_values])


    def hidden_singles_all(self):
        for index, cell_coordinates in enumerate(self.cells_coordinates):
            coordinates = [
                coordinate
                for coordinate in cell_coordinates
                if coordinate in self.possible_values.keys()
            ]
            self.hidden_singles(coordinates, "cell", index)

        for index, row_coordinates in enumerate(self.rows_coordinates):
            coordinates = [
                coordinate
                for coordinate in row_coordinates
                if coordinate in self.possible_values.keys()
            ]
            self.hidden_singles(coordinates, "row", index)

        for index, col_coordinates in enumerate(self.cols_coordinates):
            coordinates = [
                coordinate
                for coordinate in col_coordinates
                if coordinate in self.possible_values.keys()
            ]
            self.hidden_singles(coordinates, "col", index)

    def hidden_singles(self, coordinates, type, index):
        occurences_cell = {i: 0 for i in range(1, 10)}

        for coord in coordinates:
            for count in self.possible_values[coord]:
                occurences_cell[count] += 1

        changed_coordinates = []
        # set hidden single
        for value, count in occurences_cell.items():
            if count == 1:
                neighbor = [
                    neighbor
                    for neighbor in coordinates
                    if value in self.possible_values[neighbor]
                ][0]
                self.board[neighbor] = value
                changed_coordinates.append(neighbor)
                self.print_step(
                    f"Hidden single in {type.capitalize()} {index+1} - R{neighbor[0]+1}C{neighbor[1]+1} = {value}"
                )
        self.clean_possible_values(changed_coordinates)

    def clean_possible_values(self, coordinates):

        # remove possibilities from neighbors
        for coord in coordinates:
            del self.possible_values[coord]

            value = self.board[coord[0], coord[1]]

            neighbors = self.get_cell_coordinates(coord) + self.get_X_coordinates(coord)

            neighbors = [i for i in neighbors if i in self.possible_values.keys()]
            for neighbor in neighbors:
                if value in self.possible_values[neighbor]:
                    self.possible_values[neighbor].remove(value)

    def next(self):
        self.naked_singles()
        self.hidden_singles_all()
        self.pointing_pair()  # Add this line

    def solve(self, show_steps=False, output_text=None):
        i = 1
        while len(self.possible_values) and i < 100:
            self.next()
            i += 1
        self.print_step("Solved sudoku:", final=True)

        if show_steps:
            if output_text is not None:
                with open(output_text, "w") as file:
                    for description, board in self.state:
                        file.write(description)
                        file.write("\n")
                        file.write(self.print_sudoku(board, silent=True))
        return self.board


def open_sudoku_file():
    with open("./96_input.txt") as file:
        text = file.readlines()
        sudokus = [text[1 + 10 * i : 10 + 10 * i] for i in range(50)]
        sudokus = [
            np.array([[int(x) for x in list(line.strip("\n"))] for line in sudoku])
            for sudoku in sudokus
        ]
    return sudokus


sudokus = open_sudoku_file()


s = Sudoku(sudokus[5], silent=False)
s.print_sudoku()
board = s.solve(show_steps=True, output_text="output.txt")
s.print_sudoku(board)
# answer += sum(board[0,0:3])

# answer = 0
# for sudoku in sudokus:
#     s = Sudoku(sudoku)
#     s.print_sudoku()
#     board = s.solve(show_steps=True, output_text="output.txt")
#     s.print_sudoku(board)
#     answer += sum(board[0,0:3])
