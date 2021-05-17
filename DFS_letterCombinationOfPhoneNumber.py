import string
from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        all_letters = string.ascii_lowercase
        idx = 0
        num_to_letter = dict()
        for i in range(10):
            if i not in (0,1,7,9):
                num_to_letter[str(i)] = list(all_letters[idx:idx+3])
                idx = idx+3

            elif i == 7 or i ==9:
                num_to_letter[str(i)] = list(all_letters[idx:idx+4])
                idx = idx+4
        num_to_letter[-1] = ""
        def dfs(idx_digit,idx):
            if idx_digit == len(digits)-1:
                return [num_to_letter[digits[idx_digit]][idx]]

            result = []
            cur_letter = "" if idx_digit ==-1 else num_to_letter[digits[idx_digit]][idx]
            for i in range(len(num_to_letter[digits[idx_digit+1]])):
                next_re = dfs(idx_digit+1,i)
                new_result = [cur_letter+j for j in next_re]
                result += new_result

            return result

        return dfs(-1,0)
