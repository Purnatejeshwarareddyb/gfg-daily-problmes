class Solution:
    def nthCharacter(self, n: int) -> str:
        num_digits = 1
        count = 9
        start = 1
        while n > num_digits * count:
            n -= num_digits * count
            start *= 10
            num_digits += 1
            count *= 10
        target_num = start + (n - 1) // num_digits
        return str(target_num)[(n - 1) % num_digits]