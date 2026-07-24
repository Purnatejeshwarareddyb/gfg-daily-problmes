class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code hear
        
        # Build Adjacency List
        adj = [[] for _ in range(V)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        #  Initialize Distances
        dist = [float('inf')] * V
        dist[src] = 0
        
        # Custom Min-Heap Implementation
        heap = [(0, src)]  # Stores tuples of (distance, vertex)
        
        def push(item):
            heap.append(item)
            # Bubble up
            curr = len(heap) - 1
            while curr > 0:
                parent = (curr - 1) // 2
                if heap[curr][0] < heap[parent][0]:
                    heap[curr], heap[parent] = heap[parent], heap[curr]
                    curr = parent
                else:
                    break
                    
        def pop():
            if not heap:
                return None
            if len(heap) == 1:
                return heap.pop()
            
            root = heap[0]
            heap[0] = heap.pop()
            # Bubble down
            curr = 0
            n = len(heap)
            while True:
                left = 2 * curr + 1
                right = 2 * curr + 2
                smallest = curr
                
                if left < n and heap[left][0] < heap[smallest][0]:
                    smallest = left
                if right < n and heap[right][0] < heap[smallest][0]:
                    smallest = right
                    
                if smallest != curr:
                    heap[curr], heap[smallest] = heap[smallest], heap[curr]
                    curr = smallest
                else:
                    break
            return root

        # 4. Dijkstra Main Loop
        while heap:
            pop_res = pop()
            if not pop_res:
                break
            d, u = pop_res
            
            # Skip obsolete heap entries
            if d > dist[u]:
                continue
                
            # Relax edges
            for v, w in adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    push((dist[v], v))
                    
        return dist
