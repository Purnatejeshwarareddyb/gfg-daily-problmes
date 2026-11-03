class Solution:

  def maximumWeight(self, n, edges, queries):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    indexed_queries = sorted(enumerate(queries), key=lambda x: x[1])

    parent = list(range(n + 1))
    size = [1] * (n + 1)
    total_paths = 0

    def find(i):
      path = []
      while parent[i] != i:
        path.append(i)
        i = parent[i]
      for node in path:
        parent[node] = i
      return i

    ans = [0] * len(queries)
    edge_idx = 0
    num_edges = len(edges_sorted)

    for q_idx, x in indexed_queries:
      while edge_idx < num_edges and edges_sorted[edge_idx][2] <= x:
        u, v, w = edges_sorted[edge_idx]
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
          total_paths += size[root_u] * size[root_v]
          if size[root_u] < size[root_v]:
            root_u, root_v = root_v, root_u
          parent[root_v] = root_u
          size[root_u] += size[root_v]
        edge_idx += 1
      ans[q_idx] = total_paths

    return ans