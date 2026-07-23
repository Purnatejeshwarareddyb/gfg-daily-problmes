class Solution:
    def canRepresentBST(self, arr):
        # code hear
        
        low_bound = float('-inf')
        stack = []
        
        for val in arr:
            if val < low_bound:
                return False
                
            while stack and stack[-1] < val:
                low_bound = stack.pop()
                
            stack.append(val)
            
        return True
