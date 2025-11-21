class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = findMin(root.right)

            root.val = temp.val

            root.right = self.deleteNode(root.right, temp.val)

        return root


def findMin(node):
    current = node
    while current.left:
        current = current.left
    return current
