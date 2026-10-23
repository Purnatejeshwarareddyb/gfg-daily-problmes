''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:

    def pairsViolatingBST(self, root):
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.data] + inorder(node.right)

        arr = inorder(root)
        n = len(arr)

        def merge_sort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            inv_count = merge_sort(left, mid) + merge_sort(mid + 1, right)

            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    inv_count += mid - i + 1
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1

            for i in range(len(temp)):
                arr[left + i] = temp[i]
            return inv_count

        return merge_sort(0, n - 1)