#Sudoku solver
import numpy as np

grid=[[8,0,0,4,0,6,0,0,7],
      [0,0,0,0,0,0,4,0,0],
      [0,1,0,0,0,0,6,5,0],
      [5,0,9,0,3,0,7,8,0],
      [0,0,0,0,7,0,0,0,0],
      [0,4,8,0,2,0,1,0,3],
      [0,5,2,0,0,0,0,9,0],
      [0,0,1,0,0,0,0,0,0],
      [3,0,0,9,0,2,0,0,5]] 

# You can add your own helper function below here



def sudoku_solver():
  global grid  
 
  #put your code here

  raise RuntimeError() # Delete this line when you add your code in the function




sudoku_solver()


solution = [[8,3,5,4,1,6,9,2,7],
            [2,9,6,8,5,7,4,3,1],
            [4,1,7,2,9,3,6,5,8],
            [5,6,9,1,3,4,7,8,2],
            [1,2,3,6,7,8,5,4,9],
            [7,4,8,5,2,9,1,6,3],
            [6,5,2,7,8,1,3,9,4],
            [9,8,1,3,4,5,2,7,6],
            [3,7,4,9,6,2,8,1,5]]


assert(solution == grid)
print(np.matrix(grid))
