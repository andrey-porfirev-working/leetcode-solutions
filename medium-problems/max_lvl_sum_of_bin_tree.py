class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = [root]  # обычный список вместо deque
        max_sum = float("-inf")
        max_level = 0
        level = 0

        while queue:
            level += 1
            level_size = len(queue)
            current_sum = 0
            next_level = []

            for node in queue:
                current_sum += node.val
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                max_level = level

            queue = next_level

        return max_level