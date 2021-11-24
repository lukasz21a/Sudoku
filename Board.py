class Board:
    """
    Creates a Board object (the sudoku board) - a 9x9 list of lists of ints.
    The class includes all methods required to properly fill the given
    incomplete sudoku board, and to print out the result.
    """
    def __init__(self, board):
        self.board = board

    def __check(self, pos_x, pos_y, number):
        """
        Checks that the number doesn't repeat in the row, column and the 3x3 square.
        :param pos_x: the x position of the number to be checked
        :param pos_y: the y position of the number to be checked
        :param number: the number to be checked
        :rtype: bool
        """

        # Checks the row.
        row = self.board[pos_x]
        if number in row:
            return False

        # Checks the column.
        col = [self.board[i][pos_y] for i in range(9)]
        if number in col:
            return False

        # The starting index of the 3x3 square.
        x_start = pos_x // 3 * 3
        y_start = pos_y // 3 * 3

        # Checks the 3x3 square.
        for i in range(x_start, x_start + 3):
            for j in range(y_start, y_start + 3):
                if self.board[i][j] == number:
                    return False

        return True

    def __find_empty(self):
        """
        Searches for the x, y position of the empty cell (value 0).
        :return: x, y position
        """

        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return i, j

        return None

    def solve(self):
        """
        Solves sudoku using backtracking algorithm.
        :rtype: bool
        """

        # Finds the x, y position of the empty cell (value 0) in the board.
        if self.__find_empty() is not None:
            x, y = self.__find_empty()
        else:
            return True

        # For the given position, checks the numbers 1-9 one by one
        # if they match the sudoku criteria.
        # If it gets to the point of no solution, assigns 0 and goes back
        # to check for different numbers.
        for guess in range(1, 10):
            if self.__check(x, y, guess):
                self.board[x][y] = guess

                if self.solve():
                    return True

                self.board[x][y] = 0

        return False

    def print_board(self):
        """
        Prints the sudoku board with the separated 3x3 squares
        """

        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("---------------------")
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print("| ", end="")
                print(self.board[i][j], "", end="")
            print()
