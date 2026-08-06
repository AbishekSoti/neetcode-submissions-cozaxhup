class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check for the row for duplicates
        for i in range(0,len(board)):
            list_of_values = []
            for j in board[i]:
                if j != ".":
                    list_of_values.append(j)
            if len(set(list_of_values)) != len(list_of_values):
                print("there is a repeat in the row")
                return False


        # Check for the column for duplicates
        for i in range(0,len(board)): # 0 - 8.
            list_of_col_values = []
            for j in range(0,len(board[i])):
                if board[j][i] != ".":
                    list_of_col_values.append(board[j][i])
            if len(list_of_col_values)!= len(set(list_of_col_values)):
                print("column repeat")
                return False

        # Check for adjacent 1 square from middle and figure out.
        # Make a area checker funciton
        def area_checker(row_start,col_start):

            set_of_relevant_values = set()

            for row in range(row_start,row_start+3):
                for col in range(col_start, col_start+3):
                    if board[row][col] != '.':
                        if board[row][col] in set_of_relevant_values:
                            return False
                        else:
                            set_of_relevant_values.add(board[row][col])
            

        for i in range(0,9,3):
            for j in range(0,9,3):
                output = area_checker(i,j)
                if output == False:
                    return output
        return True








