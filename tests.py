from sudoku import *
import csv
import time

def test_grid_test():
    
    with open('sudoku_valid.csv', mode ='r') as file:
        lines = csv.reader(file)
    
        # displaying the contents of the CSV file

        grid = create_grid() 
        for line in lines:
            grid = load_grid(grid, line[0])
            assert test_grid(grid) == True, "Test grid error !"
        
        print("Test OK : test_grid valid")

    with open('sudoku_invalid.csv', mode ='r') as file:
        lines = csv.reader(file)
    
        # displaying the contents of the CSV file

        grid = create_grid()
        for line in lines:
            grid = load_grid(grid, line[0])
            assert test_grid(grid) == False, "Test grid error !"
        
        print("Test OK : test_grid invalid")


def test_grid_solver():
    
    with open('sudoku_to_solve2.csv', mode ='r') as file:
        lines = csv.reader(file)
    
        # displaying the contents of the CSV file

        grid = create_grid() 
        for line in lines:
            grid = load_grid(grid, line[0])
            t = time.time()
            solved_grid = backtracking_solving(grid, 0)
            assert test_grid(solved_grid) == True, "Solving error !"
            print(f"{save_grid(solved_grid)}, {time.time() - t}")

        print("Test OK : solve_grid")

# grid = create_grid()
# print(grid.shape)
# print_grid(grid)

# grid = create_grid_test()

# print_grid(grid)

test_grid_test()
test_grid_solver()