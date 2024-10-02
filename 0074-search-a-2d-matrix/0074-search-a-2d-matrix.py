class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Initialize pointers to traverse the rows
        top_row, bottom_row = 0, num_rows - 1

        # Binary search to find the potential row that may contain the target
        while top_row <= bottom_row:
            middle_row = top_row + ((bottom_row - top_row) // 2)
            
            # If target is greater than the last element of the middle row, it must be in a lower row
            if target > matrix[middle_row][-1]:
                top_row = middle_row + 1
            # If target is less than the first element of the middle row, it must be in a higher row
            elif target < matrix[middle_row][0]:
                bottom_row = middle_row - 1
            # Target is within the range of the current row
            else:
                break

        # If no valid row is found (target is not within any row range)
        # if not (top_row <= bottom_row):
        if top_row > bottom_row:
            return False

        # Determine the row that may contain the target value
        target_row = top_row + ((bottom_row - top_row) // 2)

        # Initialize pointers to perform binary search within the selected row
        left_col, right_col = 0, num_cols - 1

        # Binary search within the target row to find the target value
        while left_col <= right_col:
            middle_col = (left_col + right_col) // 2

            # If the target is greater than the middle element, it must be in the right half
            if target > matrix[target_row][middle_col]:
                left_col = middle_col + 1
            # If the target is less than the middle element, it must be in the left half
            elif target < matrix[target_row][middle_col]:
                right_col = middle_col - 1
            # Target is found
            else:
                return True

        # Target is not found in the matrix
        return False

        #log(m) + log(n) = log(m * n)

        
        