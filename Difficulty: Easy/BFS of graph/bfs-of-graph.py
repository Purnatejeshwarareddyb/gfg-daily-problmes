class Solution:
    def bfs(self, adj):
        # code hear 

        V = len(adj)
        if V == 0:
            return []
            
        visited = [False] * V
        bfs_traversal = []
        queue = []
        

        queue.append(0)
        visited[0] = True
        
        while queue:

            u = queue.pop(0)
            bfs_traversal.append(u)
            

            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    
        return bfs_traversal
