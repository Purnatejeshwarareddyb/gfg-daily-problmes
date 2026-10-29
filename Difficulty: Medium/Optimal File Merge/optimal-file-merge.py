import heapq

class Solution:
    def minComputation(self, files):
        heapq.heapify(files)
        total_cost = 0
        while len(files) > 1:
            cost = heapq.heappop(files) + heapq.heappop(files)
            total_cost += cost
            heapq.heappush(files, cost)
        return total_cost