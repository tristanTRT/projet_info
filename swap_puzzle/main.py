from grid import Grid
from solver import Solver

data_path = "/home/onyxia/work/projet_info/input/"
file_name = data_path + "grid1.in"




g = Grid.grid_from_file(file_name)
print(g)

s = Solver()

print(s.get_solution(g))


