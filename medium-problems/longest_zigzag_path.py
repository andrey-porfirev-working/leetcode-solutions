class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def check_zigzag(node, go_left, steps):
            if node:
                self.max_len = max(self.max_len, steps)
                if go_left:
                    check_zigzag(node.left, False, steps+1)
                    check_zigzag(node.right, True, 1)
                else:
                    check_zigzag(node.right, True, steps+1)
                    check_zigzag(node.left, False, 1)
        check_zigzag(root, True, 0)
        check_zigzag(root, False, 0)
        return self.max_len