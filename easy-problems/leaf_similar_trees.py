class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaves_iterative(root):
            if not root:
                return []

            stack = [root]
            leaves = []

            while stack:
                node = stack.pop()

                if not node.left and not node.right:
                    leaves.append(node.val)

                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

            return leaves

        return get_leaves_iterative(root1) == get_leaves_iterative(root2)

    def leafSimilar_v_2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafFinder(root):
            if not root:
                return []
            if root.left is None and root.right is None:
                return [root.val]
            leftLeaf = leafFinder(root.left)
            rightLeaf = leafFinder(root.right)
            return leftLeaf + rightLeaf

        return leafFinder(root1) == leafFinder(root2)
