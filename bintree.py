class TreeNode:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self, nd):
        m = nd.value
        if m < self.value:
            if self.left is None:
                self.left = nd
            else:
                self.left.ins(nd)
        else:
            if self.right is None:
                self.right = nd
            else:
                self.right.ins(nd)
