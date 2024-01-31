from grid import Grid
from solver import Solver

data_path = "/home/onyxia/work/projet_info/input/"
file_name = data_path + "grid1.in"


print(file_name)


g = Grid.grid_from_file(file_name)

s = Solver()
print(s)
print(s.get_solution(g))


