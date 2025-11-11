class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, current_sum, prefix_sum):
            if not node:
                return 0

            current_sum += node.val
            count = prefix_sum.get(current_sum - targetSum, 0)

            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum, prefix_sum)
            count += dfs(node.right, current_sum, prefix_sum)

            prefix_sum[current_sum] -= 1
            if prefix_sum[current_sum] == 0:
                del prefix_sum[current_sum]

            return count

        return dfs(root, 0, {0: 1})

    def pathSum_v_2(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0

        def dfs(node, current_sum):
            if not node:
                return 0
            count = 0
            current_sum += node.val
            if current_sum == targetSum:
                count += 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            return count

        def traverse(node):
            if not node:
                return 0
            paths_from_here = dfs(node, 0)
            paths_from_left = traverse(node.left)
            paths_from_right = traverse(node.right)
            return paths_from_here + paths_from_left + paths_from_right

        return traverse(root)