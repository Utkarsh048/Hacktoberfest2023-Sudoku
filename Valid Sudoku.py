class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sub_box_sets = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                digit = board[i][j]

                if digit == '.':
                    continue

                if digit in row_sets[i]:
                    return False
                row_sets[i].add(digit)

                if digit in col_sets[j]:
                    return False
                col_sets[j].add(digit)

                sub_box_idx = (i // 3) * 3 + j // 3
                if digit in sub_box_sets[sub_box_idx]:
                    return False
                sub_box_sets[sub_box_idx].add(digit)

        return True
