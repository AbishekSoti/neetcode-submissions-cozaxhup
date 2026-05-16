class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # # get those values from matrix. then add
        # list_to_add = []
        # # for each row, get the desired column length then go from there.
        # print(self.matrix)
        # print(row1,row2,col1,col2)
        # # row 2 to row 4, col1 to col3(count starts from 0, upper range -1)
        

        #so i must get all rows from row 1 to row 2. i can do it in a loop.
        total_of_that_row = 0
        for i in range(row1,row2+1):
            total_of_that_row += sum(self.matrix[i][col1:col2+1])
        return total_of_that_row
            

      


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)