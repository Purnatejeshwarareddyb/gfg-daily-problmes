class Solution:
    def partyHouse(self, adj: list[list[int]]) -> int:
        # code here
        n = len(adj)

        def get_farthest_and_dist(start_node):
            dist = [-1] * (n + 1)
            dist[start_node] = 0
            queue = [start_node]

            farthest_node = start_node
            max_d = 0

            while queue:
                curr = queue.pop(0)
                if dist[curr] > max_d:
                    max_d = dist[curr]
                    farthest_node = curr

                for neighbor in adj[curr - 1]:
                    if dist[neighbor] == -1:
                        dist[neighbor] = dist[curr] + 1
                        queue.append(neighbor)

            return farthest_node, max_d

        u, _ = get_farthest_and_dist(1)

        _, diameter = get_farthest_and_dist(u)

        return (diameter + 1) // 2