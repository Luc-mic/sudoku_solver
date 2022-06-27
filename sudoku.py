import numpy as np

def create_grid():
    grid = np.zeros((9, 9), dtype=np.int8)
    return grid

def create_grid_test():
    grid = np.zeros((9, 9), dtype=np.int8)
    for i in range(9):
        for j in range(9):
            grid[i, j] = i*9 + j
    return grid

def load_grid(grid, data):
    for i in range(9):
        for j in range(9):
            grid[i, j] = np.int8(data[i*9 + j])
    return grid

def save_grid(grid):
    data = ""
    for i in range(9):
        for j in range(9):
            data += str(grid[i, j])
    return data

def print_grid(grid):
    print("-------------------------")
    for i in range(9):
        print(f"| {grid[i][0]} {grid[i][1]} {grid[i][2]} | {grid[i][3]} {grid[i][4]} {grid[i][5]} | {grid[i][6]} {grid[i][7]} {grid[i][8]} |")
        if i == 2 or i == 5 or i == 8:
            print("-------------------------")

def get_column(grid, n):
    assert n >= 0 and n <= 8, "Wrong column number"
    return grid[:, n].flatten()

def get_line(grid, n):
    assert n >= 0 and n <= 8, "Wrong line number"
    return grid[n, :].flatten()

def get_cell(grid, n):
    assert n >= 0 and n <= 8, "Wrong square number"
    square = []
    lines = [n // 3 * 3, n // 3 * 3 + 1, n // 3 * 3 + 2]
    columns = [n % 3 * 3, n % 3 * 3 + 1, n % 3 * 3 + 2]

    for i in lines:
        for j in columns:
            square.append(grid[i, j])

    return square

def check_dupplicate(element):
    hashmap = {}
    for i in range(9):
        if element[i] != 0:
            if not hashmap.get(element[i]):
                hashmap[element[i]] = i
            else:
                return False, hashmap[element[i]], i
    return True, -1, -1

def test_grid(grid):
    for i in range(9):
        line = get_line(grid, i)
        column = get_column(grid, i)
        cell = get_cell(grid, i)
        if not (sum(line) == 45 and sum(column) == 45 and sum(cell) == 45):
            return False
        else :
            if not (check_dupplicate(line)[0] and check_dupplicate(column)[0] and check_dupplicate(cell)[0]):
                return False
    return True

def get_available_values(grid, index):
    line = get_line(grid, index // 9)
    column = get_column(grid, index % 9)
    cell = get_cell(grid, (index % 9) // 3 + 3 * (index // 27))
    available_values = {}
    for i in range(1, 10):
        available_values[i] = True
    for value in line:
        if value != 0:
            available_values[value] = False
    for value in column:
        if value != 0:
            available_values[value] = False
    for value in cell :
        if value != 0:
            available_values[value] = False
    return available_values
        


def backtracking_solving(grid, index):

    # Check if this is the last unknown value
    available_values = get_available_values(grid, index)
    last_value = True
    if index != 80:
        for i in range(index + 1, 81):
            if grid[i // 9, i % 9] == 0:
                next_index = i
                last_value = False
                break
    
    # Index 0 case:
    if index == 0 :
        if last_value == True:
            for i in range(1, 10):
                if available_values[i] == True:
                    grid[index // 9, index % 9] = i
                    if test_grid(grid):
                        return grid
            grid[index // 9, index % 9] = 0
            return grid
        else :
            if grid[index // 9, index % 9] == 0:
                for i in range(1, 10):
                    if available_values[i] == True:
                        grid[index // 9, index % 9] = i
                        deeper_result = backtracking_solving(grid, next_index)
                        if deeper_result != 0:
                            return grid
                grid[index // 9, index % 9] = 0
                return grid
            else :
                deeper_result = backtracking_solving(grid, next_index)
                return grid

    # Last unknown value case
    if last_value == True:
        for i in range(1, 10):
            if available_values[i] == True:
                grid[index // 9, index % 9] = i
                if test_grid(grid):
                    if index == 0:
                        return grid
                    else:
                        return i
        grid[index // 9, index % 9] = 0
        return 0

    # Other cases
    for i in range(1, 10):
        if available_values[i] == True:
            grid[index // 9, index % 9] = i
            deeper_result = backtracking_solving(grid, next_index)
            if deeper_result != 0:
                return i
    grid[index // 9, index % 9] = 0
    return 0
        