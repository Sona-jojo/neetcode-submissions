class Solution:
    from collections import defaultdict        # 🔧 Added import for defaultdict
from typing import List                    # 🔧 Added import for List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)            # ✅ Proper indentation
        cols = defaultdict(set)            # ✅ Proper indentation
        squares = defaultdict(set)         # ✅ Proper indentation

        for r in range(9):                 # 🔧 Fixed indentation
            for c in range(9):             # 🔧 Fixed indentation
                if board[r][c] == ".":     # 🔧 Fixed indentation
                    continue

                val = board[r][c]          # 🔧 Added intermediate variable for clarity
                if (val in rows[r] or
                    val in cols[c] or
                    val in squares[(r // 3, c // 3)]):  # 🔧 Added spaces around `//`
                    return False

                rows[r].add(val)           # 🔧 Fixed: was cols[r].add()
                cols[c].add(val)           # ✅ Correct
                squares[(r // 3, c // 3)].add(val)  # ✅ Correct

        return True                        # 🔧 Fixed indentation and capitalization (True not true)


            


