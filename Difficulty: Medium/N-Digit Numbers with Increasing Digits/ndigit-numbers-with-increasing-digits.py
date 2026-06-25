class Solution:
    def increasingNumbers(self, n: int) -> list[int]:
        if n == 1:
            return list(range(10))
        if n > 9:
            return []
        
        res = []
        def backtrack(curr_num, last_digit, length):
            if length == n:
                res.append(curr_num)
                return
            for next_digit in range(last_digit + 1, 10):
                backtrack(curr_num * 10 + next_digit, next_digit, length + 1)
                
        for start_digit in range(1, 10):
            backtrack(start_digit, start_digit, 1)
            
        return res
