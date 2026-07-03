class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        n1 = len(s1)
        n2 = len(s2)
        
        dp_prefix = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp_prefix[i][j] = dp_prefix[i - 1][j - 1] + 1
                else:
                    dp_prefix[i][j] = max(dp_prefix[i - 1][j], dp_prefix[i][j - 1])
                    
        original_lcs = dp_prefix[n1][n2]
        
        dp_suffix = [[0] * (n2 + 2) for _ in range(n1 + 2)]
        for i in range(n1, 0, -1):
            for j in range(n2, 0, -1):
                if s1[i - 1] == s2[j - 1]:
                    dp_suffix[i][j] = dp_suffix[i + 1][j + 1] + 1
                else:
                    dp_suffix[i][j] = max(dp_suffix[i + 1][j], dp_suffix[i][j + 1])
                    
        char_positions = {}
        for j, char in enumerate(s2):
            if char not in char_positions:
                char_positions[char] = []
            char_positions[char].append(j)
            
        ways = 0
        
        for i in range(n1 + 1):
            for char in char_positions:
                for j in char_positions[char]:
                    if dp_prefix[i][j] + dp_suffix[i + 1][j + 2] == original_lcs:
                        ways += 1
                        break  
                        
        return ways
