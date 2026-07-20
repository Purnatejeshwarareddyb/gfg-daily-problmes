class Solution:
    def findPrefixes(self, arr):
        # code hear
        root = {}
        for word in arr:
            node = root
            for char in word:
                if char not in node:
                    node[char] = {"_count": 0}
                node = node[char]
                node["_count"] += 1
        
        result = []
        for word in arr:
            node = root
            prefix = ""
            for char in word:
                prefix += char
                node = node[char]
                if node["_count"] == 1:
                    break
            result.append(prefix)
            
        return result
