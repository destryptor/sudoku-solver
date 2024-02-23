import tkinter as tk
from tkinter import messagebox

M = 9

class SudokuSolverApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sudoku Solver")
        self.grid_edit = [[None]*M for _ in range(M)]
        self.initUI()

    def initUI(self):
        for i in range(M):
            for j in range(M):
                edit = tk.Entry(self, width=2, font=("Arial", 18))
                edit.grid(row=i, column=j)
                edit.config(highlightthickness=1, highlightbackground="black")
                self.grid_edit[i][j] = edit

        solve_button = tk.Button(self, text="Solve Sudoku", command=self.solveSudoku, font=("Arial", 14))
        solve_button.grid(row=M, column=0, columnspan=M, pady=10)

    def solveSudoku(self):
        grid = [[0]*M for _ in range(M)]
        for i in range(M):
            for j in range(M):
                text = self.grid_edit[i][j].get()
                if text.isdigit():
                    grid[i][j] = int(text)
        if self.Sudoku(grid, 0, 0):
            for i in range(M):
                for j in range(M):
                    self.grid_edit[i][j].delete(0, tk.END)
                    self.grid_edit[i][j].insert(0, str(grid[i][j]))
        else:
            messagebox.showerror("Error", "Solution does not exist :(")

    def solve(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
        for x in range(9):
            if grid[x][col] == num:
                return False
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True

    def Sudoku(self, grid, row, col):
        if (row == M - 1 and col == M):
            return True
        if col == M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return self.Sudoku(grid, row, col + 1)
        for num in range(1, M + 1, 1): 
            if self.solve(grid, row, col, num):
                grid[row][col] = num
                if self.Sudoku(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False

if __name__ == "__main__":
    app = SudokuSolverApp()
    app.mainloop()
