class Solution:
    def findInOutDegree(self, V, edges):
        # code hear
        in_degree = [0] * V
        out_degree = [0] * V
        for u, v in edges:
            out_degree[u] += 1
            in_degree[v] += 1
        result = []
        for i in range(V):
            result.append([in_degree[i], out_degree[i]])
            
        return result
