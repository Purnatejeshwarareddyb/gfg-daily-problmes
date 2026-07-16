class Solution:
    def dfs(self, adj):
        # Determine the number of vertices
        V = len(adj)
        
        # Array to keep track of visited vertices
        visited = [False] * V
        ans = []
        
        # Helper function for recursive DFS
        def dfs_helper(node):
            # Mark the current node as visited and add to result
            visited[node] = True
            ans.append(node)
            
            # Recur for all adjacent vertices in order
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_helper(neighbor)
                    
        # Start DFS from vertex 0
        dfs_helper(0)
        
        return ans
