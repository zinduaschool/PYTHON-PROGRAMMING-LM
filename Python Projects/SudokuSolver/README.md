# SudokuSolver
## How a sudoku grid looks like :

![Sudoku](https://www.learn-sudoku.com/images/start2finish.gif)

##
##
## Playing Sudoku
### 1. Only use the numbers 1 to 9 in a game of Sudoku.
Standard Sudoku games are played in grids with 9 blocks x 9 blocks. The columns and rows make up 9 squares that feature spaces of 3 x 3. Every single row, square, and column must be filled in with the numbers 1 to 9. The catch is that you can only use each number once – no numbers can be repeated in a row, column, or square.
Each Sudoku puzzle published already has a number of the blocks filled in, to make things a little simpler and to serve as clues for the final solution to the puzzle.

### 2. Avoid trying to guess the solution to the Sudoku puzzle.
It is tempting to try to guess the solution to a Sudoku puzzle when you are just starting out. For beginners (and pros), this is usually not a good idea. Sudoku is not a guessing game; therefore guessing shouldn’t form part of your game strategy. You might find that guessing only leads to wasting time.

### 3. Only use each number once – do not repeat any numbers.
You can only use each number once in each sub-grid row and column, as well as just once on the entire grid’s rows and columns. Is this possible? It actually is! To do this, you will need to note which numbers happen to be missing from each of the columns, rows, and blocks. Deductive reasoning and the process of elimination can be used to determine which missing numbers belong in which blocks on the grid.

### 4. You can use the process of elimination as a tactic.
The process of elimination is actually a great tactic as by knowing which numbers are already present, you can start to reason which numbers are missing and which best go into the open blocks.


### 
### 
****
****
# Sudoku solver
Given the sudoku puzzle **grid** you are to fill it full using the function **sudoku_solver**

**NB :** You are allowed to construct your own _helper functions_ , but do not delete the **sudoku_solver** function,and make sure all your other functions can run from within **sudoku_solver** function.


Helper function are function that are called by the 'main' function, in this case **sudoku_solver** so as to execute certain tasks within it.
e.g
```
def SUM(a,b):
  return a+b

def MULTIPLY(a,b,n)
  multiplication_val  = n*sum(a,b)
  return multiplication_val
```
_**In the above case SUM is a helper function to MULTIPLY **_


Delete **raise RuntimeError()** function when writing your code within **sudoku_solver** .

Note : The partially filled Sudoku is set in such a way there can only be one solution so the assertion error should work if your sudoku puzzle is filled in correctly.



