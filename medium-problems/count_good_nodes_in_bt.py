class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def check_roots(root_to_check, max_val):
            if not root_to_check:
                return 0
            good_nodes = 0
            if root_to_check.val >= max_val:
                good_nodes = 1
                max_val = root_to_check.val
            good_nodes += check_roots(root_to_check.left, max_val)
            good_nodes += check_roots(root_to_check.right, max_val)
            return good_nodes
        return check_roots(root, root.val)